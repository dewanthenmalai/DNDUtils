import numpy as np
import matplotlib.pyplot as plt

buckets = [i for i in range(1, 21)]
quantities  = [0 for i in range(20)]
values = []

for i in range(100000):
    rolls = np.random.randint(1, 21, size = 2)
    keep = rolls.max()
    values.append(keep)
    quantities[keep - 1] += 1

avg = sum(values) / len(values)
print(avg)
plt.xticks(buckets)
plt.bar(buckets, quantities)
plt.show()