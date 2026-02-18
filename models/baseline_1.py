
import torch 
from torch import nn
from torchvision import models


class ImageClassification(nn.Module):
    def __init__(self):
        super().__init__()
        
        
    def forward (self, inp):
        pass 
    
m = models.alexnet(pretrained=True)
print(m)