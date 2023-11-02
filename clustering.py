data = []

lenn = int(input("Enter the length of data for clustering : "))
print("Enter the data : ")

for i in range(lenn):
    d = int(input())
    data.append(d)


nom = int(input("Enter the number of clusters u want to form : "))

means = {}

for i in range(nom):
    means.update({"m"+str(i): ""})


print("Enter the intial mean value : ")
for i in range(nom):
    mv = int(input(f'{"Mean "}{i}{" value : "}'))
    means.update({"m"+str(i): mv})


print(data)
print(means)


clusters = []

for i in range(nom):
    clusters.append([])

valcal = []
dupMeans = []


def createClus(count):

    for i in range(lenn):

        for j in range(nom):
            valcal.append(abs(data[i] - means.get("m"+str(j))))

        clusters[valcal.index(min(valcal))].append(data[i])

        valcal.clear()

    for k in range(len(clusters)):

        nm = 0

        for m in clusters[k]:
            nm = nm + m

        means.update({"m"+str(k): nm/len(clusters[k])})

        dupMeans[count].append(nm/len(clusters[k]))


dupMeans.append([])
createClus(0)
print(clusters)
for m in range(nom):
    clusters[m].clear()


dupMeans.append([])
createClus(1)
print(clusters)
for m in range(nom):
    clusters[m].clear()


while True:
    c = 2
    check = 0
    for ii in range(len(dupMeans)):
        for jj in range(ii+1, len(dupMeans)):
            if dupMeans[ii] == dupMeans[jj]:
                check = 1
            else:
                check = 0

    if check == 1:
        break
    else:
        for m in range(nom):
            clusters[m].clear()

        dupMeans.append([])
        createClus(c)
        print(clusters)
        c += 1


print("The final cluster is : ", clusters)
print("The final mean is : ", means)
