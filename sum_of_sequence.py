class sum_of_sequence():
    sum = 0
    def geometric(self, sequence):
        n = len(sequence)
        a1 = sequence[0]
        q = sequence[1]/a1
        if q == 1:
            sum = n * a1
        else :
            sum = a1 * (1-q**n)/(1-q)
        return sum

    def arytmetic(self, sequence):
        n = len(sequence)
        a1 = sequence[0]
        r = sequence[1] - a1
        an = a1 + (n-1) * r
        sum = (a1 + an)/2 * n
        return sum
    
    def any_seqence(self, sequence):
        sum = 0
        for i in sequence:
            sum += i
        return sum

def type_of_sequence(sequence,a):
    n = len(sequence)
    for i in range(n - 2):
        if sequence[i+1] - sequence[i] == sequence[i+2] - sequence[i+1]:
            a = 'arytmetic'
        elif sequence[i+1]/sequence[i] == sequence[i+2]/sequence[i+1] and a != 'arytmetyczny':
            a = 'geometric'
        else :
            a = 'any_seqence'
            break
    return a

sum_of_sequence = sum_of_sequence()

sequence = []
type_of_sequence = type_of_sequence(sequence,'')

if type_of_sequence == 'arytmetic':
    print(sum_of_sequence.arytmetic(sequence))
elif type_of_sequence == 'geometric':
    print(sum_of_sequence.geometric(sequence))
elif type_of_sequence == 'any_seqence':
    print(sum_of_sequence.any_seqence(sequence))