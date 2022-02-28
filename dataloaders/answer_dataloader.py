#datasets에 있는 answer_data를 불러오는 코드

from torch.utils.data import Dataset

import pandas as pd
import numpy as np

DATASET_DIR = "../datasets/answer_data.csv"

class Answerloader(Dataset):
    def __init__(self, dataset_dir = DATASET_DIR):
        super().__init__()

        self.dataset_dir = dataset_dir

        #preprocess틀 통해 인스턴트 불러오기
        self.q_seqs, self.r_seqs, self.t_seqs, \
            self.metas, self.u2idx, self.q2idx, \
                self.u_list, self.q_list = self.preprocess()
        """
        self.q_seqs: question sequences
        self.r_seqs: response sequneces
        self.t_seqs: timestamp sequences
        self.metas: user meta data
        self.u2idx: user to index
        self.q2idx: question to index
        self.u_list: unique user list
        self.q_list: unique question list
        """

        self.len = len(self.q_seqs)

    def __getitem__(self, index):
        return self.q_seqs[index], self.r_seqs[index], self.t_seqs[index]

    def __len__(self):
        return self.len

    #여기서 데이터 전처리하기
    def preprocess(self):
        df = pd.read_csv(self.dataset_dir) #필요시 encoding
        #정답값이 0과 1인 것으로 전처리하기
        df = df[ (df["answer"] == 0).values + (df["answer"] == 1).values ]

        #시간을 datetime으로 변환
        df["timestamp"] = pd.to_datetime(df["timestamp"]) #https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wideeyed&logNo=221603462366
        
        #일단 모든 column을 대상으로 unique값과 sequence 값을 만들기
        u_list = np.unique( df["user_ID"].values ) #user ID
        q_list = np.unique( df["item_ID"].values ) #평가문항 ID

        #딕셔너리
        u2idx = { u:idx for idx, u in enumerate(u_list) }
        q2idx = { q:idx for idx, q in enumerate(q_list) }

        #user별 sequence 데이터 만들기
        #user_ID 별로, item_ID와 answer, 그리고 timestamp를 담기
        q_seqs = [] #question sequences
        r_seqs = [] #response sequences
        t_seqs = [] #timestamps

        metas = []

        for u in u_list:
            df_u = df[df["user_ID"] == u].sort_values("timestamp") #datetime으로 변경했기에 sort_values 사용 가능
            
            q_seq = np.array([q2idx[q] for q in df_u["item_ID"].values])
            r_seq = df_u["answer"].values
            t_seq = df_u["timestamp"].values

            q_seqs.append(q_seq)
            r_seqs.append(r_seq)
            t_seqs.append(t_seq)

            #user별 메타데이터 정리(sex, level, grade)
            meta = {}
            
            meta["user"] = u2idx[u]
            meta["sex"] = df_u["sex"].values[0]
            meta["level"] = df_u["level"].values[0]
            meta["grade"] = df_u["grade"].values[0]

            metas.append(meta)

        return q_seqs, r_seqs, t_seqs, metas, u2idx, q2idx, u_list, q_list



    