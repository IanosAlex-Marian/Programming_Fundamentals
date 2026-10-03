# def func(a, b): 
#     if a == 10 or b == 10 or a + b == 10:
#         return True
#     else:
#         return False

# print(func(10, 6))

# def FizzBuzz():
#     for i in range(1,51):
#         if i % 3 == 0:
#             if i % 5 == 0:
#                 print("FizzBuzz", end=" ")
#             else:
#                 print("Fizz",end=" ")
#         elif i % 5 == 0:
#             print("Buzz",end=" ")
#         else:
#             print(i,end=" ")

# FizzBuzz()

# def temp_lister():
#     temp_list= []
#     while True:
#         temp= input("Please input your temperature (in celsius) or q to quit\n")
#         if temp == "q":
#             break
#         temp_list.append(float(temp))

#     print(f"Your temperatures are:{temp_list}.")
#     print(f"The maximum temperature is {max(temp_list)}.")
#     print(f"The minimum temperature is {min(temp_list)}.")
#     print(f"The average temperature is {sum(temp_list)/ len(temp_list)}")
#     print(f"The median temperature is {sorted(temp_list)[len(temp_list)//2] if len(temp_list) % 2 == 1 else (sorted(temp_list)[len(temp_list)//2]+sorted(temp_list)[len(temp_list)//2-1])/2}")
#     print(f"The temperatures in fahrenheit are: {list(map(lambda x: x * 1.8 + 32, temp_list))}")

# temp_lister()

# def string_splosion(word : str):
#     for i in range(len(word)+1):
#         print(word[:i], end= "")

# string_splosion(input("Please enter a word:\n"))

# from collections import Counter

# def word_counter():
#     text= input("Please input a sentence:\n")
#     print(Counter(text.split()).most_common()[0][0])
# word_counter()
    

# def check_anagrams(str1: str, str2: str):
#     print("They are anagrams." if sorted(str1) == sorted(str2) else "They aren't anagrams.")

# check_anagrams(input("Please enter the first string:\n"), input("Please enter the second string:\n"))


def grader():
    dictionary= {}
    while True:
        aux= input("Please enter the student and grade or done if finished:\n")
        if aux == "done":
            break
        Name, grade= aux.split()
        if Name in dictionary.keys():
            dictionary[Name].append(int(grade))
        else:
            dictionary[Name]= list(int(grade))
    
grader()