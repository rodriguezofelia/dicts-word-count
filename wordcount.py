# put your code here.

def word_count(filename):

    poem = open(filename)

    word_count = {}

    for line in poem:
        line = line.rstrip()
        words = line.split(' ')


        for word in words:
            if word in word_count:
                word_count[word] += 1
            else: 
                word_count[word] = 1

    return word_count

word_count("test.txt")