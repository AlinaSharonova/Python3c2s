def write_file(file, text):
    file.write(text)

file = open( "pay.txt", 'w')
list1 = []
list2 = []

stroka = input("Введите тип транзакции и сумму: ")
while (stroka != 'quit'):
    write_file(file, stroka)
    stroka = input()


file = open("pay.txt", 'r')
for line in file:
    line.split(":")
    list1.append(line[0])
    list2.append(line[1])
    print(line)

file.close()

d = {}
d = dict.fromkeys(list1, list2)
print(d)
sum(list2)
print("Всего потрачено" + sum)