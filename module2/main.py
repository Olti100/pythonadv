#tuple
fruits1 = ['apple', 'date', 'banana', 'elderberry']
print(fruits1[0])

words = ('spam', 'eggs', 'sausages',)
print(words)

person = ("Alice", 30, "engineer")
name, age, profession = person
print(name , "'s", "profession is", profession, "and she is", age, "years old")

dog = ("Bosley", 8, "funny")
name, age, charectiristic = dog
print(name,"'s", 'age is', age, "and he is very", charectiristic)

#dictionaries
my_dictionary={
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3",
}

contact_info={
    "Alice" : "555-1234",
    "Bob" : "555-4567",
}

alice_phone = contact_info["Alice"]
print(alice_phone)

contact_info ["Alice"] = "555-4321"
contact_info["Eve"] = "555-9999"

del contact_info["Bob"]
print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)

contact_information={
    "Alice" :{
        "phone_number" : "555-3245",
        "email" : "alice@gmail.com",
        "home_address"  : "123 Main St, Cityville",
        "birthday"  : 2/11/2000
    },
    "Bob": {
        "phone_number": "555-3267",
        "email": "bob@gmail.com",
        "home_address": "123 Main St, Cityville",
        "birthday": 1/ 11 / 2000
    },
    "Eve": {
        "phone_number": "555-6967",
        "email": "eve@gmail.com",
        "home_address": "123 Main St, Cityville",
        "birthday": 3 / 11 / 2000
    }

}
print(contact_information)

bob_information = contact_information["Bob"]
print(bob_information)

#challenge
jane_contact = {
    'name' : 'Jane',
    'phone' : '123-456',
    'email' : 'jane@gmail.com'
}
john_contact = {
    'name' : 'John',
    'phone' : '124-567',
    'email' : 'john@gmail.com'
}

contacts = {
    'Jane' : jane_contact,
    'John' : john_contact
}

print(jane_contact)

contacts['Jane']['phone'] = '111-222'

print("\nJane's update contact information:")
print(contacts['Jane'])

#tuples in dictionaries

grades ={
    ("John", "Math") : 5,
    ("Alice", "Biology") : 4,
    ("Bob", "Physics")  : 3.5,
    ("John", "Music") : 5,
    ("Eve", "English") : 4
}

john_math = grades[("John", "Math")]
print("John's garde in math is", john_math)

grades[("Bob", "Math")]= 3
print(grades)

keys= list(grades.keys())

student ,subject = keys[0]
print(student,"'s grade in", subject, "is", john_math)

#challenge2

books = {
    ("1984", 'George Orwell') : "Dystopian",
    ("To kill a Mockingbird", 'Harperlee') : "Classic",
    ("The Great Gatsby", 'F. Scott Fitzgerald') : "Classic",
}

books[("Brave New World", "Aldous Huxley")]="Dystopian"

book_info = books[("1984", 'George Orwell')]
print("1984's genre", book_info)

book_info=books[("Brave New World", "Aldous Huxley")]
print("Brave New World's genre:", book_info)