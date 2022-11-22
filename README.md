# ISE 7202 Final Project: RL for Visuomotor Control of Robot Arms

## Abstract 

Humans constantly utilize visual feedback to interact with their environments in infinitely
novel ways. In robotics, the technical term for this 'hand-eye coordination' is visuomotor
control. 

As opposed to following a rigid set of instructions, the philosophy of visuomotor control is
to directly transform an image inputs into the next robot state. However, identifying the correct
way to perform this is quite challenging.

However, advancements in Deep-Reinforcement learning have enabled researchers to demonstrate this
style of robotic control. And simulation-based learning environments have made it safe and easy to
collect expert demonstrations of a task and to let agents learn in a low-risk environment. 

In this project, we take inspiration for the results of Chen et Al [[1]](https://arxiv.org/abs/2011.06698v1),
who utilized the TD3 [[2]](https://arxiv.org/abs/1802.09477) algorithm to train their agents.

---

## Installation

All code was written with Python 3.10 on Ubuntu 20.04. Stability for other versions of Python or other unix
operating systems is not guaranteed.

The robotic simulation stack in this project relies upon RLBench [[3]](http://arxiv.org/abs/1909.12271),
PyRep [[4]](http://arxiv.org/abs/1906.11176), and CoppeliaSim [[5]](https://www.coppeliarobotics.com/).
Please download the appropriate CoppeliaSim version and follow the installation instruction in the 
[RLBench repository](https://github.com/stepjam/RLBench) and [PyRep repository](https://github.com/stepjam/PyRep) 
repositories to install these on your system.

Our deep RL algorithms are built with [TensorFlow](https://www.tensorflow.org/). Please ensure this is installed properly.

The `requirements.txt` file has specifications for all additional libraries needed for this project. To ensure these
are met, run:

```shell
pip install -r requirements.txt
```

## Project Overview

To be completed as the project is implemented. The important components are:
- [✅] Set up project repository
- [❌] Defining the TD3 agent and the deep policy structure
- [❌] Writing the scripts for training and saving the policies for a specific task
- [❌] Write scripts to demonstrate a trained agent on its appropriate task 

---

## Sources
[1] B. Chen et al., “Robust Policies via Mid-Level Visual Representations: An Experimental Study in Manipulation and Navigation.” arXiv, Nov. 12, 2020. Accessed: Oct. 18, 2022. [Online]. Available: http://arxiv.org/abs/2011.06698

[2] S. Fujimoto, H. van Hoof, and D. Meger, “Addressing Function Approximation Error in Actor-Critic Methods.” arXiv, Oct. 22, 2018. Accessed: Nov. 21, 2022. [Online]. Available: http://arxiv.org/abs/1802.09477

[3] S. James, Z. Ma, D. R. Arrojo, and A. J. Davison, “RLBench: The Robot Learning Benchmark & Learning Environment,” arXiv:1909.12271 [cs], Sep. 2019, Accessed: Nov. 21, 2022. [Online]. Available: http://arxiv.org/abs/1909.12271

[4] S. James, M. Freese, and A. J. Davison, “PyRep: Bringing V-REP to Deep Robot Learning,” arXiv:1906.11176 [cs], Jun. 2019, Accessed: Nov. 21, 2022. [Online]. Available: http://arxiv.org/abs/1906.11176

[5] E. Rohmer, S. P. N. Singh, and M. Freese, “V-REP: A versatile and scalable robot simulation framework,” in 2013 IEEE/RSJ International Conference on Intelligent Robots and Systems, Tokyo, Nov. 2013, pp. 1321–1326. doi: 10.1109/IROS.2013.6696520.


