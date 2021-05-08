from vrep_env import ArmEnv
from configs import Configs
# import os
import time

Train_Configs = Configs()
env = ArmEnv()
env.reset()
env.robot.move_to([-0.6,0,0.2],[0,0,0])
print("move to [-0.6,0,0.2]")
time.sleep(0.5)

env.robot.move_to([-0.1,-0.1,0.1],[0,0,0])
print("move to [-0.1,-0.1,0.1]")
time.sleep(0.5)

env.robot.move_to([-0.4,0.1,0.25],[0,0,0])
print("move to [-0.4,0.1,0.25]")
time.sleep(0.5)

env.robot.move_to([0,-0.2,0.1],[0,0,0])
print("move to [0,-0.2,0.1]")
time.sleep(0.5)

env.robot.move_to([-0.45,0,0.1],[0,0,0])
print("move end")


