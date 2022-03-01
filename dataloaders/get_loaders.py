#collate_fn에서 time을 반환하도록 수정할 필요가 있음

from torch.utils.data import DataLoader, random_split
from utils import time_collate_fn, basic_collate_fn
from dataloaders.time_dataloader import Answerloader
from dataloaders.basic_dataloader import Basic_Answerloader

def get_loaders(config):

    #시간으로 실험
    if config.model_name == "time_dkt":
        dataset = Answerloader()
        collate_func = time_collate_fn
    elif config.model_name == "basic_dkt":
        dataset = Basic_Answerloader()
        collate_func = basic_collate_fn

    print("len(dataset): ", len(dataset))

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
        collate_fn = collate_func #함수로 변경
    )
    test_loader = DataLoader(
        test_dataset,
        batch_size = config.batch_size,
        shuffle = True,
        collate_fn = collate_func
    )

    return train_loader, test_loader, num_q