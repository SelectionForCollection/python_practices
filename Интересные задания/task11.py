import csv
from matplotlib import pyplot as plt

with open(
        'D:/PyCharm projects/playground/venv/Lib/site-packages/data/GAMES.csv',
        encoding='utf8') as f:
    arr = list(csv.reader(f, delimiter=';'))

arr_data_full = []
arr_sum = []
arr_sum_1 = []
arr_janr = []
for i in range(0, len(arr)):
    arr_janr.append(arr[i][1])
    if not arr[i][3] == 'не издана':
        arr_data_full.append(int(arr[i][3]))

arr_data_uniq = list(set(arr_data_full))
arr_janr_uniq = list(set(arr_janr))
print(arr_data_uniq)
print(arr_janr_uniq)

for i in range(0, len(arr_data_uniq)):
    flag = arr_data_uniq.__getitem__(i)
    arr_sum.append(arr_data_full.count(flag))

for i in range(0, len(arr_janr_uniq)):
    flag = arr_janr_uniq.__getitem__(i)
    arr_sum_1.append(arr_janr.count(flag))

plt.bar(arr_data_uniq, arr_sum)
plt.show()

plt.bar(arr_janr_uniq, arr_sum_1)
plt.show()
