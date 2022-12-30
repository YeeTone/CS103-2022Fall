import numpy as np

a = np.arange(1, 10)
a = a.reshape((3, 3))
a = a.T

b = np.array([[-1, -2, -1],
              [0, 0, 0],
              [1, 2, 1]])

b = b.T

c = np.zeros((3, 3))

for i in range(3):
    for j in range(3):
        tmp = 0
        for i_ in range(-1, 2):
            for j_ in range(-1, 2):
                shift_i = i - i_
                shift_j = j - j_

                a_ = a[shift_j][shift_i] \
                    if (shift_i in range(3) and shift_j in range(3)) \
                    else 0
                b_ = b[j_ + 1, i_ + 1]
                tmp += a_ * b_
        c[i, j] = tmp

print(c)
