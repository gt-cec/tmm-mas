import numpy as np

class Drone:
    def __init__(self, name: str, 
                 path: str, 
                 PID: list = [1.5,0,2], 
                 zPID: list = [2,0,0.5],
                 state: int = 0) -> None:
                 
        self.name = name
        self.path = path

        # PID
        self.PID = PID
        self.zPID = zPID

        # Stored poses
        self.pose_prev = [0,0,0]
        self.del_prev = [0,0,0]
        self.pose = [0,0,0]

        self.dind = 0

        # Path planning input type
        self.state = state
        self.dind = 0
        self.dy = []
        self.dx = []
        self.dz = []

    def setPath(self, x_grid: list, y_grid: list, dz:list, key) -> None:
        self.dy = [key[i][0] for i in y_grid]
        self.dx = [key[i][1] for i in x_grid]
        self.dz = dz

    def setPID(self, PID: list, zPID: list) -> None:
        self.PID = PID
        self.zPID = zPID