import matplotlib.pyplot as plt
from random import randint


def gen():
  orig = [[randint(0, 1) for j in range(5)] for i in range(5)]
  fig, ax = plt.subplots()
  ax.imshow(orig + orig[::-1])
  plt.show()


def genFor(x):
  for i in range(x):
    gen()


genFor(5)
