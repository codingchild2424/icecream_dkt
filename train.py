import torch

from dataloaders.get_loaders import get_loaders
from define_argparser import define_argparser


def main(config):
    device = torch.device('cpu') if config.gpu_id < 0 else torch.device('cuda:%d' % config.gpu_id)

    #1. 데이터 받아오기
    train_loader, test_loader, num_q = get_loaders(config)


if __name__ == "__main__":
    config = define_argparser()
    main(config)