
# Hierarchical Deep Temporal Model for Group Activity Recognition
## A PyTorch Implementation of the CVPR 2016 Paper: [*A Hierarchical Deep Temporal Model for Group Activity Recognition*](http://www.cs.sfu.ca/~mori/research/papers/ibrahim-cvpr16.pdf) *Written by Mostafa S. Ibrahim, Srikanth Muralidharan, Zhiwei Deng, Arash Vahdat, and Greg Mori* 

## Table of Contents
- [Abstract](#abstract)
- [Paper Overview](#paper-overview)
- [Model Architecture](#model-architecture)
- [Dataset](#dataset)
- [Experiments](#experiments)
- [Results and Comparison with the Paper](#results-and-comparison-with-the-paper)
- [Key Differences from the Original Paper](#key-differences-from-the-original-paper)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage and Demo](#usage-and-demo)
- [Poster](#poster)

---
## Abstract

This repository provides a PyTorch reimplementation of the hierarchical deep temporal model proposed in CVPR 2016 for group activity recognition.
The model captures temporal dynamics at both the individual-person level and the group level using a two-stage LSTM architecture.
The implementation aims to 

---
## Paper Overview

### 1- Problem

Group Activity Recognition aims to identify the **collective activity** performed by a group of people in a video scene, rather than recognizing individual actions in isolation.

This task is challenging because:

- Group activities depend on **interactions between individuals**
- **Temporal dynamics** are critical at both individual and group levels
- Frame-level or holistic image classification fails to capture these relationships


### 2- Key Idea

The paper proposes a **hierarchical deep temporal model** based on **LSTM networks** that models activity at two levels:

#### Person-level Temporal Modeling
- Each person is processed independently
- CNN features are extracted from person bounding boxes
- An LSTM captures the temporal evolution of each individual’s action

#### Group-level Temporal Modeling
- Person-level representations are aggregated using pooling
- The aggregated representation is used to infer the group activity

---
## Model Architecture
---
## Dataset
---
## Experiments
---
## Results and Comparison with the Paper
---
## Key Differences from the Original Paper
---
## Installation
---
## Project Structure
---
## Usage and Demo
---
## Poster
