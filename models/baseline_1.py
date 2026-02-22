import torch.nn as nn
import torchvision.models as models


class ImageClassification(nn.Module):
    """
    Image Classification model using a ResNet-50 backbone.

    Args:
        num_classes (int): Number of output classes.
        pretrained (bool): Whether to use ImageNet pretrained weights.
    """

    def __init__(self, num_classes: int = 10, pretrained: bool = True):
        super().__init__()
        
        weights = models.ResNet50_Weights.DEFAULT if pretrained else None
        self.backbone = models.resnet50(weights=weights)

        in_features = self.backbone.fc.in_features
        self.backbone.fc = nn.Linear(in_features, num_classes)

    def forward(self, x):
        """
        Forward pass.

        Args:
            x (Tensor): Input tensor of shape (B, C, H, W)

        Returns:
            Tensor: Logits of shape (B, num_classes)
        """
        return self.backbone(x)