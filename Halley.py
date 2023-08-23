import math
import time

A = [[0.0] * 15 for _ in range(9)]
X = [0.0] * 15
Y = [0.0] * 15

K = 6.28
PHD = 0.59
PH = 1986.10833
SD = 1985.525
TI = 0.0833
N = 13

for I in range(1, N + 1):
    A[6][I] = K * (SD + (I - 1) * TI - PH) / (math.sqrt(2 * PHD ** 3))
    if I == 1:
        A[1][I] = A[6][I]
    A[5][I] = -(A[1][I] ** 3 + 3 * A[1][I] - 3 * A[6][I]) / (3 * A[1][I] ** 2 + 3)
    A[2][I] = A[1][I] + A[5][I]
    A[3][I] = A[2][I] ** 3 + 3 * A[2][I] - 3 * A[6][I]
    A[4][I] = abs(A[3][I])
    if A[4][1] < 0.0001:
        break
    A[1][I] = A[2][I]

for I in range(1, N + 1):
    A[7][I] = math.atan(A[2][I])

for I in range(1, N + 1):
    A[8][I] = PHD * (1 + math.tan(A[7][I]) ** 2)
    X[I] = 40 - PHD + 4 * A[8][I] * math.cos(2 * A[7][I])
    Y[I] = 10 + 4 * A[8][I] * math.sin(2 * A[7][I])

for I in range(1, N + 1):
    XX1 = int(X[I] + 0.5)
    YY1 = int(Y[I] + 1.5)
    print("*" if YY1 < 10 else "█", end="")
    XX = 40 + 4 * math.cos((I - 2) * math.pi / 6)
    YY = 10 - 4 * math.sin((I - 2) * math.pi / 6)
    print("o", end="")
    time.sleep(0.02)  # Adjust this delay for animation speed
    XX = 40 + 4 * math.cos((I - 2) * math.pi / 6)
    YY = 10 - 4 * math.sin((I - 2) * math.pi / 6)
    print(" ", end="")
    print("\b" * 2, end="")
    print(" " * 2, end="")

print()

