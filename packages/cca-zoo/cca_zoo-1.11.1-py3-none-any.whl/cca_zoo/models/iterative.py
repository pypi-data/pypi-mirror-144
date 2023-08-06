import copy
import warnings
from abc import abstractmethod
from typing import Union, Iterable

import numpy as np

from cca_zoo.models import MCCA
from cca_zoo.models._cca_base import _CCA_Base
from cca_zoo.models._innerloop import (
    _PLSInnerLoop,
    _PMDInnerLoop,
    _ParkhomenkoInnerLoop,
    _ElasticInnerLoop,
    _ADMMInnerLoop,
    _SpanCCAInnerLoop,
    _SWCCAInnerLoop,
)
from cca_zoo.utils.check_values import _check_views


class _Iterative(_CCA_Base):
    """
    A class used as the base for iterative CCA methods i.e. those that optimize for each dimension one at a time with deflation.

    """

    def __init__(
        self,
        latent_dims: int = 1,
        scale: bool = True,
        centre=True,
        copy_data=True,
        random_state=None,
        deflation="cca",
        max_iter: int = 100,
        initialization: Union[str, callable] = "random",
        tol: float = 1e-9,
    ):
        """
        Constructor for _Iterative

        :param latent_dims: number of latent dimensions to fit
        :param scale: normalize variance in each column before fitting
        :param centre: demean data by column before fitting (and before transforming out of sample
        :param copy_data: If True, X will be copied; else, it may be overwritten
        :param random_state: Pass for reproducible output across multiple function calls
        :param deflation: the type of deflation.
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param initialization: either string from "pls", "cca", "random", "uniform" or callable to initialize the score variables for iterative methods
        :param tol: tolerance value used for early stopping
        """
        super().__init__(
            latent_dims=latent_dims,
            scale=scale,
            centre=centre,
            copy_data=copy_data,
            accept_sparse=["csc", "csr"],
            random_state=random_state,
        )
        self.max_iter = max_iter
        self.initialization = initialization
        self.tol = tol
        self.deflation = deflation

    def fit(self, views: Iterable[np.ndarray], y=None, **kwargs):
        """
        Fits the model by running an inner loop to convergence and then using either CCA or PLS deflation

        :param views: list/tuple of numpy arrays or array likes with the same number of rows (samples)
        """
        views = _check_views(
            *views, copy=self.copy_data, accept_sparse=self.accept_sparse
        )
        views = self._centre_scale(views)
        self.n_views = len(views)
        self.n = views[0].shape[0]
        if isinstance(self.initialization, str):
            initializer = _default_initializer(
                views, self.initialization, self.random_state, self.latent_dims
            )
        else:
            initializer = self.initialization()
        n = views[0].shape[0]
        p = [view.shape[1] for view in views]
        # List of d: p x k
        self.weights = [np.zeros((p_, self.latent_dims)) for p_ in p]
        self.loadings = [np.zeros((p_, self.latent_dims)) for p_ in p]

        # List of d: n x k
        self.scores = [np.zeros((n, self.latent_dims)) for _ in views]

        residuals = copy.deepcopy(list(views))
        self.track = []
        # For each of the dimensions
        for k in range(self.latent_dims):
            self._set_loop_params()
            self.loop = self.loop.fit(*residuals, initial_scores=next(initializer))
            for i, residual in enumerate(residuals):
                self.weights[i][:, k] = self.loop.weights[i].ravel()
                self.scores[i][:, k] = self.loop.scores[i].ravel()
                self.loadings[i][:, k] = np.dot(self.scores[i][:, k], residual)
                residuals[i] = self._deflate(
                    residuals[i], self.scores[i][:, k], self.weights[i][:, k]
                )
            self.track.append(self.loop.track)
            if not self.track[-1]["converged"]:
                warnings.warn(
                    f"Inner loop {k} not converged. Increase number of iterations."
                )
        return self

    def _deflate(self, residual, score, loading):
        """
        Deflate view residual by CCA deflation (https://ars.els-cdn.com/content/image/1-s2.0-S0006322319319183-mmc1.pdf)

        :param residual: the current residual data matrix
        :param score: the score for that view

        """
        if self.deflation == "cca":
            return (
                residual
                - np.outer(score, score) @ residual / np.dot(score, score).item()
            )
        elif self.deflation == "pls":
            return residual - np.outer(score, loading)
        else:
            raise ValueError(f"deflation method {self.deflation} not implemented yet.")

    @abstractmethod
    def _set_loop_params(self):
        """
        Sets up the inner optimization loop for the method. By default uses the PLS inner loop.
        """
        self.loop = _PLSInnerLoop(
            max_iter=self.max_iter,
            random_state=self.random_state,
        )


def _default_initializer(views, initialization, random_state, latent_dims):
    """
    This is a generator function which generates initializations for each dimension

    :param views:
    :param initialization:
    :param random_state:
    :param latent_dims:
    :return:
    """
    if initialization == "random":
        while True:
            yield np.array(
                [random_state.normal(0, 1, size=(view.shape[0])) for view in views]
            )
    elif initialization == "uniform":
        while True:
            yield np.array([np.ones(view.shape[0]) for view in views])
    elif initialization == "pls":
        latent_dim = 0
        # use rCCA to use multiple views
        pls_scores = MCCA(latent_dims, c=1).fit_transform(views)
        while True:
            yield np.stack(pls_scores)[:, :, latent_dim]
            latent_dim += 1
    elif initialization == "cca":
        latent_dim = 0
        cca_scores = MCCA(latent_dims).fit_transform(views)
        while True:
            yield np.stack(cca_scores)[:, :, latent_dim]
            latent_dim += 1
    else:
        raise ValueError(
            "Initialization {type} not supported. Pass a generator implementing this method"
        )


class PLS_ALS(_Iterative):
    r"""
    A class used to fit a PLS model

    Fits a partial least squares model with CCA deflation by NIPALS algorithm

    .. math::

        w_{opt}=\underset{w}{\mathrm{argmax}}\{\sum_i\sum_{j\neq i} \|X_iw_i-X_jw_j\|^2\}\\

        \text{subject to:}

        w_i^Tw_i=1

    :Example:

    >>> from cca_zoo.models import PLS
    >>> import numpy as np
    >>> rng=np.random.RandomState(0)
    >>> X1 = rng.random((10,5))
    >>> X2 = rng.random((10,5))
    >>> model = PLS_ALS(random_state=0)
    >>> model.fit((X1,X2)).score((X1,X2))
    array([0.81796854])
    """

    def __init__(
        self,
        latent_dims: int = 1,
        scale: bool = True,
        centre=True,
        copy_data=True,
        random_state=None,
        max_iter: int = 100,
        initialization: Union[str, callable] = "random",
        tol: float = 1e-9,
    ):
        """
        Constructor for PLS

        :param latent_dims: number of latent dimensions to fit
        :param scale: normalize variance in each column before fitting
        :param centre: demean data by column before fitting (and before transforming out of sample
        :param copy_data: If True, X will be copied; else, it may be overwritten
        :param random_state: Pass for reproducible output across multiple function calls
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param initialization: either string from "pls", "cca", "random", "uniform" or callable to initialize the score variables for iterative methods
        :param tol: tolerance value used for early stopping
        """
        super().__init__(
            latent_dims=latent_dims,
            scale=scale,
            centre=centre,
            copy_data=copy_data,
            deflation="pls",
            max_iter=max_iter,
            initialization=initialization,
            tol=tol,
            random_state=random_state,
        )

    def _set_loop_params(self):
        self.loop = _PLSInnerLoop(
            max_iter=self.max_iter,
            tol=self.tol,
            random_state=self.random_state,
        )


class ElasticCCA(_Iterative):
    r"""
    Fits an elastic CCA by iterating elastic net regressions.

    By default, ElasticCCA uses CCA with an auxiliary variable target i.e. MAXVAR configuration

    .. math::

        w_{opt}, t_{opt}=\underset{w,t}{\mathrm{argmax}}\{\sum_i \|X_iw_i-t\|^2 + c\|w_i\|^2_2 + \text{l1_ratio}\|w_i\|_1\}\\

        \text{subject to:}

        t^Tt=n


    :Citation:

    Fu, Xiao, et al. "Scalable and flexible multiview MAX-VAR canonical correlation analysis." IEEE Transactions on Signal Processing 65.16 (2017): 4150-4165.

    But we can force it to attempt to use the SUMCOR form which will approximate a solution to the problem:

    .. math::

        w_{opt}=\underset{w}{\mathrm{argmax}}\{\sum_i\sum_{j\neq i} \|X_iw_i-X_jw_j\|^2 + c\|w_i\|^2_2 + \text{l1_ratio}\|w_i\|_1\}\\

        \text{subject to:}

        w_i^TX_i^TX_iw_i=n

    :Example:

    >>> from cca_zoo.models import ElasticCCA
    >>> import numpy as np
    >>> rng=np.random.RandomState(0)
    >>> X1 = rng.random((10,5))
    >>> X2 = rng.random((10,5))
    >>> model = ElasticCCA(c=[1e-1,1e-1],l1_ratio=[0.5,0.5], random_state=0)
    >>> model.fit((X1,X2)).score((X1,X2))
    array([0.9316638])
    """

    def __init__(
        self,
        latent_dims: int = 1,
        scale: bool = True,
        centre=True,
        copy_data=True,
        random_state=None,
        deflation="cca",
        max_iter: int = 100,
        initialization: Union[str, callable] = "pls",
        tol: float = 1e-9,
        c: Union[Iterable[float], float] = None,
        l1_ratio: Union[Iterable[float], float] = None,
        maxvar: bool = True,
        stochastic=False,
        positive: Union[Iterable[bool], bool] = None,
    ):
        """
        Constructor for ElasticCCA

        :param latent_dims: number of latent dimensions to fit
        :param scale: normalize variance in each column before fitting
        :param centre: demean data by column before fitting (and before transforming out of sample
        :param copy_data: If True, X will be copied; else, it may be overwritten
        :param random_state: Pass for reproducible output across multiple function calls
        :param deflation: the type of deflation.
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param initialization: either string from "pls", "cca", "random", "uniform" or callable to initialize the score variables for iterative methods
        :param tol: tolerance value used for early stopping
        :param c: lasso alpha
        :param l1_ratio: l1 ratio in lasso subproblems
        :param maxvar: use auxiliary variable "maxvar" formulation
        :param stochastic: use stochastic regression optimisers for subproblems
        :param positive: constrain model weights to be positive
        """
        self.c = c
        self.l1_ratio = l1_ratio
        self.maxvar = maxvar
        self.stochastic = stochastic
        self.positive = positive
        if self.positive is not None and stochastic:
            self.stochastic = False
            warnings.warn(
                "Non negative constraints cannot be used with stochastic regressors. Switching to stochastic=False"
            )
        super().__init__(
            latent_dims=latent_dims,
            scale=scale,
            centre=centre,
            copy_data=copy_data,
            deflation=deflation,
            max_iter=max_iter,
            initialization=initialization,
            tol=tol,
            random_state=random_state,
        )

    def _set_loop_params(self):
        self.loop = _ElasticInnerLoop(
            max_iter=self.max_iter,
            c=self.c,
            l1_ratio=self.l1_ratio,
            maxvar=self.maxvar,
            tol=self.tol,
            stochastic=self.stochastic,
            positive=self.positive,
            random_state=self.random_state,
        )


class CCA_ALS(ElasticCCA):
    r"""
    Fits a CCA model with CCA deflation by NIPALS algorithm. Implemented by ElasticCCA with no regularisation

    :Maths:

    .. math::

        w_{opt}=\underset{w}{\mathrm{argmax}}\{\sum_i\sum_{j\neq i} \|X_iw_i-X_jw_j\|^2\}\\

        \text{subject to:}

        w_i^TX_i^TX_iw_i=n

    :Citation:

    Golub, Gene H., and Hongyuan Zha. "The canonical correlations of matrix pairs and their numerical computation." Linear algebra for signal processing. Springer, New York, NY, 1995. 27-49.

    :Example:

    >>> from cca_zoo.models import CCA_ALS
    >>> import numpy as np
    >>> rng=np.random.RandomState(0)
    >>> X1 = rng.random((10,3))
    >>> X2 = rng.random((10,3))
    >>> model = CCA_ALS(random_state=0)
    >>> model.fit((X1,X2)).score((X1,X2))
    array([0.858906])
    """

    def __init__(
        self,
        latent_dims: int = 1,
        scale: bool = True,
        centre=True,
        copy_data=True,
        random_state=None,
        deflation="cca",
        max_iter: int = 100,
        initialization: str = "random",
        tol: float = 1e-9,
        stochastic=True,
        positive: Union[Iterable[bool], bool] = None,
    ):
        """
        Constructor for CCA_ALS

        :param latent_dims: number of latent dimensions to fit
        :param scale: normalize variance in each column before fitting
        :param centre: demean data by column before fitting (and before transforming out of sample
        :param copy_data: If True, X will be copied; else, it may be overwritten
        :param random_state: Pass for reproducible output across multiple function calls
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param initialization: either string from "pls", "cca", "random", "uniform" or callable to initialize the score variables for iterative methods
        :param tol: tolerance value used for early stopping
        :param stochastic: use stochastic regression optimisers for subproblems
        :param positive: constrain model weights to be positive
        """

        super().__init__(
            latent_dims=latent_dims,
            max_iter=max_iter,
            initialization=initialization,
            tol=tol,
            stochastic=stochastic,
            centre=centre,
            copy_data=copy_data,
            scale=scale,
            positive=positive,
            random_state=random_state,
            deflation=deflation,
            maxvar=False,
        )


class SCCA(ElasticCCA):
    r"""
    Fits a sparse CCA model by iterative rescaled lasso regression. Implemented by ElasticCCA with l1 ratio=1

    For default maxvar=False, the optimisation is given by:

    :Maths:

    .. math::

        w_{opt}=\underset{w}{\mathrm{argmax}}\{\sum_i\sum_{j\neq i} \|X_iw_i-X_jw_j\|^2 + \text{l1_ratio}\|w_i\|_1\}\\

        \text{subject to:}

        w_i^TX_i^TX_iw_i=n

    :Citation:

    Mai, Qing, and Xin Zhang. "An iterative penalized least squares approach to sparse canonical correlation analysis." Biometrics 75.3 (2019): 734-744.

    For maxvar=True, the optimisation is given by the ElasticCCA problem with no l2 regularisation:

    :Maths:

    .. math::

        w_{opt}, t_{opt}=\underset{w,t}{\mathrm{argmax}}\{\sum_i \|X_iw_i-t\|^2 + \text{l1_ratio}\|w_i\|_1\}\\

        \text{subject to:}

        t^Tt=n

    :Citation:

    Fu, Xiao, et al. "Scalable and flexible multiview MAX-VAR canonical correlation analysis." IEEE Transactions on Signal Processing 65.16 (2017): 4150-4165.


    :Example:

    >>> from cca_zoo.models import SCCA
    >>> import numpy as np
    >>> rng=np.random.RandomState(0)
    >>> X1 = rng.random((10,5))
    >>> X2 = rng.random((10,5))
    >>> model = SCCA(c=[0.001,0.001], random_state=0)
    >>> model.fit((X1,X2)).score((X1,X2))
    array([0.99998761])
    """

    def __init__(
        self,
        latent_dims: int = 1,
        scale: bool = True,
        centre=True,
        copy_data=True,
        random_state=None,
        deflation="cca",
        c: Union[Iterable[float], float] = None,
        max_iter: int = 100,
        maxvar: bool = False,
        initialization: Union[str, callable] = "pls",
        tol: float = 1e-9,
        stochastic=False,
        positive: Union[Iterable[bool], bool] = None,
    ):
        """
        Constructor for SCCA

        :param latent_dims: number of latent dimensions to fit
        :param scale: normalize variance in each column before fitting
        :param centre: demean data by column before fitting (and before transforming out of sample
        :param copy_data: If True, X will be copied; else, it may be overwritten
        :param random_state: Pass for reproducible output across multiple function calls
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param maxvar: use auxiliary variable "maxvar" form
        :param initialization: either string from "pls", "cca", "random", "uniform" or callable to initialize the score variables for iterative methods
        :param tol: tolerance value used for early stopping
        :param c: lasso alpha
        :param stochastic: use stochastic regression optimisers for subproblems
        :param positive: constrain model weights to be positive
        """
        super().__init__(
            latent_dims=latent_dims,
            scale=scale,
            centre=centre,
            copy_data=copy_data,
            max_iter=max_iter,
            initialization=initialization,
            tol=tol,
            c=c,
            l1_ratio=1,
            maxvar=maxvar,
            stochastic=stochastic,
            positive=positive,
            random_state=random_state,
            deflation=deflation,
        )


class PMD(_Iterative):
    r"""
    Fits a Sparse CCA (Penalized Matrix Decomposition) model.

    :Maths:

    .. math::

        w_{opt}=\underset{w}{\mathrm{argmax}}\{ w_1^TX_1^TX_2w_2  \}\\

        \text{subject to:}

        w_i^Tw_i=1

        \|w_i\|<=c_i

    :Citation:

    Witten, Daniela M., Robert Tibshirani, and Trevor Hastie. "A penalized matrix decomposition, with applications to sparse principal components and canonical correlation analysis." Biostatistics 10.3 (2009): 515-534.

    :Example:

    >>> from cca_zoo.models import PMD
    >>> import numpy as np
    >>> rng=np.random.RandomState(0)
    >>> X1 = rng.random((10,5))
    >>> X2 = rng.random((10,5))
    >>> model = PMD(c=[1,1],random_state=0)
    >>> model.fit((X1,X2)).score((X1,X2))
    array([0.81796873])
    """

    def __init__(
        self,
        latent_dims: int = 1,
        scale: bool = True,
        centre=True,
        copy_data=True,
        random_state=None,
        deflation="cca",
        c: Union[Iterable[float], float] = None,
        max_iter: int = 100,
        initialization: Union[str, callable] = "pls",
        tol: float = 1e-9,
        positive: Union[Iterable[bool], bool] = None,
    ):
        """
        Constructor for PMD

        :param latent_dims: number of latent dimensions to fit
        :param scale: normalize variance in each column before fitting
        :param centre: demean data by column before fitting (and before transforming out of sample
        :param copy_data: If True, X will be copied; else, it may be overwritten
        :param random_state: Pass for reproducible output across multiple function calls
        :param c: l1 regularisation parameter between 1 and sqrt(number of features) for each view
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param initialization: either string from "pls", "cca", "random", "uniform" or callable to initialize the score variables for iterative methods
        :param tol: tolerance value used for early stopping
        :param positive: constrain model weights to be positive
        """
        self.c = c
        self.positive = positive
        super().__init__(
            latent_dims=latent_dims,
            scale=scale,
            centre=centre,
            copy_data=copy_data,
            max_iter=max_iter,
            initialization=initialization,
            tol=tol,
            random_state=random_state,
            deflation=deflation,
        )

    def _set_loop_params(self):
        self.loop = _PMDInnerLoop(
            max_iter=self.max_iter,
            c=self.c,
            tol=self.tol,
            positive=self.positive,
            random_state=self.random_state,
        )


class ParkhomenkoCCA(_Iterative):
    r"""
    Fits a sparse CCA (penalized CCA) model

    .. math::

        w_{opt}=\underset{w}{\mathrm{argmax}}\{ w_1^TX_1^TX_2w_2  \} + c_i\|w_i\|\\

        \text{subject to:}

        w_i^Tw_i=1

    :Citation:

    Parkhomenko, Elena, David Tritchler, and Joseph Beyene. "Sparse canonical correlation analysis with application to genomic data integration." Statistical applications in genetics and molecular biology 8.1 (2009).

    :Example:

    >>> from cca_zoo.models import ParkhomenkoCCA
    >>> import numpy as np
    >>> rng=np.random.RandomState(0)
    >>> X1 = rng.random((10,5))
    >>> X2 = rng.random((10,5))
    >>> model = ParkhomenkoCCA(c=[0.001,0.001],random_state=0)
    >>> model.fit((X1,X2)).score((X1,X2))
    array([0.81803527])
    """

    def __init__(
        self,
        latent_dims: int = 1,
        scale: bool = True,
        centre=True,
        copy_data=True,
        random_state=None,
        deflation="cca",
        c: Union[Iterable[float], float] = None,
        max_iter: int = 100,
        initialization: Union[str, callable] = "pls",
        tol: float = 1e-9,
    ):
        """
        Constructor for ParkhomenkoCCA

        :param latent_dims: number of latent dimensions to fit
        :param scale: normalize variance in each column before fitting
        :param centre: demean data by column before fitting (and before transforming out of sample
        :param copy_data: If True, X will be copied; else, it may be overwritten
        :param random_state: Pass for reproducible output across multiple function calls
        :param c: l1 regularisation parameter
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param initialization: either string from "pls", "cca", "random", "uniform" or callable to initialize the score variables for iterative methods
        :param tol: tolerance value used for early stopping
        """
        self.c = c
        super().__init__(
            latent_dims=latent_dims,
            scale=scale,
            centre=centre,
            copy_data=copy_data,
            max_iter=max_iter,
            initialization=initialization,
            tol=tol,
            random_state=random_state,
            deflation=deflation,
        )

    def _set_loop_params(self):
        self.loop = _ParkhomenkoInnerLoop(
            max_iter=self.max_iter,
            c=self.c,
            tol=self.tol,
            random_state=self.random_state,
        )


class SCCA_ADMM(_Iterative):
    r"""
    Fits a sparse CCA model by alternating ADMM

    .. math::

        w_{opt}=\underset{w}{\mathrm{argmax}}\{\sum_i\sum_{j\neq i} \|X_iw_i-X_jw_j\|^2 + \text{l1_ratio}\|w_i\|_1\}\\

        \text{subject to:}

        w_i^TX_i^TX_iw_i=1

    :Citation:

    Suo, Xiaotong, et al. "Sparse canonical correlation analysis." arXiv preprint arXiv:1705.10865 (2017).

    :Example:

    >>> from cca_zoo.models import SCCA_ADMM
    >>> import numpy as np
    >>> rng=np.random.RandomState(0)
    >>> X1 = rng.random((10,5))
    >>> X2 = rng.random((10,5))
    >>> model = SCCA_ADMM(random_state=0,c=[1e-1,1e-1])
    >>> model.fit((X1,X2)).score((X1,X2))
    array([0.84348183])
    """

    def __init__(
        self,
        latent_dims: int = 1,
        scale: bool = True,
        centre=True,
        copy_data=True,
        random_state=None,
        deflation="cca",
        c: Union[Iterable[float], float] = None,
        mu: Union[Iterable[float], float] = None,
        lam: Union[Iterable[float], float] = None,
        eta: Union[Iterable[float], float] = None,
        max_iter: int = 100,
        initialization: Union[str, callable] = "pls",
        tol: float = 1e-9,
    ):
        """
        Constructor for SCCA_ADMM

        :param latent_dims: number of latent dimensions to fit
        :param scale: normalize variance in each column before fitting
        :param centre: demean data by column before fitting (and before transforming out of sample
        :param copy_data: If True, X will be copied; else, it may be overwritten
        :param random_state: Pass for reproducible output across multiple function calls
        :param c: l1 regularisation parameter
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param initialization: either string from "pls", "cca", "random", "uniform" or callable to initialize the score variables for iterative methods
        :param tol: tolerance value used for early stopping
        :param mu:
        :param lam:
        :param: eta:
        """
        self.c = c
        self.mu = mu
        self.lam = lam
        self.eta = eta
        super().__init__(
            latent_dims=latent_dims,
            scale=scale,
            centre=centre,
            copy_data=copy_data,
            max_iter=max_iter,
            initialization=initialization,
            tol=tol,
            random_state=random_state,
            deflation=deflation,
        )

    def _set_loop_params(self):
        self.loop = _ADMMInnerLoop(
            max_iter=self.max_iter,
            c=self.c,
            mu=self.mu,
            lam=self.lam,
            eta=self.eta,
            tol=self.tol,
            random_state=self.random_state,
        )


class SpanCCA(_Iterative):
    r"""
    Fits a Sparse CCA model using SpanCCA.

    .. math::

        w_{opt}=\underset{w}{\mathrm{argmax}}\{\sum_i\sum_{j\neq i} \|X_iw_i-X_jw_j\|^2 + \text{l1_ratio}\|w_i\|_1\}\\

        \text{subject to:}

        w_i^TX_i^TX_iw_i=1

    :Citation:

    Asteris, Megasthenis, et al. "A simple and provable algorithm for sparse diagonal CCA." International Conference on Machine Learning. PMLR, 2016.


    :Example:

    >>> from cca_zoo.models import SpanCCA
    >>> import numpy as np
    >>> rng=np.random.RandomState(0)
    >>> X1 = rng.random((10,5))
    >>> X2 = rng.random((10,5))
    >>> model = SpanCCA(regularisation="l0", c=[2, 2])
    >>> model.fit((X1,X2)).score((X1,X2))
    array([0.84556666])
    """

    def __init__(
        self,
        latent_dims: int = 1,
        scale: bool = True,
        centre=True,
        copy_data=True,
        max_iter: int = 100,
        initialization: str = "uniform",
        tol: float = 1e-9,
        regularisation="l0",
        c: Union[Iterable[Union[float, int]], Union[float, int]] = None,
        rank=1,
        positive: Union[Iterable[bool], bool] = None,
        random_state=None,
        deflation="cca",
    ):
        """

        :param latent_dims: number of latent dimensions to fit
        :param scale: normalize variance in each column before fitting
        :param centre: demean data by column before fitting (and before transforming out of sample
        :param copy_data: If True, X will be copied; else, it may be overwritten
        :param random_state: Pass for reproducible output across multiple function calls
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param initialization: either string from "pls", "cca", "random", "uniform" or callable to initialize the score variables for iterative methods
        :param tol: tolerance value used for early stopping
        :param regularisation:
        :param c: regularisation parameter
        :param rank: rank of the approximation
        :param positive: constrain weights to be positive
        """
        super().__init__(
            latent_dims=latent_dims,
            scale=scale,
            centre=centre,
            copy_data=copy_data,
            max_iter=max_iter,
            initialization=initialization,
            tol=tol,
            random_state=random_state,
            deflation=deflation,
        )
        self.c = c
        self.regularisation = regularisation
        self.rank = rank
        self.positive = positive

    def _set_loop_params(self):
        self.loop = _SpanCCAInnerLoop(
            max_iter=self.max_iter,
            c=self.c,
            tol=self.tol,
            regularisation=self.regularisation,
            rank=self.rank,
            random_state=self.random_state,
            positive=self.positive,
        )


class SWCCA(_Iterative):
    r"""
    A class used to fit SWCCA model

    :Citation:

    .. Wenwen, M. I. N., L. I. U. Juan, and Shihua Zhang. "Sparse Weighted Canonical Correlation Analysis." Chinese Journal of Electronics 27.3 (2018): 459-466.

    :Example:

    >>> from cca_zoo.models import SWCCA
    >>> import numpy as np
    >>> rng=np.random.RandomState(0)
    >>> X1 = rng.random((10,5))
    >>> X2 = rng.random((10,5))
    >>> model = SWCCA(regularisation='l0',c=[2, 2], sample_support=5, random_state=0)
    >>> model.fit((X1,X2)).score((X1,X2))
    array([0.61620969])
    """

    def __init__(
        self,
        latent_dims: int = 1,
        scale: bool = True,
        centre=True,
        copy_data=True,
        random_state=None,
        max_iter: int = 500,
        initialization: str = "uniform",
        tol: float = 1e-9,
        regularisation="l0",
        c: Union[Iterable[Union[float, int]], Union[float, int]] = None,
        sample_support=None,
        positive=False,
    ):
        """

        :param latent_dims: number of latent dimensions to fit
        :param scale: normalize variance in each column before fitting
        :param centre: demean data by column before fitting (and before transforming out of sample
        :param copy_data: If True, X will be copied; else, it may be overwritten
        :param random_state: Pass for reproducible output across multiple function calls
        :param max_iter: the maximum number of iterations to perform in the inner optimization loop
        :param initialization: either string from "pls", "cca", "random", "uniform" or callable to initialize the score variables for iterative methods
        :param tol: tolerance value used for early stopping
        :param regularisation: the type of regularisation on the weights either 'l0' or 'l1'
        :param c: regularisation parameter
        :param sample_support: the l0 norm of the sample weights
        :param positive: constrain weights to be positive
        """

        self.c = c
        self.sample_support = sample_support
        self.regularisation = regularisation
        self.positive = positive
        super().__init__(
            latent_dims=latent_dims,
            scale=scale,
            centre=centre,
            copy_data=copy_data,
            max_iter=max_iter,
            initialization=initialization,
            tol=tol,
            random_state=random_state,
        )

    def _set_loop_params(self):
        self.loop = _SWCCAInnerLoop(
            max_iter=self.max_iter,
            tol=self.tol,
            regularisation=self.regularisation,
            c=self.c,
            sample_support=self.sample_support,
            random_state=self.random_state,
            positive=self.positive,
        )
