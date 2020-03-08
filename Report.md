[//]: # (Image References)

[image1]: https://raw.github.com/ounospanas/DLRN_P1_Navigation/master/dqn_score.png "scores"

### Learning Algorithm
This implementation is based on a DQN model, which is a deep Model-Free and Off-policy RL algorithm. It relies also on experience replay memory a mechanism for storing the transitions that the agent observes, allowing us to randomly sample and reuse these data later. Thus, the samples that build up a batch are decorrelated. Moreover, a target network that has its weights frozen and updates them with the policy network's weights every so often, was added to compute target action-values and ensure stability.
 
#### Hyperparameters
A deep fully connected neural network was used having 2 hidden layers. They both consist of 32 neurons.
Some other hyperparameters are:
- max episode termination: 1000
- epsilon starting value: 0.3
- epsilon ending value: 0.01
- epsilon decay: 0.99
- replay buffer size: int(1e5)
- batch size: 128
- gamma: 0.99
- tau (soft update target parameter): 1e-3  
- learning rate: 5e-4 
- update the target network episodes: 4

### Plot of Rewards

![scores][image1]
As shown in the figure above, the environment was solved after 261 episodes.

### Ideas for Future Work
- use a more sophisticated DQN algorithm such as Double DQN, Dueling DQN, Distributional DQN, Noisy DQN etc
- use a more sophisticated way to sample from the buffer such as prioritized experience replay