
st = 'Never Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you'
print(st)


def frequency(str):

    def calculates(arg1):
        counter = {}

        for word in str.split(" "):
            counter[word] = counter.get(word, 0) + 1

        counter_list = counter.keys()

        for words in counter_list:
            print(words, counter[words])
        return counter

    m = max(calculates(str), key=calculates(str).get)
    return print ("The most popular word is " + m)

frequency(st)