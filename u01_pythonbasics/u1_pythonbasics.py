name = "jiajie"
school = "JSS"
hobby = "gaming"
print("my name is {} and i am from {} and i like {} ".format(name,school,hobby))
print(f"my name is {name} and i am from {school} and i like {hobby} ")


#simple math 
x = 50
y = 10
print(f"addition {x + y}")
print(f"division {x // y}")
print(f"multiplication {x * y}")
print(f"subtraction {x - y}")
print(f"power {x**y}")

for i in range(5): 
    expressway = input("Enter name of gantry:") 
    old = float(input("Enter old rate:")) 
    new = float(input("Enter new rate:")) 
    change = new - old 
    print("Change is",change)