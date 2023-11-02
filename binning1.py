# data = [13, 7, 6, 21, 2, 9, 20, 30, 24]

# data.sort()

# dl = len(data)

# binsC = 3

# bins1 = []

# for i in range(0, len(data)-1, binsC):
#     l1 = []
#     for j in range(i, binsC+i):
#         l1.append(data[j])
#     bins1.append(l1)

# print(bins1)

# meanBin = []

# for i in bins1:
#     mean = sum(i)/len(i)
#     meanBin.append([round(mean, 2)]*3)

# print(meanBin)

# for bin in bins1:
#     mx = max(bin)
#     mn = min(bin)

#     for i in range(len(bin)):
#         if abs(bin[i]-mn) < abs(bin[i]-mx):
#             bin[i] = mn
#         else:
#             bin[i] = mx

# print(bins1)




dataSize = int(input("Enter the size of data set : "))

dataset = []

print("Enter data values : ")

for i in range(dataSize):
    dataset.append(int(input()))


binS = int(input("Enter the bin size : "))


print(dataSize)
print(dataset)

dataset.sort()

print(dataset)


bins = []
addrem = 0


for i in range(0, dataSize, binS):
    b = []
    for j in range(i, binS+i):
        if j>dataSize-1:
            addrem = i
            break
        else:
            b.append(dataset[j])
    bins.append(b)

# [1 2 3] [4 5 6] [7 8 9] i 10  

print(addrem)

if addrem != 0:
    bins.pop()

    for i in range(addrem, dataSize):
        bins[-1].append(dataset[i])


print(len(dataset), len(bins))

print(bins)


meanBin = []

for i in bins:
    m = []
    mean = sum(i)/len(i)
    for j in i:
        m.append(round(mean,2))
    meanBin.append(m)


print(meanBin)

for b in bins:
    mn = min(b)
    mx = max(b)

    for i in range(len(b)):
        if abs(mn-b[i]) < abs(mx-b[i]):
            b[i] = mn
        else:
           b[i] = mx


print(bins)
           
           
        

    























