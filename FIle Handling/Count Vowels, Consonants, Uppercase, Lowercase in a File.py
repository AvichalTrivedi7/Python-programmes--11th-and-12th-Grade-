def show():
    f = open('myfile.txt')
    data = f.read()
    vowel = cons = upper = lower = 0
    vowelList = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

    for i in data:
        if i.isalpha():
            if i in vowelList:
                vowel += 1
            else:
                cons += 1
            if i.isupper():
                upper += 1
            else:
                lower += 1

    print('Number of vowels:', vowel)
    print('Number of consonants:', cons)
    print('Number of uppercase letters:', upper)
    print('Number of lowercase letters:', lower)
    f.close()

show()
