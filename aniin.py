import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(2, 2)  # Fully connected layer with input size 2 and output size 2

    def forward(self, x):
        x = self.fc1(x)  # Pass the input through the fully connected layer
        return x
