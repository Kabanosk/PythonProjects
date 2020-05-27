class MegaProjectIdeasList():
    def reverse_a_string(self, string):
        reversedString = ''
        for i in range(len(string)-1,-1,-1):
            reversedString += string[i]
        return reversedString

    def pig_latin(self, string):
        if string[0].lower() in ['a','e','i','o','u']:
            return string + 'way'
        else :
            for i in range(0,len(string),1):
                if string[i] in ['a','e','i','o','u']:
                    return string[i:] + string[:i] + 'ay'
                    
    def count_vowels(self,string):
        numberOfVowels = 0
        numberOfA = 0
        numberOfE = 0
        numberOfI = 0
        numberOfO = 0
        numberOfU = 0
        for i in string:
            if i == 'a':
                numberOfA += 1
                numberOfVowels += 1
            if i == 'e':
                numberOfE += 1
                numberOfVowels += 1
            if i == 'i':
                numberOfI += 1
                numberOfVowels += 1
            if i == 'o':
                numberOfO += 1
                numberOfVowels += 1
            if i == 'u':
                numberOfU += 1
                numberOfVowels += 1
        return f'a: {numberOfA}, e: {numberOfE}, i: {numberOfI}, o: {numberOfO}, u: {numberOfU}, all: {numberOfVowels}'

    def count_words_in_string(self, string):
        numbersOfWords = 1
        for i in range(0,len(string),1):
            if string[i] == ' ' and string[i+1] != ' ':
                numbersOfWords += 1
        return numbersOfWords

    def check_if_palindrome(self, string):
        reversedString = ''
        for i in range(len(string)-1,-1,-1):
            reversedString += string[i]
        if string == reversedString:
            return True
        else :
            return False

MegaProjectIdeasList = MegaProjectIdeasList()

print(MegaProjectIdeasList.check_if_palindrome('kajak'))
