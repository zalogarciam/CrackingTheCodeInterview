
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        
class Animal:
    def __init__(self, name, type, order):
        self.name = name
        self.type = type
        self.order = order

    def setOrder(self, order):
        self.order = order

    def getOrder(self):
        return self.order

    def get_type(self):
        return self.type

    def print_animal(self):
        res = 'Name: ' + self.name + ' Type: ' + str(self.type) + ' Order: '+ str(self.order) + '\n'
        return res



class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        current = self.head
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            while current.next != None:
                current = current.next
            current.next = node

    def print_list(self):
        current = self.head
        show =  ""
        while current != None:
            show += str(current.data) + " "
            current = current.next
        print(show)

    def remove(self, data):
        current = self.head
        if self.head == data:
            self.head = None
        else:
            while current.next != None:
                if current.next.data == data:
                    current.next = current.next.next
                else:
                    current = current.next


class AnimalQueue:
    def __init__(self):
        self.dogs = LinkedList()
        self.cats = LinkedList()

    def get_head_of_types(self):
        if self.dogs.head == None and self.cats.head == None:
            return None
        if self.dogs.head == None:
            return self.cats.head
        elif self.cats.head == None:
            return self.dogs.head
        else:
            if self.dogs.head.data.getOrder() > self.cats.head.data.getOrder():
                return self.cats.head
            else:
                return self.dogs.head

    def enqueue(self, animal):
        if animal.type == 'Cat':
            self.cats.add(animal)
        elif animal.type == 'Dog':
            self.dogs.add(animal)

    def print_list(self):
        current_dog = self.dogs.head
        show_dog = ""
        while current_dog != None:
            dog = current_dog.data
            show_dog += dog.print_animal()
            current_dog = current_dog.next

        current_cat = self.cats.head
        show_cat = ""
        while current_cat != None:
            cat = current_cat.data
            show_cat += cat.print_animal()
            current_cat = current_cat.next

        print(show_dog)
        print(show_cat)

    def dequeueAny(self):
        head = self.get_head_of_types()
        if head == None:
            print('Shelter is empty')
        else:
            if 'Cat' == head.data.get_type():
                self.dequeueCat()
            else:
                self.dequeueDog()

    def dequeueDog(self):
        current = self.dogs.head
        self.dogs.head = self.dogs.head.next
        self.dogs.remove(current)

    def dequeueCat(self):
        current = self.cats.head
        self.cats.head = self.cats.head.next
        self.cats.remove(current)


animalShelter = AnimalQueue()
animal = Animal('Raul', 'Cat', 1)
animal2 = Animal('Richard', 'Dog', 2)
animal5 = Animal('Ger', 'Dog', 3)
animal6 = Animal('Tod', 'Dog', 4)
animal3 = Animal('Maria', 'Cat', 5)
animal4 = Animal('Pepe', 'Cat', 6)
animalShelter.enqueue(animal)
animalShelter.enqueue(animal2)
animalShelter.enqueue(animal3)
animalShelter.enqueue(animal4)
animalShelter.enqueue(animal5)
animalShelter.enqueue(animal6)

animalShelter.dequeueDog()

animalShelter.dequeueAny()
animalShelter.print_list()