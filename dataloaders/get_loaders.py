#collate_fn에서 time을 반환하도록 수정할 필요가 있음

from torch.utils.data import DataLoader, random_split
from utils import collate_fn
from dataloaders.dataloader import Answerloader

def get_loaders(config):

    dataset = Answerloader()

    num_q = dataset.num_q

    train_size = int( len(dataset) * config.train_ratio )
    test_size = len(dataset) - train_size

    train_dataset, test_dataset = random_split(
        dataset, [ train_size, test_size ]
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size = config.batch_size,
        shuffle = True,
        collate_fn = collate_fn
    )
    test_loader = DataLoader(
        test_dataset,
        batch_size = config.batch_size,
        shuffle = True,
        collate_fn = collate_fn
    )

    return train_loader, test_loader, num_q