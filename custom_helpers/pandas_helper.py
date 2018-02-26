import pandas as pd


def insert_article_to_pandas(df, article):
    current_columns = []

    current_columns.append('JOURNAL')

    for key_word in article.ordered_keys:
        current_columns.append(key_word)

    df_1 = pd.DataFrame(columns=current_columns)
    frames = [df, df_1]
    df = pd.concat(frames)

    df.loc[article.doi, 'JOURNAL'] = article.journal.title

    for key_word in article.ordered_keys:
        for column in df:
            if column == key_word:
                df.loc[article.doi, key_word] = 1

    return df
