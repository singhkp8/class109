import random
import plotly_express as pe
import plotly.figure_factory as pff
import statistics

result = []
count = []

for i in range(1000,10000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result.append(dice1 + dice2)
    count.append(i)


mean = sum(result)/len(result)
print(mean)

median = statistics.median(result)
print(median)

mode = statistics.mode(result)
print(mode)

standard_dev = statistics.stdev(result)
print(standard_dev)

fig1 = pff.create_distplot([result],["result"],show_hist=False)
fig1.show()