class Bounds():

    def __init__(self, current_loc):
        self.bounds = []
        and_index = 0
        length = len(current_loc)

        for i, word in enumerate(current_loc):
            if 'and' in word:
                and_index = i

        if and_index > 0 and and_index + 1 < length:
            self.bounds = current_loc[and_index + 1: length]
        elif not and_index:
            self.bounds = current_loc

    def interpret(self):
        length = len(self.bounds)
        type = ''
        restricted = []

        if length > 1:
            type = self.bounds.pop(-1)

        if 'corner' in type or 'wall' in type:
            restricted = self.bounds
        elif 'hall' in type:
            if 'east' in self.bounds[0] and 'west' in self.bounds[1]:
                restricted = ['north', 'south']
            elif 'north' in self.bounds[0] and 'south' in self.bounds[1]:
                restricted = ['east', 'west']
        elif 'end' in type:
            if 'west' in self.bounds:
                restricted = ['north', 'south', 'east']
            elif 'east' in self.bounds:
                restricted = ['north', 'south', 'west']

        return restricted
