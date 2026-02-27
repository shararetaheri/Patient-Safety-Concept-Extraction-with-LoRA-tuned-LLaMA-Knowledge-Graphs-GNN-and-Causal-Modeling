import numpy as np
from sklearn.metrics import roc_auc_score
from scipy import stats
from statsmodels.stats.contingency_tables import mcnemar

class StatisticalEvaluator:

    def bootstrap_ci(self, y_true, y_pred, metric_fn, n_bootstrap=1000):
        scores = []
        n = len(y_true)

        for _ in range(n_bootstrap):
            idx = np.random.choice(n, n, replace=True)
            score = metric_fn(y_true[idx], y_pred[idx])
            scores.append(score)

        lower = np.percentile(scores, 2.5)
        upper = np.percentile(scores, 97.5)
        return np.mean(scores), (lower, upper)

    def mcnemar_test(self, y_true, pred1, pred2):
        table = [[0, 0], [0, 0]]
        for i in range(len(y_true)):
            correct1 = pred1[i] == y_true[i]
            correct2 = pred2[i] == y_true[i]
            table[int(correct1)][int(correct2)] += 1

        result = mcnemar(table, exact=True)
        return result.pvalue

    def delong_test(self, y_true, prob1, prob2):
        auc1 = roc_auc_score(y_true, prob1)
        auc2 = roc_auc_score(y_true, prob2)
        z = (auc1 - auc2) / np.std(prob1 - prob2)
        p = 2 * (1 - stats.norm.cdf(abs(z)))
        return p

    def cohens_d(self, group1, group2):
        diff = np.mean(group1) - np.mean(group2)
        pooled_std = np.sqrt(
            (np.std(group1) ** 2 + np.std(group2) ** 2) / 2
        )
        return diff / pooled_std
