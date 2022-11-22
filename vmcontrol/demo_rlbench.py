'''
Main testing program for re-familiarization with the RLBench / PyRep / CopelliaSim robotic
reinforcement learning of multi-step tasks.

This program simply launches CoppeliaSim with the StackBlocks task and lets the agent
run for 100 time steps with completely random commands.

The commands are for the velocity of all 6 axes and the state of the gripper (open or closed).
'''


# import tensorflow as tf

import numpy as np

from rlbench.action_modes.action_mode import MoveArmThenGripper
from rlbench.action_modes.arm_action_modes import JointVelocity
from rlbench.action_modes.gripper_action_modes import Discrete
from rlbench.environment import Environment
from rlbench.tasks import ReachTarget, StackBlocks


def main():
    """ Program entry point """
    action_mode = MoveArmThenGripper(arm_action_mode=JointVelocity(),
                                     gripper_action_mode=Discrete()
                                    )
    env = Environment(action_mode)
    env.launch()

    task = env.get_task(StackBlocks)
    descriptions, obs = task.reset()
    terminate = 0
    step_num = 0
    while step_num < 100 and terminate == 0:
        obs, reward, terminate = task.step(np.random.normal(size=env.action_shape))
        step_num += 1


if __name__ == '__main__':
    main()

