import torch
import torch.nn as nn
import torch.nn.functional as F

class FeatureDQN(nn.Module):
    """DQN Model having features as input (not raw image)."""
    def __init__(self, state_size, action_size, seed, neurons_1 = 64, neurons_2 = 64):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            neurons_1 (int): number of neurons for the 1rst hidden layer
            neurons_2 (int): number of neurons for the 2rst hidden layer
        """
        super(FeatureDQN, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, neurons_1)
        self.fc2 = nn.Linear(neurons_1, neurons_2)
        self.fc3 = nn.Linear(neurons_2, action_size)
        
    def forward(self, x):
        """Runs the DQN to estimate the action values."""
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.fc3(x)