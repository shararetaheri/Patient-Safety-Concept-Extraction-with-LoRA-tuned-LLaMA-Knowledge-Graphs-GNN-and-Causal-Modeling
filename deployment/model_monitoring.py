import numpy as np

class DriftDetector:

    def population_stability_index(self, expected, actual, bins=10):
        expected_perc, _ = np.histogram(expected, bins=bins)
        actual_perc, _ = np.histogram(actual, bins=bins)

        expected_perc = expected_perc / len(expected)
        actual_perc = actual_perc / len(actual)

        psi = np.sum(
            (actual_perc - expected_perc) *
            np.log((actual_perc + 1e-6) / (expected_perc + 1e-6))
        )
        return psi
