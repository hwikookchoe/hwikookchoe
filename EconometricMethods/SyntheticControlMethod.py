import numpy as np
import pandas as pd
from scipy.optimize import minimize
from sklearn.base import BaseEstimator, TransformerMixin


class SyntheticControl(BaseEstimator, TransformerMixin):
    '''
    Reference:
        Abadie, Alberto.
        "Using synthetic controls: Feasibility, data requirements, and methodological aspects."
        Journal of Economic Literature 59, no. 2 (2021): 391-425.

    Currently, I did not made optimizing the weight for covariates, nu.
    I only made equal weights, nu_1 = ... = nu_k = 1/k

    I used sklearn.base.BaseEstimator, so this class could be incorporated into pipeline.
    '''
    def __init__(
        self,
        treatment_time_index,
        extrapolation=False,
    ):
        self.treatment_time_index = treatment_time_index
        self.extrapolation = extrapolation
        self.weight = None

    @staticmethod
    def _loss_omega(W, X, y):
        return np.sqrt(np.mean((y - X.dot(W)) ** 2))

    def fit(self, X, y=None):
        pretreat_X = X[:self.treatment_time_index, :]
        pretreat_y = y[:self.treatment_time_index]
        omega_start = [1/X.shape[1]]*X.shape[1]

        if self.extrapolation:
            return_result = minimize(
                fun=self._loss_omega,
                x0=np.array(omega_start),
                args=(pretreat_X, pretreat_y),
                constraints={'type':'eq', 'fun':lambda x: np.sum(x) - 1},
            )
        else:
            return_result = minimize(
                fun=self._loss_omega,
                x0=np.array(omega_start),
                args=(pretreat_X, pretreat_y),
                constraints={'type':'eq', 'fun':lambda x: np.sum(x) - 1},
                bounds=[(0.0, 1.0)]*len(omega_start),
            )

        if return_result.status == 0:
            self.weight = np.around(return_result.x, 3)
        else:
            raise ValueError('Scipy.Optimize.Minimize failed to find solution.')

        return self

    def transform(self, X, y=None):
        return X @ self.weight
