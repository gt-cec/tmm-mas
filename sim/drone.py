import numpy as np

class Drone:
    def __init__(self, name: str, 
                 path: str, 
                 PID: list = [1,0,0], 
                 zPID: list = [1,0,0],
                 state: int = 0) -> None:
                 
        self.name = name
        self.path = path

        # PID
        self.PID = PID
        self.zPID = zPID

        # PID controller state
        self.integral_error = np.zeros(3)  # Integral error for x, y, z
        self.prev_error = np.zeros(3)      # Previous error for x, y, z

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
        self.flags = []

        self.y_grid = []
        self.x_grid = []

    def setPath(self, x_grid: list, y_grid: list, dz:list, flags:list, key) -> None:
        self.y_grid = y_grid
        self.x_grid = x_grid

        self.dy = [key[i][0] for i in y_grid]
        self.dx = [key[i][1] for i in x_grid]
        self.dz = dz
        self.flags = flags
    
    def getPath(self):
        x_values = self.x_grid
        y_values = self.y_grid
        return [[x, y] for x, y in zip(x_values, y_values)]

    def setPID(self, PID: list, zPID: list) -> None:
        self.PID = PID
        self.zPID = zPID

    # State update function
    def update_drone_state(self, state, control_input, dt):
        # Unpack state variables
        x, y, z, vx, vy, vz = state
        ax, ay, az = control_input

        # Update position
        x_new = x + vx * dt
        y_new = y + vy * dt
        z_new = z + vz * dt

        # Update velocity
        vx_new = vx + ax * dt
        vy_new = vy + ay * dt
        vz_new = vz + az * dt

        # New state
        return np.array([x_new, y_new, z_new, vx_new, vy_new, vz_new])

    # PID control function
    def pid_control(self, goal, dt):
        # PIDs
        Kp = [self.PID[0], self.PID[0], self.zPID[0]]
        Ki = [self.PID[1], self.PID[1], self.zPID[1]]
        Kd = [self.PID[2], self.PID[2], self.zPID[2]]

        # Compute position error
        position = self.pose  # x, y, z
        error = goal - position

        # Update integral and derivative errors
        self.integral_error += error * dt
        derivative_error = (error - self.prev_error) / dt

        # PID control law
        control_input = Kp * error + Ki * self.integral_error + Kd * derivative_error

        # Update previous error
        self.prev_error = error

        return control_input