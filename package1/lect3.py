# file.txt - file with text from user
# metadata.pkl - file with the filename and the count of lines
import pickle

a = input("Введите имя файла:")
file = open(a, 'w')

def write_file(file, text):
    file.write(text)

str = input()
count = 0
while (str != 'quit'):
    write_file(file, str)
    count += 1
    str = input()

file.close()
file = open(a, 'r')
print("Содержание файла:")
for line in file:
    print(line)

file.close()

pickle_file = open('metadata.pkl', 'wb')
pickle.dump(a, pickle_file)
pickle.dump(count, pickle_file)
pickle_file.close()
pickle_file = open('metadata.pkl', 'rb')
loaded = pickle.load(pickle_file)
pickle_file.close()
print("Метаданные:", {loaded})
print("Количество строк: ", count)
