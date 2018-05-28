import pandas as pd


def print_author_topics(model, author_id):
    df = pd.DataFrame(model[author_id], columns=['Topic', 'Value'])
    df = df.sort_values(by='Value', ascending=False)
    return df.set_index('Topic')


def print_topic(model, topic_id, topn=20):
    d = model.print_topic(topic_id, topn).replace('"', '').split('+')
    d = [el.split('*') for el in d]
    df = pd.DataFrame(d, columns=['prob', 'word'])
    return df.set_index('word')
