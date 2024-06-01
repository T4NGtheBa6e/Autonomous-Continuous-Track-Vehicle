# Embedded System about Autonomous Continuous Track Vehicle

## Introduction
Learn Mbed operating system API and some open-source software, and design relevant system programs. Finally, integrate what you have learned to implement an autonomous "continuous track vehicle" capable of completing a specified route.

## Goal
Using Raspberry Pi, put it on a simplified vehicle to handle data transmission. Then, self-determine the direction of movement to complete a full lap.

## System Architecture
1. **Camera Image Processing, then send it back to Raspberry Pi**
    - Image matrix transformation

2. **The Raspberry Pi assesses the current situation and provides the correct message to the vehicle side.**
    - Determine whether the vehicle is on the specified route.
    - Using python's Socket
    - <img width="605" alt="image" src="https://github.com/T4NGtheBa6e/Self-propelled-tracked-vehicle/assets/155707117/18e76798-e93f-4203-97d9-b901ce957b8c">


3. **The car side receives the message and executes corresponding instructions.**
