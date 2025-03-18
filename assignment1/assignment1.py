# Write your code here.
# Task 1
def hello():
    return "Hello!"
print(hello())

# Task 2
def greet(name):
    return f"Hello, {name}!"
print(greet("Stetchi"))

#Task 3

def calc(x, y, operation="multiply"):     
    try:
     if operation == "add":
         return x + y
     elif operation == "subtract":
        return x - y
     elif operation == "multiply":
            return x * y
     elif operation == "divide":
            return x / y    
     elif operation == "modulo":
        return x % y
     elif operation == "int_divide":
        return x // y
     elif operation == "power":
        return x ** y
     else:
        return "invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    finally:
       print("Calculation finished")
result = calc(5,3,"add")     
print(result)  

# The same task with match-case
# Task 3
# def calc(x, y, operation="multiply"):
#     try: 
#      match operation:
#             case "add":
#              return x + y
#             case "subtract":
#              return x - y
#             case "multiply":
#              return x * y
#             case "divide":
#              return x / y
#             case "modulo":
#              return x % y
#             case "int_divide":
#              return x // y
#             case "power":
#              return x ** y
#             case _:
#              return "Invalid operation"
#     except ZeroDivisionError:
#         return "You can't divide by 0!"
#     except TypeError:
#         return "You can't multiply those values"

# Task 4
def data_type_conversion(value, data_type):
    try:
        if data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        elif data_type == "int":
            return int(value)
        else:
            return f"Invalid data type: {data_type}."
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
    finally:
        print("Conversion finished")  

# Task 5
def grade(*args):
    try:
        if not args:
            return "No grades provided"
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise ValueError("Invalid data was provided.")
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except ValueError:
        return "Invalid data was provided."

    finally:
        print("Finished")

#  Task 6       
def repeat (string, count):
    result = ""
    for i in range(count):
        result += string
    return result 
#Task 7
def student_scores(type, **kwargs):
    if not kwargs:
        return None
    if type == "best":
        return max(kwargs, key=kwargs.get)
    elif type == "mean":
        return sum(kwargs.values()) / len(kwargs)
    else:
        raise ValueError("Invalid option. Use 'best' or 'mean'.")

# Task 8
def titleize(str):
    little_words = {"a", "on", "an", "the", "of", "and", "is","in"}
    words = str.split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()
    
    return " ".join(words)

# Task 9
def hangman(secret, guess):
    result = ""
    for i in list(secret):
        if i in guess:
            result +=i
        else: result += "_"
    return result        

# Task 10
def pig_latin(sentence):
    result = ""
    for word in sentence.split(" "): 
        if word[0] in "aeiou":  
            result += word + "ay"  
        elif word[0:2] == "qu":  
            result += word[2:] + "quay"  
        else:
            i = 0
            while word[i] not in "aeiou": 
                i += 1
            if word[i - 1:i + 1] == "qu":  
                result += word[i + 1:] + word[:i + 1] + "ay" 
            else:
                result += word[i:] + word[:i] + "ay"  
        result += " "
    
    return result.strip()  

print(pig_latin("apple"))