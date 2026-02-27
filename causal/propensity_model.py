from sklearn.linear_model import LogisticRegression
import numpy as np

class PropensityModel:

    def fit(self, X, treatment):
        self.model = LogisticRegression()
        self.model.fit(X, treatment)

    def compute_scores(self, X):
        return self.model.predict_proba(X)[:, 1]
