x1 = int(input())
x2 = int(input())

def euclidean_algorithm_with_recursion(x1,x2):
  rest = x1%x2
  if rest == 0:
    return x2
  else :
    return euclidean_algorithm_with_recursion(x2,rest)

a = int(input('prosze podac liczbe a ='))
b= int(input('prosze podac liczbe b ='))

def euclidean_algorithm_with_substraction(a,b):
  while a != b:
    if a > b:
      a -= b
    else :
      b -= a
  return a
