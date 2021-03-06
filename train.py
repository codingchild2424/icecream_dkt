import torch

from dataloaders.get_loaders import get_loaders
from define_argparser import define_argparser
from models.get_models import get_models
from utils import get_optimizers, get_crits
from trainers.get_trainers import get_trainers


def main(config):
    device = torch.device('cpu') if config.gpu_id < 0 else torch.device('cuda:%d' % config.gpu_id)

    #1. 데이터 받아오기
    train_loader, test_loader, num_q = get_loaders(config)

    #2. model 선택
    model = get_models(num_q, device, config)

    #3. optimizer 선택
    optimizer = get_optimizers(model, config)
    
    #4. criterion 선택
    crit = get_crits(config)

    #5. trainer 선택
    trainer = get_trainers(model, optimizer, device, num_q, crit, config)

    #6. 훈련 및 score 계산
    y_true_record, y_score_record, highest_auc_score = trainer.train(train_loader, test_loader)

    #7. model 기록 저장 위치
    model_path = './train_model_records/' + config.model_name + \
         '_' + str(round(highest_auc_score, 4)) + '_' + config.model_fn

    #8. model 기록
    torch.save({
        'model': trainer.model.state_dict(),
        'config': config
    }, model_path)

if __name__ == "__main__":
    config = define_argparser()
    main(config)