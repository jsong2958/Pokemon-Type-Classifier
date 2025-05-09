import torch
import torch.nn as nn
import torch.nn.functional as F

class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 5)
        self.conv2 = nn.Conv2d(16, 32, 5)
        self.conv3 = nn.Conv2d(32, 64, 5)
        self.conv4 = nn.Conv2d(64, 128, 5)
        self.conv5 = nn.Conv2d(128, 256, 5)
        self.conv6 = nn.Conv2d(256, 512, 5)

        self.fc1 = nn.Linear(512 * 25 * 25, 512)
        self.fc2 = nn.Linear(512, 128)
        self.fc3 = nn.Linear(128, 18) # 18 Types including None

    def forward(self, input):
        c1 = F.relu(self.conv1(input)) # Takes in input image tensor, outputs tensor with size (N, 16, 252, 252), where N = batch_size (4)
        c2 = F.relu(self.conv2(c1)) # Tensor (N, 16, 252, 252) -> Tensor (N, 32, 248, 248)
        p1 = F.max_pool2d(c2, (2,2)) # Tensor (N, 32, 248, 248) -> Tensor (N, 32, 124, 124)
        c3 = F.relu(self.conv3(p1)) # Tensor (N, 32, 124, 124) -> Tensor (N, 64, 120, 120)
        c4 = F.relu(self.conv4(c3)) # Tensor (N, 64, 120, 120) -> Tensor (N, 128, 116, 116)
        p2 = F.max_pool2d(c4, (2,2)) # Tensor (N, 128, 116, 116) -> Tensor (N, 128, 58, 58)
        c5 = F.relu(self.conv5(p2)) # Tensor (N, 128, 58, 58) -> Tensor (N, 256, 54, 54)
        c6 = F.relu(self.conv6(c5)) # Tensor (N, 256, 54, 54) -> Tensor (N, 512, 50, 50)
        p3 = F.max_pool2d(c6, (2,2)) # Tensor (N, 512, 50, 50) -> Tensor (N, 512, 25, 25)

        flat = torch.flatten(p3, 1) # Tensor (N, 512, 25, 25) -> Tensor (N, 512 * 25 * 25)
        f1 = self.fc1(flat)
        f2 = self.fc2(f1)
        out = self.fc3(f2)

        return out
    
types = {
        "Normal": 0,
        "Fire": 1,
        "Water": 2,
        "Electric": 3,
        "Grass": 4,
        "Ice": 5,
        "Fighting": 6,
        "Poison": 7,
        "Ground": 8,
        "Flying": 9,
        "Psychic": 10,
        "Bug": 11,
        "Rock": 12,
        "Ghost": 13,
        "Dragon": 14,
        "Dark": 15,
        "Steel": 16,
        "Fairy": 17
    }

types_inverse = {v: k for k, v in types.items()}