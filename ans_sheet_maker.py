filename = input("filename: ")
number = input("Number of question: ")

with open(filename+".txt", 'w+') as f:
    for i in range(1, int(number) + 1):
        f.write(str(i) + '. \n')
