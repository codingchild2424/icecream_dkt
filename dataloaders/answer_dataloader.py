#datasets에 있는 answer_data를 불러오는 코드

from torch.utils.data import Dataset

import pandas as pd
import numpy as np

DATASET_DIR = "datasets/answer_data.csv"

class Answerloader(Dataset):
    def __init__(self, dataset_dir = DATASET_DIR):
        super().__init__()

        self.dataset_dir = dataset_dir

        #preprocess틀 통해 인스턴트 불러오기


    def __getitem__(self, index):
        pass

    def __len__(self):
        pass

    #여기서 데이터 전처리하기
    def preprocess(self):
        df = pd.read_csv(self.dataset_dir) #필요시 encoding
        #정답값이 0과 1인 것으로 전처리하기
        df = df[ (df["answer"] == 0).values + (df["answer"] == 1).values ]

        #index: user_ID, sex, level, grade, test_ID, item_ID, answer, timestamp
        #여기서 당장 필요한 것은 user_ID, item_ID, answer, timestamp
        
        #일단 모든 column을 대상으로 unique값과 sequence 값을 만들기
        u_list = np.unique( df["user_ID"].values ) #user ID
        s_list = np.unique( df["sex"].values ) #성별 M 아니면 F 밖에 없음
        l_list = np.unique( df["level"].values ) #학교급
        g_list = np.unique( df["grade"].values ) #학년
        t_list = np.unique( df["test_ID"].values ) #평가(시험) ID
        i_list = np.unique( df["item_ID"].values ) #평가문항 ID
        a_list = np.unique( df["answer"].values ) #문항 정오답 구분

        #timestamp는 Unique 값이 필요하지 않음

        #sex, level, grade는 모두 메타데이터임
        #메타데이터는 따로 user별로 메타데이터가 담긴 dictionary를 만드는게 좋아보임


        #user별 sequence 데이터 만들기
        #user_ID 순서로, item_ID와 answer, 그리고 timestamp를 담기
        u_seqs = []
        i_seqs = []
        a_seqs = []

        for u in u_list:
            df_u = df[df["user_ID"] == u]
        






    