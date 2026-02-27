import numpy as np
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score,
    brier_score_loss
)

class EvaluationFramework:

    def ner_metrics(self, y_true, y_pred):
        return {
            "precision": precision_score(y_true, y_pred, average="micro"),
            "recall": recall_score(y_true, y_pred, average="micro"),
            "f1_micro": f1_score(y_true, y_pred, average="micro"),
            "f1_macro": f1_score(y_true, y_pred, average="macro")
        }

    def temporal_metrics(self, y_true, y_prob):
        return {
            "AUROC": roc_auc_score(y_true, y_prob),
            "AUPRC": average_precision_score(y_true, y_prob),
            "Brier": brier_score_loss(y_true, y_prob)
        }
