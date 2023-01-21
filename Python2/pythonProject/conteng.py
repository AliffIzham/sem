var = 0
x = []

while var != "STOP":
    var = input("enter smtg: ")
    if var == "STOP":
        break
    else:
        x.append(var)

print(x)