import random
import matplotlib.pyplot as plt

CONST0 = 0x5A4A  # 23114
CONST1 = 0xB753  # 46931
CONST2 = 0x0248  # 584


galaxy = []


def nipS(s):
    tmp = s[0] + s[1] + s[2]
    s[0] = s[1]
    s[1] = s[2]
    s[2] = tmp
    return s



def generate(s):
    nedoSys = [0, 0, '']
    nedoSys[0] = (s[1] >> 8) % 256
    nedoSys[1] = (s[0] >> 8) % 256
    s = nipS(s)

    return nedoSys


seed = [CONST0, CONST1, CONST2]
for i in range(0, 256):
    galaxy.append(generate(seed))

xs = range(0, 256)
color = ['black', 'red', 'green', 'yellow', 'grey', 'blue', 'orange', 'purple',
         'pink']
plt.title('Galaxy')
for i in range(0, 256):
    plt.scatter(galaxy[i][0], 256 - galaxy[i][1], c=color[random.randint(0, len(color) - 1)])
    plt.text(galaxy[i][0], 256 - galaxy[i][1], galaxy[i][2])
plt.show()
