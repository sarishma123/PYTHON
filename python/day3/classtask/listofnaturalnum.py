# 1n.1
numbers = list(range(1, 11))
print(numbers)

# qn.2
# for add
list2 = [1,2,3,4]
list3 = [5,6,7,8]
list4 = list2 + list3
print(list4)

# for average
total = sum(list4)
num= len(list4)
average = total / num if num > 0 else 0
print(f"Average: {average}")



# qn.3smallest and largest

numbers = [4, 10, -2, 33, 7]

largest = max(numbers)
smallest = min(numbers)

print("Largest:", largest)
print("Smallest:", smallest)


# qn.4..odd and even number
numbers = [4, 10, -2, 33, 7, 8, 15]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)



# qn.5 remove duplicate from list
numbers = [1, 2, 2, 3, 4, 4, 5]
a= list(set(numbers))
print(a)



# qn.6..reverse a li st without using list
arr = [1, 2, 3, 4, 5]

rev = []
for i in range(len(arr) - 1, -1, -1):
    rev.append(arr[i])

print(rev)