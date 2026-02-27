causal_effect = self.causal_pipeline.run(
    X_features,
    treatment_vector,
    outcome_vector
)

gnn_risk = self.gnn_model(node_embeddings)

return {
    ...
    "causal_effect": causal_effect,
    "gnn_risk": gnn_risk.item()
}
