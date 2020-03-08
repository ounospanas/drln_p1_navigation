# DLRN_P1_Navigation
DQN-based solution to the 1st project of Udacity's DRL nanodegree

[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif "Trained Agent"

# Solution for DLRN Project 1: Navigation

### Introduction

For this project, an AI agent is trained to navigate (and collect bananas!) in a Unity-based large square world.  

![Trained Agent][image1]

### World physics

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana.  Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.  

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  Given this information, the agent has to learn how to best select actions.  Four discrete actions are available, corresponding to:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.

### Getting Started (only if you have OS different from Linux)

1. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip) to obtain the environment.

2. Place the file in the `DLRN_P1_Navigation/` folder, and unzip (or decompress) the file. 
### Dependencies installation
Similarly to the [DRLN GiHub repository](https://github.com/udacity/deep-reinforcement-learning) run the following: 
```bash
git clone https://github.com/udacity/deep-reinforcement-learning.git
cd deep-reinforcement-learning/python
pip install .
```
### DQN algorithm
This implementation is based on a DQN model, which is a deep Model-Free and	Off-policy RL algorithm. It relies also on experience replay memory a mechanism for storing the transitions that the agent observes, allowing us to randomly sample and reuse these data later. Thus, the samples that build up a batch are decorrelated. Moreover, a target network that has its weights frozen and updates them with the policy networkâ€™s weights every so often, was added to compute target action-values and ensure stability.

### Instructions
Run the cells in the `Navigation.ipynb` to get started with training your own agent! An already trained model is provided in the `checkpoint.pth`. 
