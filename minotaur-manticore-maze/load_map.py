import pandas as pd


class LoadMap():

    def __init__(self, map_csv):
        self.map_csv = map_csv
        self.df = pd.read_csv(map_csv, header=None)
