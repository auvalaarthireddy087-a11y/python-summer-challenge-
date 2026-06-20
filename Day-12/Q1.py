n = [23,45,6,21,90,2]
for i in range(len(n)):
    ind = i
    for j in range(i + 1, len(n)):
        if n [j] < n [ind]:
            ind = j
            n[i],n[ind]= n[ind], n[i]
            print("the selection sort:",n)
            
