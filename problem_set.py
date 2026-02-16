
#1
def count_up(n):
    counter = 1
    while counter <= n:
        yield counter 
        counter += 1

for num in count_up(5):
    print(num)

#2
def evens(n):
    counter = 1
    while counter <= n:
        if counter%2==0:
            yield counter
        counter += 1
print(list(evens(10)))

#3
gen = count_up(3)
print(next(gen)) # each line will result in the equivalent of each round in a for loop 
print(next(gen)) # 
print(next(gen)) #
print(next(gen)) # raises a StopIteration

#4
def digits(n):
    n = str(n)
    num_of_dig = len(n)
    while num_of_dig > 0:
        yield int(n[num_of_dig-1])
        num_of_dig -= 1

print(list(digits(4827)))

#5
def count_from(n):
    while True:
        yield n
        n += 1

gen = count_from(10)
print(next(gen)) # 10
print(next(gen)) # 11
print(next(gen)) # 12

#6
def fibonacci():
    num1= 0 
    num2 = 1
    yield num1
    yield num2
    while True:
        yield num1 + num2
        temp = num1
        num1 = num2
        num2 = num2 + temp

fib = fibonacci()
for _ in range(8):
    print(next(fib), end=" ")

#7
def take(rounds,fun_name):
    while rounds > 0:
        yield next(fun_name)
        rounds -= 1

print(list(take(5, fibonacci())))
print(list(take(3, count_from(100))))

#8
def even_num_square(num_list):
    for num in num_list:
        if num%2==0:
            yield num**2

print(sum(even_num_square([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

#9
def read_lines(file):
    with open(file,"r") as f:
        while True:
            row = f.readline().strip()
            if not row:
                break
            yield row


for line in read_lines("data.txt"):
    print(line)

#10
def is_prime(num):
    if num%2==0 and num != 2:
        return False
    temp = 2
    while temp < num:
        result = num/temp
        if result%1==0 and num != 2 :
            return False
        temp += 1
    return True

def primes():
    counter = 1
    while True:
        if is_prime(counter):
            yield counter
        counter += 1
print(list(take(10, primes())))

#11
def sliding_window(data,window_size):
    counter = 0 
    index = 0
    num_list = []
    while index+window_size <= len(data):
        while counter < window_size:
            num_list.append(data[index+counter])
            counter += 1
        yield num_list 
        counter = 0
        index += 1
        num_list = []
data = [1, 2, 3, 4, 5, 6]
print(list(sliding_window(data, 3)))
print(list(sliding_window(data, 2)))