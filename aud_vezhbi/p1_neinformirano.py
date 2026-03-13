from searching_framework import *
class Explorer(Problem):
     def __init__(self,initial, goal=None):
          super().__init__(initial, goal)
          self.max_x=7
          self.max_y=5
     def move_objects(self, o1x,o1y,d1,o2x,o2y,d2):
          if d1==1:
               if o1x==self.max_x:
                    d1=-1
                    o1y-=1
               else :
                    o1y+=1
          else:
               if o1y==0:
                    d1=-1
                    o1y+=1
               else:
                    o1x-=1
          if d2 == 1:
               if o2x == self.max_x:
                    d2 = -1
                    o2y -= 1
               else:
                    o2y += 1
          else:
               if o2y == 0:
                    d2 = -1
                    o2y += 1
               else:
                    o2x -= 1
          return o1x,o1y,d1,o2x,o2y,d2
     def successors(self, state):
          successors = dict()
          x,y,o1x,o1y,d1,o2x,o2y,d2 = state
          o1x,o1y,d1,o2x,o2y,d2=self.move_objects(o1x, o1y, d1, o2x, o2y, d2)
          objects = [(o1x, o1y), (o2x, o2y)]
          if x+1<=self.max_x and (x+1,y) not in objects:
               successors['Right']=(x+1,y,o1x,o1y,d1,o2x,o2y,d2)
          if x-1>=0 and (x-1,y) not in objects:
               successors['Left']=(x-1,y,o1x,o1y,d1,o2x,o2y,d2)
          if y+1<=self.max_y and (x,y+1) not in objects:
               successors['Up']=(x,y+1,o1x,o1y,d1,o2x,o2y,d2)
          if y-1>=0 and (x,y-1) not in objects:
               successors['Down']=(x,y-1,o1x,o1y,d1,o2x,o2y,d2)
          return successors
     def actions(self, state):
          return self.successors(state).keys()
     def result(self, state,action):
          return self.successors(state)[action]
     def goal_test(self, state):
          position=(state[0],state[1])
          return position==self.goal
if __name__ == '__main__':
     goal_state = (7, 4)
     initial_state = (0, 2)
     obstacle_1 = (2, 5, 1)
     obstacle_2 = (5, 0, -1)
     explorer=Explorer((initial_state[0],initial_state[1],obstacle_1[0],obstacle_1[1],obstacle_1[2],obstacle_2[0],obstacle_2[1],obstacle_2[2]),goal_state)
     print(breadth_first_graph_search(explorer).solution())
     print(breadth_first_graph_search(explorer).solve())

