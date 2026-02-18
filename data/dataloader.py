# The DataLoader class is responsible for:
#   1- Batching samples into mini-batches
#   2- Shuffling the dataset
#   3- Parallel loading using multiple workers
#   4- Creating an iterable over the dataset
#   5- Collating samples into tensors

from torch.utils.data import DataLoader, WeightedRandomSampler
from typing import List, Dict, Optional, Any

STATUS = {"train", "test", "val"}

def build_dataloader(dataset, status: str,config):
    if status not in STATUS:
        raise ValueError(
            "Invalid status {status}. Supported statas {STATUS}"
        )
    if status == "train":
        dataloader = DataLoader(
            dataset,
            config.TRAIN.BATCH_SIZE, 
            config.TRAIN.SHUFFLE,
            
        )
    
    return dataloader


def collate_fun(batch):
    return None

def get_sampler():
    #sampler = WeightedRandomSampler(weights, num_samples)
    pass