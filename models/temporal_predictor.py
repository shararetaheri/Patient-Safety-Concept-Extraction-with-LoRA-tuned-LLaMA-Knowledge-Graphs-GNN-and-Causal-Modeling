import torch
import torch.nn as nn

class TemporalSafetyPredictor(nn.Module):

    def __init__(self, dim):
        super().__init__()

        self.encoder = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(
                d_model=dim,
                nhead=4
            ),
            num_layers=2
        )

        self.classifier = nn.Linear(dim, 1)

    def forward(self, sequence):
        x = self.encoder(sequence)
        out = self.classifier(x[-1])
        return torch.sigmoid(out)
