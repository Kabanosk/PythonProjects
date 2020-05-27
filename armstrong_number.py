def armstrong_number(n):
    array =[]
    a = 0
    for i in str(n):
        array.append(i)
    for i in array:
        a += int(i)**len(str(n))
    if a == n:
        return True
    else :
        return False

print(armstrong_number(2248))