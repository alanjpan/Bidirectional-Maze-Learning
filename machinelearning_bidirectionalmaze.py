# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 16:06:26 2018

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

Machine learning a bidirectional maze.

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Bidirectional Maze Learning [Computer software]. Github repository <https://github.com/alanjpan/Bidirectional-Maze-Learning>

Note this software's license is GNU GPLv3.
"""

import random
import math

#maze with solution left left left right
maze = [0, 0, 0, 1, 1, 1]

#action event to select left or right
action = 100

#learning rate
def learn(step):
    global action
    return int(action/(1+math.pow(math.e,-step)))

#rewards program for success
def leftsuccess(step):
    global action
    action -= learn(step)
    if action <= 50:
        action = 60
def rightsuccess(step):
    global action
    action += learn(step)
    if action <= 50:
        action = 60

#punishes program for failure
def leftfailure(step):
    global action
    action += learn(step)
    if action <= 50:
        action = 60
def rightfailure(step):
    global action
    action -= learn(step)
    if action <= 50:
        action = 60
    
successes = 0
almostsuccesses = 0
def entermaze():
    global successes
    global almostsuccesses
    
    move = 0
    step = 1
    for i in maze:
        select = random.randrange(0, action, 1)
        #select left
        if select <= 50:
            move = 0
        #select right
        elif select >= 50:
            move = 1
        if move == i:
            if move == 0:
                leftsuccess(step)
            elif move == 1:
                rightsuccess(step)
        else:
            if move == 0:
                leftfailure(step)
                print('unsuccessful move ' + str(select) + '/' + str(action))
                break
            elif move == 1:
                rightfailure(step)
                print('unsuccessful move ' + str(select) + '/' + str(action))
                break
        print('successful move ' + str(select) + '/' + str(action))
        step += 1
    print('end of maze')
    if step == len(maze)+1:
        successes += 1
    if step == len(maze):
        almostsuccesses+=1

for i in range(1000):
    entermaze()
print('number of successful runs: ' + str(successes))
print('number of almost successful runs (by one step): ' + str(almostsuccesses))

#returns probability of successes
def probability(success, failure):
    outcomes = success + failure
    likelihood = success / outcomes
    return likelihood