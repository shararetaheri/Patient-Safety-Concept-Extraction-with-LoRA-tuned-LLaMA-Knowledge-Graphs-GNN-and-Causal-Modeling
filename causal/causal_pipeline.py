class CausalPipeline:

    def __init__(self, propensity_model, ate_estimator):
        self.propensity = propensity_model
        self.ate = ate_estimator

    def run(self, X, treatment, outcome):

        self.propensity.fit(X, treatment)
        ps = self.propensity.compute_scores(X)

        ate_value = self.ate.estimate_ate(
            outcome,
            treatment,
            ps
        )

        return ate_value
