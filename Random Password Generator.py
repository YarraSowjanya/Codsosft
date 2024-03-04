import string
import random

if __name__ == "__main__":
    a = string.ascii_uppercase
    #print(a)
    b = string.ascii_lowercase
    #print(b)
    c = string.digits
    #print(c)
    d = string.punctuation
    #print(d)
    password_length = int(input("Enter your password length: "))
    s = []
    s.extend(a)
    s.extend(b)
    s.extend(c)
    s.extend(d)
    #print(s)
    random.shuffle(s)
    #print(s)
    print("Your Password is: ","".join(s[0 : password_length]))

