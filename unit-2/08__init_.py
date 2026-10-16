"""robotkit = a tiny package of robot helpers for the cou """

class Robot:
    fleet_size=0
    def __init__(self,name):
        self.name=name
        Robot.fleet_size+=1

a=Robot("Alpha")
b=Robot("Beta")
print(Robot.fleet_size,a.name,b.name)
    