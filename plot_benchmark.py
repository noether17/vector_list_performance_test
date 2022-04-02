import json
import matplotlib.pyplot as plt
import numpy as np

names = []
items = []
items_per_s = []
with open("output.json") as file:
    data = json.load(file)
    benchmarks = data['benchmarks']
    for bm in benchmarks:
        names.append(bm['name'])
        items.append(bm['items'])
        items_per_s.append(bm['items_per_second'])

v_indices = np.where(np.char.find(names, 'vector') > 0)
l_indices = np.where(np.char.find(names, 'list') > 0)
items = np.array(items)
items_per_s = np.array(items_per_s)
plt.loglog(items[v_indices], items_per_s[v_indices], 'b', label='vector')
plt.loglog(items[l_indices], items_per_s[l_indices], 'r', label='list')
plt.legend()
plt.show()