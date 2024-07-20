import numpy as np

# Definisikan dua matriks 2x2
A = np.array([[5, 8], [9, 4]])
B = np.array([[5, 7], [9, 3]])

# Fungsi untuk menghitung invers dari matriks 2x2
def inverse_2x2(matrix):
    det = matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    if det == 0:
        raise ValueError("Matriks tidak memiliki invers karena determinan adalah 0")
    
    inv_det = 1 / det
    return inv_det * np.array([[matrix[1, 1], -matrix[0, 1]], [-matrix[1, 0], matrix[0, 0]]])

# Hitung invers dari matriks B
B_inv = inverse_2x2(B)

# Lakukan perkalian matriks A dengan invers dari matriks B
C = np.dot(A, B_inv)

# Cetak hasil
print("Hasil dari pembagian A / B =")
print(C)