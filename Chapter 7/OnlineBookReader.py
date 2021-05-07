class OnlineBookReader:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.reading = {}

    def add_book_to_library(self, book):
        self.books.append(book)
        print(book.name, 'was added to our online library ...')

    def assign_user_to_book(self, book, user):
        book_in_use = self.reading.values()
        if book in book_in_use:
            print(book.name, 'is already assigned to other user ... please try another book')
        else:
            self.reading[user] = book
            print(user.username, 'was assigned to the book:', book.name)


class Book:
    def __init__(self):
        self.name = None
        self.ISBN = None
        self.author = None

    def create_book(self, name, ISBN, author):
        self.name = name
        self.ISBN = ISBN
        self.author = author
        print('Book:', self.name, 'with Author: ', author.name, 'was registered ...')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Author(Person):
    pass


class User(Person):
    def __init__(self):
        self.username = None
        self.password = None

    def create_user(self, username, password):
        self.username = username
        self.password = password
        print('User:', self.username, 'was created ...')


user1 = User()
user1.create_user('Admin', 1234)
user2 = User()
user2.create_user('Moderator', 'abcd')
author = Author('James Rallison', 20)
print()
book1 = Book()
book1.create_book('The First Sequel', 12345, author)
book2 = Book()
book2.create_book('How to be cool', 12346, author)
book3 = Book()
book3.create_book('The Odd 1s Out', 12347, author)
print()
online_book_reader = OnlineBookReader('My Online Library')
online_book_reader.add_book_to_library(book1)
online_book_reader.add_book_to_library(book2)
online_book_reader.add_book_to_library(book3)
print()
online_book_reader.assign_user_to_book(book1, user1)
online_book_reader.assign_user_to_book(book1, user2)
online_book_reader.assign_user_to_book(book2, user2)