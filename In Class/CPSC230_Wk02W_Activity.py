# Class Activities + Review (Week2 Wednesday)

# Classwork-----------------------------------------------

'''
1.  The code below calculates the area of a triangle. Add comments to each
    line explaining what it is doing.
'''
print("--- Problem 1 ---") # print's problem number

b = 10 # sets the triangle base (b) as 10
h = 3 # sets the triangle height (h) as 3

x = b * h # multiplies base (b) times height (h)

area = x/2 # divides the previous calculation (x) by two

print(area) # prints triangle's area


'''
2.  What type is x? Add a line of code that tells the user the type in 
    the termial.
'''
print("--- Problem 2 ---")

x = 10

print(type(x))


'''
3.  The == is the "equal to" operator. It returns True if two objects are 
    equal, and False if they are not (see below for examples). Add a line 
    of code to check if the Boolean "True" is equal to 1. Display the result.
'''
print("--- Problem 3 ---")
# examples
1 == 2 # False
3 <= 10 # True

print(True == 1)


'''
4. Print the type of each of these variables.
'''
print("--- Problem 4 ---")

my_int = 9
my_string = "quod erat demonstrandum"
my_list = [1,2,3,4,5]
my_dict = {"name": "Jessie", "age": 27, "team": "Rocket"}
my_set = {1,1,2,3,5,8,13}

print(type(my_int))
print(type(my_string))
print(type(my_list))
print(type(my_dict))
print(type(my_set))


'''
5.  Write some code that uses a boolean operator to check whether
    7 * 2 + 4 / 9 is bigger than 9 * 10 / 2 + 3 - 4 and displays 
    the result.
'''
print("--- Problem 5 ---")

x = 7 * 2 + 4 / 9
y = 9 * 10 / 2 + 3 - 4

print(x == y)

