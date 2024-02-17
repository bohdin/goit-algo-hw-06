from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, value):
        # Перевірка, чи довжина номеру телефону дорівнює 10
        if len(value) == 10:
            super().__init__(value)
        else:
            raise(ValueError) # Викидаємо виняток, якщо номер не має 10 символів
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # Додаємо телефон до списку
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    # Видаляємо телефон зі списку, якщо він співпадає з переданим значенням
    def remove_phone(self, rem_phone: str):
        self.phones = [phone for phone in self.phones if str(phone) != rem_phone]

    # Замінюємо старий номер на новий, якщо він співпадає з переданим значенням
    def edit_phone(self, old_phone, new_phone):
        self.phones = [phone if str(phone) != old_phone else Phone(new_phone) for phone in self.phones]
    
    # Пошук телефону у списку
    def find_phone(self, f_phone):
        for phone in self.phones:
            if str(phone) == f_phone:
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    # Додаємо запис у телефонну книгу
    def add_record(self, record):
        self.data[record.name] = record
    
    # Пошук запису по імені
    def find(self, name):
        for key in self.data.keys():
            if str(key) == name:
                return self.data[key]

    # Видаляємо запис з телефонної книги по імені
    def delete(self, name):
        for key in self.data.keys():
            if str(key) == name:
                return self.data.pop(key)
         
     

if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_phone("1111111111")
    print(jane_record)
    # Видалення телефону
    jane_record.remove_phone("1111111111")
    print('-' * 20)
    print(jane_record)
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    print('-' * 20)
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print('-' * 20)
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print('-' * 20)
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
    print('-' * 20)
    for name, record in book.data.items():
        print(record)   