import os
import numpy as np
from matplotlib import pyplot as plt


# Simple codre. There may be more efficient ways.
def extract_data(filename):
    infile = open(filename, 'r')
    timestamp = []
    x = []
    y = []
    pol = []
    for line in infile:
        words = line.split()
        timestamp.append(float(words[0]))
        x.append(int(words[1]))
        y.append(int(words[2]))
        pol.append(int(words[3]))
    infile.close()
    return timestamp,x,y,pol
'''
filename_sub = 'slider_depth/events_chunk.txt'
# Call the function to read data
timestamp, x, y, pol = extract_data(filename_sub)

events_raw = open('D:\workspace\events_viz-master\slider_depth\events.txt', "r")
events_sub = open(filename_sub, "w")
# format: timestamp, x, y, polarity

for k in range(50000):
    line = events_raw.readline()
    # print(line)
    events_sub.write(line)

events_raw.close()
events_sub.close()
'''