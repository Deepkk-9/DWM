graph = [[0, 1, 1, 0],
         [0, 0, 0, 1],
         [1, 1, 0, 1],
         [0, 0, 1, 0]]
         
pr = [1/len(graph[0])] * len(graph)

beta = 0.8

def calcPr():
    tempPr = []
    for i in range(len(graph)):
        temp = 0
        inbounds = getInbounds(i)
        for inbound in inbounds:
            # print('Inbound: ', inbound, 'Pr[in]: ', pr[inbound], 'Outbounds: ', countOutbounds(inbound))
            temp += pr[inbound]/countOutbounds(inbound)
        temp = (1-beta) + beta * temp
        tempPr.insert(i, temp)
    return tempPr

def getInbounds(n):
    inbounds = []
    for i, link in enumerate(graph):
        if link[n] == 1:
            inbounds.append(i)
    return inbounds

def countOutbounds(n):
    count = 0
    for i in graph[n]:
        if i == 1:
            count += 1
    return count

for i in range(3):
    print('\nIteration', i)
    for i in range(len(pr)):
        print(f'Page Rank of Node{i}: {pr[i]:.2f}')
    pr = calcPr()
