from trainers.dkt_trainer import DKT_trainer

def get_trainers(model, optimizer, device, num_q, crit, config):

    #trainer 실행
    trainer = DKT_trainer(
        model = model,
        optimizer = optimizer,
        n_epochs = config.n_epochs,
        device = device,
        num_q = num_q,
        crit = crit
    )
    #ignite 테스트용

    return trainer
