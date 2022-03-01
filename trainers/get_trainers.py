from trainers.time_dkt_trainer import Time_DKT_trainer
from trainers.basic_dkt_trainer import Basic_DKT_trainer

def get_trainers(model, optimizer, device, num_q, crit, config):

    #trainer 실행
    if config.model_name == "time_dkt":
        trainer = Time_DKT_trainer(
            model = model,
            optimizer = optimizer,
            n_epochs = config.n_epochs,
            device = device,
            num_q = num_q,
            crit = crit
        )
    elif config.model_name == "basic_dkt":
        trainer = Basic_DKT_trainer(
            model = model,
            optimizer = optimizer,
            n_epochs = config.n_epochs,
            device = device,
            num_q = num_q,
            crit = crit
        )
    #ignite 테스트용

    return trainer
