
# Write your solution here:

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name :str, number : str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
            
        self.__persons[name].add_number(number)
    
    def add_address(self, name :str, address : str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        
        self.__persons[name].add_address(address)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].numbers()

    def address(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].address()

    def all_entries(self):
        toPrint = ""
        for key, values in self.__persons.items():    
            toPrint += f"{key}, {values.numbers()} \n"         
        return toPrint.strip()

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")
    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_entry(name)
        address = self.__phonebook.address(name)        
        if numbers:
            for number in numbers:
                print(number)       
        else:
            print("number unknown")
        if address == None:
            print("address unknown")
        else:
            print(address)
       

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()
class Person:
    def __init__(self, name: str):
        self._name = name
        self._address = ""
        self._numbers = []

    def add_address(self, address : str):
        self._address = address

    def add_number(self, number: str):
        self._numbers.append(number)
    
    def name(self):
        return self._name

    def address(self):
        if self._address == "":
            return None
        else: 
            return self._address

    def numbers(self):
        return self._numbers


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

