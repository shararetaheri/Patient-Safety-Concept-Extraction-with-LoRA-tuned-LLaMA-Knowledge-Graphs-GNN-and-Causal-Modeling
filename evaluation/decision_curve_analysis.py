import numpy as np

class DecisionCurve:

    def net_benefit(self, y_true, y_prob, threshold):
        tp = np.sum((y_prob >= threshold) & (y_true == 1))
        fp = np.sum((y_prob >= threshold) & (y_true == 0))
        n = len(y_true)

        return (tp / n) - (fp / n) * (threshold / (1 - threshold))
