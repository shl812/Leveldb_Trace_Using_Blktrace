import os, sys
import csv


NAME = str(sys.argv[1])
result = open("temp.txt")
list_csv =  open("list5.csv", 'r+', encoding='utf-8', newline="")
result2 = open(NAME, 'a', encoding='utf-8', newline="")
writer = csv.writer(result2)

n_block = []
access_count = []
n_row = []
layer = []

reserved_sector = 0
fat_sector = 0
n_fat = 0
fat1_start_sector = 0
fat2_start_sector = 0
data_start_sector = 0

hex_data = result.readline()
a = hex_data.split(" ")
reserved_sector = int(int(a[16] + a[15], 16))
#print(reserved_sector)

hex_data = result.readline()
a = hex_data.split(" ")
n_fat=int(a[1])

hex_data = result.readline()
a = hex_data.split(" ")
fat_sector = int(int(a[6]+a[5], 16))
#print(fat_sector)

fat1_start_sector = reserved_sector
fat2_start_sector = (reserved_sector + fat_sector)
data_start_sector = (reserved_sector + (fat_sector * n_fat))

print(fat1_start_sector)
print(fat2_start_sector)
print(data_start_sector)

hex_print = "xxd -s 0x" + str(hex(data_start_sector*512)) + " -l 500 -g 1 /dev/ram0"
os.system("xxd -s " + str(hex(data_start_sector*512)) + " -l 500 -g 1 /dev/ram0")

while 1:
    list_data = list_csv.readline()
    if not list_data: break
    list_split = list_data.split(",")
    list_split[3] = int(list_split[3])
    if list_split[3] not in n_block:
        n_block.append(list_split[3])
        access_count.append(1)
        if (list_split[3] <= fat1_start_sector):
            layer.append(1)
        elif (fat1_start_sector <= list_split[3] < data_start_sector):
            layer.append(2)
        elif (data_start_sector <= list_split[3]):
            layer.append(3)


    else:
        array_index = n_block.index(list_split[3])
        access_count[array_index] += 1


print(len(layer))
for i in range(0, len(n_block)):
    if (layer[i] == 1):
        writer.writerow([n_block[i], access_count[i], 0, 0])
    elif (layer[i] == 2):
        writer.writerow([n_block[i], 0, access_count[i], 0])
    elif (layer[i] == 3):
        writer.writerow([n_block[i], 0, 0, access_count[i]])

result2.close()
