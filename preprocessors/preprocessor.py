#여기서 json을 파씽해서 csv로 만들기

import json
import pandas as pd

def json_loader(data_path):
    with open(data_path, "r", encoding = "utf-8") as f:
        contents = f.read()
        json_data = json.loads(contents)

    return json_data

def json_parser_to_pd(json_data):

    ID_list = []
    sex_list = []# learnerProfile에서 추출
    level_list = []# learnerProfile에서 추출
    grade_list = []# learnerProfile에서 추출
    testID_list = []
    assessmentItemID_list = []
    answerCode_list = []
    Timestamp_list = []

    for json in json_data:

        ID_json = json['learnerID']
        sex_json = json['learnerProfile'].split(';')[0]
        level_json = json['learnerProfile'].split(';')[1]
        grade_json = json['learnerProfile'].split(';')[2]
        testID_json = json['testID']
        assessmentItemID_json = json['assessmentItemID']
        answerCode_json = json['answerCode']
        Timestamp_json = json['Timestamp']
        
        ID_list.append(ID_json)
        sex_list.append(sex_json)
        level_list.append(level_json)
        grade_list.append(grade_json)
        testID_list.append(testID_json)
        assessmentItemID_list.append(assessmentItemID_json)
        answerCode_list.append(answerCode_json)
        Timestamp_list.append(Timestamp_json)
        

    df_data = pd.DataFrame(
        {
            "user_ID" : ID_list,
            "sex" : sex_list,
            "level" : level_list,
            "grade" : grade_list,
            "test_ID" : testID_list,
            "item_ID" : assessmentItemID_list,
            "answer" : answerCode_list,
            "timestamp" : Timestamp_list,
        }
    )

    return df_data

#여기서 실행
answer_data_path = "../datasets/answer_data.json"
question_IRT_data_path = "../datasets/question_IRT.json"
user_IRT_data_path = "../datasets/user_IRT.json"

answer_json = json_loader(answer_data_path)
question_IRT_json = json_loader(question_IRT_data_path)
user_IRT_json = json_loader(user_IRT_data_path)

#여기서 사용할 것은 answer_json만 사용할 것임
#그래도 미리 파씽은 전부 해두기

answer_df = json_parser_to_pd(answer_json)
# question_IRT_df = json_parser_to_pd(question_IRT_json)
# user_IRT_df = json_parser_to_pd(user_IRT_json)

answer_df.to_csv("../datasets/answer_data.csv")
# question_IRT_df.to_csv("../datasets/question_IRT.csv")
# user_IRT_df.to_csv("../datasets/user_IRT.csv")