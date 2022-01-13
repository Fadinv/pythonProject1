import math

# ЗАДАНИЕ 1
print('1 число')
a = int(input())
print('2 число')
b = int(input())
print('3число')
c = int(input())
print('4 число')
d = int(input())

p = (c / a) - (b**2 / ((a**2) * 3))
q = ((2 * b**3) / (27 * a**3)) - ((b * c) / (3 * a**2)) + (d / a)
Q = (p / 3)**3 + (q / 2)**2
al = (- (q / 2) + math.sqrt(Q))**(1 / 3)
bt = (- (q / 2) - math.sqrt(Q))**(1 / 3)

res1 = al + bt
res2 = - ((al + bt) / 2) + 3 * ((al - bt) / 2)
res3 = - ((al + bt) / 2) - 3 * ((al - bt) / 2)

print(f'Результаты кубического уравнения: 1-ый корень-{res1}, 2-ой корень-{res2} * i, 3-ий корень-{res3} * i.')


# ЗАДАНИЕ 2
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.array([0, 2, 1, 3], dtype=float)
# y = np.array([0, 1, 2, 3], dtype=float)
#
#
# def lagranz(x, y, t):
#     z = 0
#     for j in range(len(y)):
#         p1 = 1
#         p2 = 1
#         for i in range(len(x)):
#             if i == j:
#                 p1 = p1 * 1
#                 p2 = p2 * 1
#             else:
#                 p1 = p1 * (t - x[i])
#                 p2 = p2 * (x[j] - x[i])
#         z = z + y[j] * p1 / p2
#     return z
#
#
# xnew = np.linspace(np.min(x), np.max(x), 100)
# ynew = [lagranz(x, y, i) for i in xnew]
# plt.plot(x, y, 'o', xnew, ynew)
# plt.grid(True)
# plt.show()
