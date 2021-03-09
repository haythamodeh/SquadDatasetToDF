import json
import pandas as pd


def json_to_df(json_file):
    arrayForDF = []
    for current_subject in json_file['data']:
        subject = current_subject['title']
        for current_context in current_subject['paragraphs']:
            context = current_context['context']
            for current_question in current_context['qas']:
                question = current_question['question']
                if (len(question) > 2):
                    is_impossible = current_question['is_impossible']
                    if(is_impossible == False):
                        for answer in current_question['answers']:
                            answer_text = answer['text']
                            answer_start = answer['answer_start']

                            record = {
                                "answer_text": answer_text,
                                "answer_start": answer_start,
                                "question": question,
                                "context": context,
                                "subject": subject
                            }
                            arrayForDF.append(record)
    df = pd.DataFrame(arrayForDF)
    return df


json_file = open("Data/train-v2.0.json",)
data = json.load(json_file)
train_df = json_to_df(data)
print(train_df.shape)
# print(train_df.head())
