# ctrl+P - подсказка
# alt+enter - как надо писать

a = [] #список
n = 7
nums = []
for i in range(n):
    nums.append(i)
print(nums)

i = 0
while i < 7:
    for j in reversed(range(1, n)):
        num1 = nums[j]
        num2 = nums[j-1]
        nums[j] = num2
        nums[j-1] = num1
        print(nums)
        a.append(nums[::])
    i = i + 1
a.sort()
b = list(a) # для исключения повторов
print(b)