import numpy

A = numpy.array([1, 3, 7, 2, 8])
print(A, "\n")
B = numpy.array([[1, 2, 3], [4, 5, 6]])
print(B, "\n")
C= B.transpose()
print(C, "\n")

#macierze
D = numpy.arange(100)
print(D, "\n")

#dla list trzeba tworzyć for i iteracje, aby zrobić działania na liście
L = [1, 3, 5, 2, 3, 1]
for i in range(len(L)):
    L[i] = L[i]*2
print(L)

L_podwajam_l_el = L*2
print(L_podwajam_l_el, "\n")

#mnożenie macierzy
M = numpy.array([1, 3, 5, 2, 3, 1])
M = M*2
print(M)

#zadania
Z = numpy.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print(Z)

a = 0
for i in range(len(Z)):
    a+=Z[i, i]
print("Ślad macierzy wynosi: ", a)

V = Z.transpose()
print("\nTranspozycja macierz:\n", V)



