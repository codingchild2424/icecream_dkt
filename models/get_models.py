from models.time_dkt import Time_DKT
from models.basic_dkt import Basic_DKT

def get_models(num_q, device, config):

    if config.model_name == "time_dkt":
        model = Time_DKT(
            num_q = num_q,
            emb_size = config.dkt_emb_size,
            hidden_size = config.dkt_hidden_size
        ).to(device)
    elif config.model_name == "basic_dkt":
        model = Basic_DKT(
            num_q = num_q,
            emb_size = config.dkt_emb_size,
            hidden_size = config.dkt_hidden_size
        ).to(device)
    #-> 추가적인 모델 정의
    else:
        print("Wrong model_name was used...")

    return model