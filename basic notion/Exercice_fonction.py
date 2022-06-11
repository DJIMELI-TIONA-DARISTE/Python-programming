def mutiplicationTable(n,min=1, max=10):
    if min > max:
        print("min must be lower than max")
        return
    for i in range(min, max+1):
        print(i, "x", n, "=", n*i)
        
mutiplicationTable(5,5,2)