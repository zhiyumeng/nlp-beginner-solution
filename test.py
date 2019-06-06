import config as cfg
import pandas as pd
from os.path import join

DATA_DIR = cfg.DATA_PATH


def load_tsv():
    train_df = pd.read_csv(join(DATA_DIR, 'train.tsv'), delimiter='\t')
    test_df = pd.read_csv(join(DATA_DIR, 'test.tsv'), delimiter='\t')
    return train_df, test_df

if __name__ == '__main__':
    train_df, test_df = load_tsv()
    print(train_df.columns)
    print(train_df.head())