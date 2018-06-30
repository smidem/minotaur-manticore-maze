from tqdm import tqdm
from time import sleep


class Progress():

    def __init__(self, secs, prefix):
        self.secs = secs
        self.prefix = prefix

    def bar(self):
        with tqdm(total=100,
                  ncols=65,
                  bar_format='{l_bar}{bar}|',
                  desc=self.prefix) as pbar:
            for i in range(100):
                pbar.update(1)
                sleep(self.secs)
