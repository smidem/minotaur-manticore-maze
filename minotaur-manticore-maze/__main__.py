from load_map import LoadMap
from bounds import Bounds
# from navigation import Navigation

map = LoadMap('map.csv', start_row=4, start_col=0)
current_loc = map.start_point

bounds = Bounds(current_loc).interpret()
print(bounds)
