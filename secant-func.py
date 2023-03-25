import random
import matplotlib.pyplot as plt

#2

def n_finder():
    count = 1
    sum = 0
    while True:
        sum = sum + random.random()
        if sum > 4:
            return count
        count = count+1

trials = [100,1000,10000]

for trial in trials:
    n=[]
    for i in range(trial):
        n.append(n_finder())
    plt.hist(n, width = 0.5)
    plt.xlabel('Range')
    plt.ylabel('Frequency')
    plt.show()
