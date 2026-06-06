file_path = "main.txt"
file = open(file_path, 'r')

content = file.read()
print(content)

'''
with open("main.txt", "w") as file:
    file.write('Sot eshte dite e mire dite e zotit')

'''


line = ['Hello World \n', 'Digital School \n']
with open('main.txt','w') as file:
    file.writelines(line)