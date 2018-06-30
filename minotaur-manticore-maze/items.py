from strings import ItemStrings
from progress import Progress


class Items():

    def __init__(self, current_loc):

        and_index = 0

        if any('and' in word for word in current_loc):
            and_index = current_loc.index('and')

        self.list = current_loc[:and_index]

    def encounter(self):

        brushing = Progress(.05, 'Brushing the dirt off')
        if 'compass' in self.list:
            print(ItemStrings().compass_part_1)
            brushing.bar()
            print(ItemStrings().compass_part_2)
