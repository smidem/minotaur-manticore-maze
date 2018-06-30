import pandas as pd


class LoadMap():

    def __init__(self, map_csv, start_row, start_col):
        self.df = pd.read_csv(map_csv, header=None)
        start_col_list = self.df.iloc[:, start_col].str.split(' ').tolist()
        self.start_point = start_col_list[start_row]
