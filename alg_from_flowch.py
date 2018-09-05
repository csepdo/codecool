#numbers = [1,2,56,32,51,2,8,92,15]
#print(numbers)
while True:
    i = 1
    l = input('Please give the list of numbers you want to sort. ')
    try:
        numbers = list(map(int, l.split(',')))
        N = len(numbers)
        def rearrange():
            temp = numbers[j+1]
            numbers[j+1] = numbers[j]
            numbers[j] = temp
        while i < N:
            j = 0
            while j <= (N-2):
                while numbers[j] > numbers[j+1]:
                    rearrange()
                j += 1
            i += 1
        print(numbers)
    except ValueError:
        print('Only numbers, please!')
