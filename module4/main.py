names = ["Alex", "John", 'Alice', "Ron"]
for emri in names:
    print(emri)

sentence = "Hello, World"
for characters in sentence:
    if characters.isalpha():
        print(characters)

range(1,10)

my_numbers = [12,45,6,72,21,8,94,57]
maximum = my_numbers[0]

for num in my_numbers:
    if num>maximum:
        maximum = num
print(f'the maximum number is {maximum}')

emrat = ["Andi", "Anda", "Beni" ,"Bujari", "Donati", "Lea"]
target = "Bujari"

for emratt in emrat:
    print(emratt)
    if target==emratt:
        print("Target Found")
        break