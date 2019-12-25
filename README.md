# The-Tensorsaur
> A Project Using Tensor Flow to play a version of the Chrome Dinosaur Game

## Overview
This project's goal is to create an application to emmulate the Dinosaur Game using Python. Then, using Tensorflow produce a machine learning algorithm that is able to play the game based off of previously created data.

## Update in Process (Update Completed)
We are moving over to OpenAI's Gym Environment for our game combined with a high level api to make the game faster, image capture easier, along with just streamlining the process. The Old Project is under LinearLearn_Deprecated.

## Navigation
LinearLearn_Deprecated contains the human playable version of the game which is the most polished version of the game itself. It also supports switching to AI mode, utilizing Tensorflow, which learns off of human created data. However, as it is the predictions take too long for the AI to play the game. To make the game smoother and playable for the AI we switched to a Q-Learning model found in the QLearning directory. The AI learns off of its own mistakes, getting better the longer it plays.
