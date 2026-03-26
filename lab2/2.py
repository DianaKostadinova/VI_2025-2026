from searching_framework import *
dir = {"Up": (0, +1), "Down": (0, -1), "Left": (-1, 0), "Right": (+1, 0)}
class Robot(Problem):
    def __init__(self,initial_state,walls, charging,batteryCap,zones, goal=None):
        super().__init__(initial_state,goal)
        self.charging = charging
        self.batteryCap = batteryCap
        self.walls = walls
        self.zones = zones
    def in_zone(self, x,y):
        for r, x1,x2 in self.zones:
            if y==r and x1<=x<=x2:
                return True
        return False
    def successor(self, state):
        successors = dict()
        x,y,battery,used_zone = state
        for action, (dx,dy)in dir.items():
            new_x = x + dx
            new_y = y + dy
            new_battery=battery -1
            if new_battery < 0:
                continue
            if not (0<=new_x<10 and 0<=new_y<10):
                continue
            if used_zone and self.in_zone(new_x, new_y):
                continue
            if self.in_zone(new_x, new_y):
                slide_x=new_x
                while self.in_zone(slide_x, new_y):
                    slide_x+=1
                if not (0<=slide_x<=10):
                    continue
                if (slide_x, new_y) not in self.allowed:
                    continue

                final_x = slide_x
                final_y = new_y
                new_used_zone = True
                if (final_x, final_y) in self.charging:
                    new_battery = self.batteryCap
                successors[action] = (final_x, final_y, new_battery, new_used_zone)
            else:
                if (new_x, new_y)  in self.walls:
                    continue
                final_x = new_x
                final_y = new_y
                new_used_zone = used_zone

                if (final_x, final_y) in self.charging:
                    new_battery = self.batteryCap

                successors[action] = (final_x, final_y, new_battery, new_used_zone)


            successors[action] = (new_x, new_y, new_battery)
        return successors
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        x,y,_=state
        return (x,y)== self.goal
    def h(self,node):
        x,y,_=node.state
        gx,gy=self.goal
        return abs(x-gx)+abs(y-gy)



if __name__ == '__main__':
    grid=(10,10)
    walls = [(4, 0), (5, 0), (7, 5), (8, 5), (9, 5), (1, 6), (1, 7), (0, 6), (0, 8), (0, 9), (1, 9), (2, 9),
             (3, 9)]
    roboPos=tuple(map(int, input().split(",")))
    goalPos=tuple(map(int, input().split(",")))
    batteryCap=int(input())
    nmStations=int(input())
    batLocations=[]
    for i in range(nmStations):
        batLocations.append(tuple(map(int, input().split(","))))
    initial_state = (roboPos[0], roboPos[1], batteryCap)
    problem=Robot(initial_state,walls,batLocations,batteryCap,goalPos)
    result=astar_search(problem)
    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")

