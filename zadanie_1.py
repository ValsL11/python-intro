import random

list1 = [2, 1, 3, 7]
list2 = [4, 2, 0]
number = None

''' randint() is an inbuilt function of the random module in Python3. 
The random module gives access to various useful functions one of them being able to generate random numbers, 
which is randint().
https://www.geeksforgeeks.org/python-randint-function/
'''
objective = random.randint(1, 50)

'''
The zip() function returns a zip object, 
which is an iterator of tuples where the first item in each passed iterator is paired together, 
and then the second item in each passed iterator are paired together etc.
If the passed iterables have different lengths, 
the iterable with the least items decides the length of the new iterator.
https://www.w3schools.com/python/ref_func_zip.asp
'''
combined = zip(list1, list2);

'''
The print() function prints the specified message to the screen, 
or other standard output device.
The message can be a string, 
or any other object, 
the object will be converted into a string before written to the screen.
https://www.w3schools.com/python/ref_func_print.aspgit
'''
print(list(combined));

while objective != number:
    try:
        print("Podaj cyfrę od 1 do 50:")

        '''
        The input() function allows user input.
        https://www.w3schools.com/python/ref_func_input.asp
        '''
        number = int(input())
    except ValueError:
        print("Niepodano prawidłowej cyfry")
        pass

    if number > objective:
        print("Podana cyfra jest większa niż szukana")
    if number < objective:
        print("Podana cyfra jest mniejsza niż szukana")

print("Wygrałeś!");