from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Ім'я не може бути порожнім")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Неправильний формат номеру телефону. Будь ласка, введіть 10 цифр.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError as e:
            print(e)

    def remove_phone(self, phone):
        try:
            self.phones.remove(Phone(phone))
        except ValueError:
            print("Номер телефону не знайдено.")

    def edit_phone(self, old_phone, new_phone):
        try:
            index = self.phones.index(Phone(old_phone))
            self.phones[index] = Phone(new_phone)
        except ValueError:
            print("Номер телефону не знайдено.")

    def __str__(self):
        return f"Ім'я контакту: {self.name}, телефони: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, name):
        self.data[name] = Record(name)

    def search_record(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print("Запис не знайдено.")

    def delete_record(self, name):
        try:
            del self.data[name]
            print("Запис успішно видалено.")
        except KeyError:
            print("Запис не знайдено.")

    def search_phone(self, phone):
        for record in self.data.values():
            for p in record.phones:
                if p.value == phone:
                    return record.name
        print("Номер телефону не знайдено в жодному записі.")


def main():
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
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    print("Всі записи у книзі:")
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    print("\nРедагування телефону для John:")
    john = book.search_record("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

        # Пошук конкретного телефону у записі John
        found_phone = john.find_phone("5555555555")
        if found_phone:
            print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    print("\nВидалення запису Jane:")
    book.delete_record("Jane")

if __name__ == "__main__":
    main()
