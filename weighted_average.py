import os
from time import sleep
points = 0
sum_of_evaluations = 0
def weighted_average(points, sum_of_evaluations):

    i = input('Do you want to continue? [yes, no]\n')
    os.system('cls')

    if i.replace(" ", "").lower() not in ['yes', 'no']:
        print('Please give me good answer...')
        os.system('cls')
        weighted_average(points,sum_of_evaluations)

    elif i.replace(" ", "").lower() != 'no':
        ocena = input('Provide rating\n')
        os.system('cls')
        waga = input('podaj wagę oceny\n')
        points += float(waga)
        sum_of_evaluations += float(waga) * float(ocena)
        os.system('cls')
        weighted_average(points, sum_of_evaluations)
        
    elif i.replace(" ", "").lower() == 'no':
        os.system('cls')
        print(sum_of_evaluations/points)
