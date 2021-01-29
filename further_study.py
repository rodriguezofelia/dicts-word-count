import sys

def word_count(filename):

    poem = open(filename)

    word_count = {}

    for line in poem:
        line = line.rstrip()
        words = line.split(' ')


        for word in words:
            word = word.strip(",.!?-#&()%@*/:$;.""")
            word = word.lower()

            if word in word_count:
                word_count[word] += 1
            else: 
                word_count[word] = 1

    for key, value in word_count.items():
        print(key, value)
    
    return word_count

# get filename from the command line
file = sys.argv[1]

word_count(file)