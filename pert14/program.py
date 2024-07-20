import random
import numpy
# Parameter dan variabel global
v = [10,5,4,12]
w = [5,0.4,1,0.5]
max_w = 6
n_item = len(v)
n_kombinasi = 2 ** n_item
n_populasi = 8
n_bit = n_item

#fungsi untuk mengubah desimal ke biner
def DecimalToBinary(num):
    return bin(num).replace("0b", "").zfill(n_bit)

# fungsi untuk menghasilkan populasi awal
def generatePopulation():
    rnd = random.sample(range(n_kombinasi - 1), n_populasi)
    pop = numpy.zeros(shape=(n_populasi, n_item + 2))
    for idx, val in enumerate(rnd):
        binaryDigit = DecimalToBinary(val)
        for idy, j in enumerate(binaryDigit):
            pop[idx][idy] = int(j)
    return computeFitness(pop)

# fungsi untuk menghitung fitness
def computeFitness(matrix):
    for i in range(len(matrix)):
        matrix[i][4] = sum(matrix[i][j] * v[j] for j in range(n_item))
        matrix[i][5] = sum(matrix[i][j] * w[j] for j in range(n_item))
        if matrix[i][5] > max_w:
            matrix[i][4] = 0 # set fitness to 0 if weight exceeds max_w
    return matrix

#fungsi seleksi
def selection(matrix):
    selected = [row for row in matrix if 0 < row[5] <=max_w]
    if selected:
        return numpy.array(selected)
    else:
        return numpy.zeros(shape=(0, n_item + 2)) #return empty array if no selection
    
#fungsi untuk crossover
def crossOver(matrix):
    for i in range(int(len(matrix) / 2 )):
        offspring = offSpring(matrix[i * 2], matrix[i * 2 + 1])
        matrix[i * 2], matrix[i * 2 + 1] = offspring
    return matrix

#fungsi untuk melakukan offspring (cross over antara dua kromsom)
def offSpring(chromosome_x, chromosome_y):
    i, j = random.sample(range(n_bit), 2)
    chromosome_x[i], chromosome_y[j] = chromosome_y[i], chromosome_x[j]
    return chromosome_x, chromosome_y

#fungsi mutasi
def mutation(matrix):
    for row in matrix:
        if random.random() < 0.1: #misalnya probabilitas mutasi adalah 10%
            idx = random.randrange(n_bit)
            row[idx] = 1 - row[idx] # Flip the bit
    return matrix

#fungsi untuk menemukan nilai maksimum fitness
def findMax(matrix):
    values = matrix[:, 4]
    max_val = max(values)
    print('Max:', max_val)
    return max_val
# simulasi algoritma genetika
pop = generatePopulation()
for i in range(1): # misalnya, jalankan untuk 5 generasi
    pop = selection(pop)
    pop = crossOver(pop)
    pop = mutation(pop)
    pop = computeFitness(pop)
    print('Generation:', i + i, '\n', pop)
    findMax(pop)