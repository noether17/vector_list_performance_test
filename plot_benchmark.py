import json
import matplotlib.pyplot as plt
import numpy as np

names = []
items = []
item_sizes = []
items_per_s = []
bytes_per_s = []
with open("output.json") as file:
    data = json.load(file)
    benchmarks = data['benchmarks']
    for bm in benchmarks:
        names.append(bm['name'])
        items.append(bm['items'])
        item_sizes.append(bm['item_size'])
        items_per_s.append(bm['items_per_second'])
        bytes_per_s.append(bm['bytes_per_second'])

# convert lists to np arrays
names = np.array(names)
items = np.array(items)
item_sizes = np.array(item_sizes)
items_per_s = np.array(items_per_s)
bytes_per_s = np.array(bytes_per_s)

# calculate bytes
bytes = items*item_sizes

# separate data based on container type and word size
v1_indices   = np.where(np.char.find(names, 'vector_insert<1') > 0)
v8_indices   = np.where(np.char.find(names, 'vector_insert<8') > 0)
v64_indices  = np.where(np.char.find(names, 'vector_insert<64') > 0)
v512_indices = np.where(np.char.find(names, 'vector_insert<512') > 0)
l1_indices   = np.where(np.char.find(names, 'list_insert<1') > 0)
l8_indices   = np.where(np.char.find(names, 'list_insert<8') > 0)
l64_indices  = np.where(np.char.find(names, 'list_insert<64') > 0)
l512_indices = np.where(np.char.find(names, 'list_insert<512') > 0)

# plot items/s vs items
plt.loglog(items[v1_indices], items_per_s[v1_indices], 'b-+', label='vector<1w>')
plt.loglog(items[v8_indices], items_per_s[v8_indices], 'b-P', label='vector<8w>')
plt.loglog(items[v64_indices], items_per_s[v64_indices], 'b-x', label='vector<64w>')
plt.loglog(items[v512_indices], items_per_s[v512_indices], 'b-X', label='vector<512w>')
plt.loglog(items[l1_indices], items_per_s[l1_indices], 'r-+', label='list<1w>')
plt.loglog(items[l8_indices], items_per_s[l8_indices], 'r-P', label='list<8w>')
plt.loglog(items[l64_indices], items_per_s[l64_indices], 'r-x', label='list<64w>')
plt.loglog(items[l512_indices], items_per_s[l512_indices], 'r-X', label='list<512w>')
plt.xlabel("items")
plt.ylabel("items / s")
plt.title("Performance Comparison Between Vector and List for Various Node Sizes")
plt.legend()
plt.show()

# plot bytes/s vs bytes
plt.loglog(bytes[v1_indices], bytes_per_s[v1_indices], 'b-+', label='vector<1w>')
plt.loglog(bytes[v8_indices], bytes_per_s[v8_indices], 'b-P', label='vector<8w>')
plt.loglog(bytes[v64_indices], bytes_per_s[v64_indices], 'b-x', label='vector<64w>')
plt.loglog(bytes[v512_indices], bytes_per_s[v512_indices], 'b-X', label='vector<512w>')
plt.loglog(bytes[l1_indices], bytes_per_s[l1_indices], 'r-+', label='list<1w>')
plt.loglog(bytes[l8_indices], bytes_per_s[l8_indices], 'r-P', label='list<8w>')
plt.loglog(bytes[l64_indices], bytes_per_s[l64_indices], 'r-x', label='list<64w>')
plt.loglog(bytes[l512_indices], bytes_per_s[l512_indices], 'r-X', label='list<512w>')
plt.axvline(x=32768, label="L1 Dcache", linestyle="--")
plt.axvline(x=262144, label="L2 cache", linestyle="--")
plt.axvline(x=2**24, label="L3 cache", linestyle="--")
plt.xlabel("bytes")
plt.ylabel("bytes / s")
plt.title("Performance Comparison Between Vector and List for Various Node Sizes")
plt.legend()
plt.show()