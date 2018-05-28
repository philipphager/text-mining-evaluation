import pandas as pd


def print_topic_df(model, topic_id, topn=20):
    d = model.print_topic(topic_id, topn).replace('"', '').split('+')
    d = [el.split('*') for el in d]
    df = pd.DataFrame(d, columns=['prob', 'word'])
    return df
