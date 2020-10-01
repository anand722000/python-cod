#this code will not print between start and end range 
def NotMe(inp, start, end):
    lis = []
    for i in inp:
        if i<start or i>end:
            lis.append(i)
    return lis


inp=list(range(1,11)) #creating list using range
start=int(input("Enter start"))
end=int(input("Enter end"))
print(NotMe(inp, start , end))

    
