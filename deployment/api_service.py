from fastapi import FastAPI
import torch

app = FastAPI()

@app.post("/predict")
def predict(data: dict):
    # Load model
    model = torch.load("temporal_gnn.pt")
    output = model(data["x"], data["edge_index"], data["time_series"])
    return {"risk_score": float(output.detach().numpy())}
