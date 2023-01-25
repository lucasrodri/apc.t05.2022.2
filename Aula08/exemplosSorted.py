numbers = [4, 2, 12, 8]

sorted_numbers = sorted(numbers,reverse=True)

print(sorted_numbers)

# vowels list
py_list = ['e', 'a', 'u', 'o', 'B', 'i']
print(sorted(py_list))

# string
py_string = 'Python'
print(sorted(py_string))

# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple))

# dictionary
py_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(py_dict, reverse=True))
print(sorted(py_dict))


# take the second element for sort
def take_second(elem):
    return elem[1]
# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# sort list with key
sorted_list = sorted(random, key=take_second)
# print list
print('Sorted list:', sorted_list)
