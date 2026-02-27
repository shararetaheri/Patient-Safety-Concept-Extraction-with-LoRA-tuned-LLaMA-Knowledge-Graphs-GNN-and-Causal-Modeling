import numpy as np

class ATEEstimator:

    def estimate_ate(self, outcome, treatment, propensity):

        treated = treatment == 1
        control = treatment == 0

        weight_treated = 1 / propensity[treated]
        weight_control = 1 / (1 - propensity[control])

        ate = (
            np.mean(outcome[treated] * weight_treated) -
            np.mean(outcome[control] * weight_control)
        )

        return ate
