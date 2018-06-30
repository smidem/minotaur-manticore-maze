class Bounds():

    def __init__(self, current_loc):
        self.bounds = []
        and_index = 0
        length = len(current_loc)

        if any('and' in word for word in current_loc):
            and_index = current_loc.index('and')

        if and_index > 0 and and_index + 1 < length:
            self.bounds = current_loc[and_index + 1: length]
        elif not and_index:
            self.bounds = current_loc

    def interpret(self):
        blocked = []
        type = self.bounds.pop(-1)

        if 'corner' in type or 'wall' in type:
            blocked = self.bounds
        elif 'hall' in type:
            if 'east' in self.bounds[0] and 'west' in self.bounds[1]:
                blocked = ['north', 'south']
            elif 'north' in self.bounds[0] and 'south' in self.bounds[1]:
                blocked = ['east', 'west']
        elif 'end' in type:
            if 'west' in self.bounds:
                blocked = ['north', 'south', 'east']
            elif 'east' in self.bounds:
                blocked = ['north', 'south', 'west']

        return blocked
