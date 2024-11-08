import numpy as np

class Drone:
    def __init__(self, name: str, 
                 path: str, 
                 PID: list = [1.5,0,2], 
                 zPID: list = [2,0,0.5]) -> None:
        self.name = name
        self.path = path

        # PID
        self.PID = PID
        self.zPID = zPID

        # Stored pose
        self.pose_prev = [0,0,0]
        self.del_prev = [0,0,0]

        self.pose = [0,0,0]

        self.dy = []
        self.dx = []
        self.dz = []

        self.dind = 0

    def setPath(self, x_grid: list, y_grid: list, dz:list, key):
        self.dy = [key[i][0] for i in y_grid]
        self.dx = [key[i][1] for i in x_grid]
        self.dz = dz