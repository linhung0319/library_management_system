from enum import Enum
from abc import ABC
from unicodedata import name

class DatasetInfo():
    FILE_NAME = "./data/toy_Inventory.csv"
    COLUMNS = {
        "bibNum" : "BibNum",
        "ISBN" : "ISBN",
        "title" : "Title",
        "author" : "Author",
        "subjects" : "Subjects",
        "publisher" : "Publisher",
        "publicationYear" : "PublicationYear"
    }
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
    def __init__(self, street="", city="", state="", zip_code="", country=""):
        self.street_address = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

class BookStatus(Enum):
    AVAILABLE, REVERSED, LOANED, LOST, NONE = 1, 2, 3, 4, 5
