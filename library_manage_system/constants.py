from enum import Enum
from abc import ABC
from unicodedata import name

class LibraryRule():
    MAX_BOOKS_ISSUED_TO_A_USER = 5
    MAX_LENDING_DAYS = 10
class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5

class Person():
    def __init__(self, name, address='', email='', phone=''):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone

class Address():
    def __init__(self, street, city, state, zip_code, country):
        self.street_address = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

class BookStatus(Enum):
    AVAILABLE, REVERSED, LOANED, LOST, NONE = 1, 2, 3, 4, 5

class BookFormat(Enum):
    HARDCOVER, PAPERBACK, AUDIOBOOK, EBOOK = 1, 2, 3, 4
    NEWSPAPER, MAGAZINE, JOURNAL, NONE = 5, 6, 7, 8

class BookInfo():
    def __init__(self, authors: list, ISBN='', 
                 title='', subject='', publisher='', 
                 language='', numberOfPages=0):
        self.authors = authors
        self.ISBN = ISBN
        self.title = title
        self.subject = subject
        self.publisher = publisher
        self.language = language
        self.numberOfPages = numberOfPages

class BookItemInfo():
    def __init__(self, barcode='', isReferenceOnly=False, 
                 borrowed=None, dueDate=None, price=0, 
                 dateOfPurchase=None, publicationDate=None,
                 bookFormat: BookFormat=BookFormat.NONE, 
                 bookStatus: BookStatus=BookStatus.NONE):
        self.barcode = barcode
        self.isReferenceOnly = isReferenceOnly
        self.borrowed = borrowed
        self.dueDate = dueDate
        self.price = price
        self.dateOfPurchase = dateOfPurchase
        self.publicationDate = publicationDate
        self.bookFormat = bookFormat
        self.bookStatus = bookStatus

class Rack():
    def __init__(self, number=0, locationIdentifier=''):
        self.number = number
        self.locationIdentifier = locationIdentifier
