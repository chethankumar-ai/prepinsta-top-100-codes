def fact(num):
    if num==0 or num ==1:
        return 1
    return num*fact(num-1)
var=map(fact,range(10))
print(list(var))