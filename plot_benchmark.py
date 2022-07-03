import json
import matplotlib.pyplot as plt
import numpy as np

# read data
names = []
items = []
item_sizes = []
items_per_s = []
bytes_per_s = []
with open("output.json") as file:
    data = json.load(file)
    caches = [x for x in data['context']['caches'] if x['type'] != 'Instruction']
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
vr1_indices   = np.where(np.char.find(names, 'vector_random_insert<1>') > 0)
vr8_indices   = np.where(np.char.find(names, 'vector_random_insert<8>') > 0)
vr64_indices  = np.where(np.char.find(names, 'vector_random_insert<64>') > 0)
vr128_indices = np.where(np.char.find(names, 'vector_random_insert<128>') > 0)
vr256_indices = np.where(np.char.find(names, 'vector_random_insert<256>') > 0)
vr512_indices = np.where(np.char.find(names, 'vector_random_insert<512>') > 0)
lr1_indices   = np.where(np.char.find(names, 'list_random_insert<1>') > 0)
lr8_indices   = np.where(np.char.find(names, 'list_random_insert<8>') > 0)
lr64_indices  = np.where(np.char.find(names, 'list_random_insert<64>') > 0)
lr128_indices = np.where(np.char.find(names, 'list_random_insert<128>') > 0)
lr256_indices = np.where(np.char.find(names, 'list_random_insert<256>') > 0)
lr512_indices = np.where(np.char.find(names, 'list_random_insert<512>') > 0)
vf1_indices   = np.where(np.char.find(names, 'vector_front_insert<1>') > 0)
vf8_indices   = np.where(np.char.find(names, 'vector_front_insert<8>') > 0)
vf64_indices  = np.where(np.char.find(names, 'vector_front_insert<64>') > 0)
vf128_indices = np.where(np.char.find(names, 'vector_front_insert<128>') > 0)
vf256_indices = np.where(np.char.find(names, 'vector_front_insert<256>') > 0)
vf512_indices = np.where(np.char.find(names, 'vector_front_insert<512>') > 0)
lf1_indices   = np.where(np.char.find(names, 'list_front_insert<1>') > 0)
lf8_indices   = np.where(np.char.find(names, 'list_front_insert<8>') > 0)
lf64_indices  = np.where(np.char.find(names, 'list_front_insert<64>') > 0)
lf128_indices = np.where(np.char.find(names, 'list_front_insert<128>') > 0)
lf256_indices = np.where(np.char.find(names, 'list_front_insert<256>') > 0)
lf512_indices = np.where(np.char.find(names, 'list_front_insert<512>') > 0)

# plot items/s vs items
plt.loglog(items[vr1_indices],   items_per_s[vr1_indices],   'b-+', label=f'vector<4B>random')
plt.loglog(items[vr8_indices],   items_per_s[vr8_indices],   'b-P', label=f'vector<32B>random')
plt.loglog(items[vr64_indices],  items_per_s[vr64_indices],  'b-x', label=f'vector<256B>random')
plt.loglog(items[vr128_indices], items_per_s[vr128_indices], 'b-X', label=f'vector<512B>random')
plt.loglog(items[vr256_indices], items_per_s[vr256_indices], 'b-v', label=f'vector<1024B>random')
plt.loglog(items[vr512_indices], items_per_s[vr512_indices], 'b-^', label=f'vector<2048B>random')
plt.loglog(items[lr1_indices],   items_per_s[lr1_indices],   'r-+', label=f'list<4B>random')
plt.loglog(items[lr8_indices],   items_per_s[lr8_indices],   'r-P', label=f'list<32B>random')
plt.loglog(items[lr64_indices],  items_per_s[lr64_indices],  'r-x', label=f'list<256B>random')
plt.loglog(items[lr128_indices], items_per_s[lr128_indices], 'r-X', label=f'list<512B>random')
plt.loglog(items[lr256_indices], items_per_s[lr256_indices], 'r-v', label=f'list<1024B>random')
plt.loglog(items[lr512_indices], items_per_s[lr512_indices], 'r-^', label=f'list<2048B>random')
plt.loglog(items[vf1_indices],   items_per_s[vf1_indices],   'k-+', label=f'vector<4B>front')
plt.loglog(items[vf8_indices],   items_per_s[vf8_indices],   'k-P', label=f'vector<32B>front')
plt.loglog(items[vf64_indices],  items_per_s[vf64_indices],  'k-x', label=f'vector<256B>front')
plt.loglog(items[vf128_indices], items_per_s[vf128_indices], 'k-X', label=f'vector<512B>front')
plt.loglog(items[vf256_indices], items_per_s[vf256_indices], 'k-v', label=f'vector<1024B>front')
plt.loglog(items[vf512_indices], items_per_s[vf512_indices], 'k-^', label=f'vector<2048B>front')
plt.loglog(items[lf1_indices],   items_per_s[lf1_indices],   'y-+', label=f'list<4B>front')
plt.loglog(items[lf8_indices],   items_per_s[lf8_indices],   'y-P', label=f'list<32B>front')
plt.loglog(items[lf64_indices],  items_per_s[lf64_indices],  'y-x', label=f'list<256B>front')
plt.loglog(items[lf128_indices], items_per_s[lf128_indices], 'y-X', label=f'list<512B>front')
plt.loglog(items[lf256_indices], items_per_s[lf256_indices], 'y-v', label=f'list<1024B>front')
plt.loglog(items[lf512_indices], items_per_s[lf512_indices], 'y-^', label=f'list<2048B>front')
plt.xlabel("items")
plt.ylabel("items / s")
plt.title("Insert Performance of Vector and List for Various Node Sizes")
plt.legend()
plt.show()

# plot bytes/s vs bytes
plt.loglog(bytes[vr1_indices],   bytes_per_s[vr1_indices],   'b-+', label=f'vector<4B>random')
plt.loglog(bytes[vr8_indices],   bytes_per_s[vr8_indices],   'b-P', label=f'vector<32B>random')
plt.loglog(bytes[vr64_indices],  bytes_per_s[vr64_indices],  'b-x', label=f'vector<256B>random')
plt.loglog(bytes[vr128_indices], bytes_per_s[vr128_indices], 'b-X', label=f'vector<512B>random')
plt.loglog(bytes[vr256_indices], bytes_per_s[vr256_indices], 'b-v', label=f'vector<1024B>random')
plt.loglog(bytes[vr512_indices], bytes_per_s[vr512_indices], 'b-^', label=f'vector<2048B>random')
plt.loglog(bytes[lr1_indices],   bytes_per_s[lr1_indices],   'r-+', label=f'list<4B>random')
plt.loglog(bytes[lr8_indices],   bytes_per_s[lr8_indices],   'r-P', label=f'list<32B>random')
plt.loglog(bytes[lr64_indices],  bytes_per_s[lr64_indices],  'r-x', label=f'list<256B>random')
plt.loglog(bytes[lr128_indices], bytes_per_s[lr128_indices], 'r-X', label=f'list<512B>random')
plt.loglog(bytes[lr256_indices], bytes_per_s[lr256_indices], 'r-v', label=f'list<1024B>random')
plt.loglog(bytes[lr512_indices], bytes_per_s[lr512_indices], 'r-^', label=f'list<2048B>random')
plt.loglog(bytes[vf1_indices],   bytes_per_s[vf1_indices],   'k-+', label=f'vector<4B>front')
plt.loglog(bytes[vf8_indices],   bytes_per_s[vf8_indices],   'k-P', label=f'vector<32B>front')
plt.loglog(bytes[vf64_indices],  bytes_per_s[vf64_indices],  'k-x', label=f'vector<256B>front')
plt.loglog(bytes[vf128_indices], bytes_per_s[vf128_indices], 'k-X', label=f'vector<512B>front')
plt.loglog(bytes[vf256_indices], bytes_per_s[vf256_indices], 'k-v', label=f'vector<1024B>front')
plt.loglog(bytes[vf512_indices], bytes_per_s[vf512_indices], 'k-^', label=f'vector<2048B>front')
plt.loglog(bytes[lf1_indices],   bytes_per_s[lf1_indices],   'y-+', label=f'list<4B>front')
plt.loglog(bytes[lf8_indices],   bytes_per_s[lf8_indices],   'y-P', label=f'list<32B>front')
plt.loglog(bytes[lf64_indices],  bytes_per_s[lf64_indices],  'y-x', label=f'list<256B>front')
plt.loglog(bytes[lf128_indices], bytes_per_s[lf128_indices], 'y-X', label=f'list<512B>front')
plt.loglog(bytes[lf256_indices], bytes_per_s[lf256_indices], 'y-v', label=f'list<1024B>front')
plt.loglog(bytes[lf512_indices], bytes_per_s[lf512_indices], 'y-^', label=f'list<2048B>front')
for cache in caches:
    plt.axvline(x=cache['size'], label=f"L{cache['level']} {cache['type']} Cache", linestyle='--')
plt.xlabel("bytes")
plt.ylabel("bytes / s")
plt.title("Insert Performance of Vector and List for Various Node Sizes")
plt.legend()
plt.show()