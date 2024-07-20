from heapq import heappush, heappop, heapify
from collections import Counter

# Data input
data = "AAAAAAABCCCCCCDDEEEEE"

# Step 1: Hitung frekuensi kemunculan setiap simbol
frequency = Counter(data)

# Step 2: Buat pohon Huffman
heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
heapify(heap)

while len(heap) > 1:
    lo = heappop(heap)
    hi = heappop(heap)
    for pair in lo[1:]:
        pair[1] = '0' + pair[1]
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]
    heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

# Step 3: Tentukan kode Huffman untuk setiap simbol
huffman_code = sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
huffman_dict = {symbol: code for symbol, code in huffman_code}

# Tampilkan hasil frekuensi dan kode Huffman
print("Symbol\tFrequency\tHuffman Code")
for symbol, freq in frequency.items():
    code = huffman_dict[symbol]
    print(f"{symbol}\t{freq}\t\t{code}")
