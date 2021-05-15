import math
import heapq

directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
max_g = 100000000000

class Point:
  def __init__(self, x, y, topo_map=None):
    self.x = x
    self.y = y
    self.topo_map = topo_map
    self.height = topo_map.height_map[y][x] if (topo_map and self.inBounds()) else -1

    self.g = 0
    self.h = 0
    self.f = 0

  def __lt__(self, other):
    return self.f < other.f

  def inBounds(self):
    height_map = self.topo_map.height_map
    map_height = len(height_map)
    map_width = len(height_map[0])
    return (self.x >= 0) and (self.x < map_width) and (self.y >= 0) and (self.y < map_height)
  
  def dist(self, other):
    return math.sqrt(
      ((self.x - other.x) * self.topo_map.dist_between_pixels) ** 2 + 
      ((self.y - other.y) * self.topo_map.dist_between_pixels) ** 2 + 
      (self.height - other.height) ** 2)

  def sameCoord(self, other):
    return self.x == other.x and self.y == other.y
  
  def heuristic(self, other):
    return self.dist(other)

def find_path(topo_map, start, dest):
  print("in lops")
  height_map = topo_map.height_map
  map_height = len(height_map)
  map_width = len(height_map[0])

  min_g = [x[:] for x in [[max_g] * map_width] * map_height]
  min_g[start.y][start.x] = 0
  parent = [x[:] for x in [[None] * map_width] * map_height]

  to_visit = [Point(start.x, start.y, topo_map)]
  heapq.heapify(to_visit)

  while to_visit: 
    curr_point = heapq.heappop(to_visit)

    if(curr_point.sameCoord(dest)):
      break

    if(min_g[curr_point.y][curr_point.x] < curr_point.g):
      continue

    for direction in directions:
      next_point = Point(curr_point.x + direction[0], curr_point.y + direction[1], topo_map)

      if(not next_point.inBounds()):
        continue

      next_point.g = min_g[curr_point.y][curr_point.x] + curr_point.dist(next_point)
      next_point.h = next_point.heuristic(dest)
      next_point.f = next_point.g + next_point.h
      
      # Shorter path was found!
      # It is possible that this point has already been traversed and we are revisiting a path
      if(next_point.g < min_g[next_point.y][next_point.x]):
        min_g[next_point.y][next_point.x] = next_point.g
        parent[next_point.y][next_point.x] = curr_point
        heapq.heappush(to_visit, next_point)
      
  curr_point = dest
  path = [x[:] for x in [[False] * map_width] * map_height]
  while(curr_point != None):
    path[curr_point.y][curr_point.x] = True
    curr_point = parent[curr_point.y][curr_point.x]

  return path
