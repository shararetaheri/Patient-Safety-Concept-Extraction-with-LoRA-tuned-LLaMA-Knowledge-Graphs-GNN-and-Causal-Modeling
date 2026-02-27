import torch
import torch.nn as nn
import torch.nn.functional as F

class TemporalGNN(nn.Module):

    def __init__(self, in_dim, hidden_dim):
        super().__init__()

        self.linear1 = nn.Linear(in_dim, hidden_dim)
        self.attention = nn.MultiheadAttention(
            hidden_dim,
            num_heads=4,
            batch_first=True
        )
        self.linear2 = nn.Linear(hidden_dim, 1)

    def forward(self, node_embeddings):

        h = F.relu(self.linear1(node_embeddings))

        attn_output, _ = self.attention(
            h, h, h
        )

        out = self.linear2(attn_output[:, -1, :])
        return torch.sigmoid(out)
