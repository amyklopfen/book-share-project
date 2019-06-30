browsing = True 
#install this for Google API: pip install -U google-api-python-client
import os
import json
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import * # info drawn from send notification exercise.
import datetime

import requests 
import apiclient
from apiclient import discovery

load_dotenv()

import pprint

GOOGLE_BOOKS_API_KEY = os.environ.get("GOOGLE_BOOKS_API_KEY")

def remove_verify(book_name):
    for i in list_of_books:
        if i['title'] == book_lookup:
            list_of_books.remove(i)
            p = "Here is your new list" + str(list_of_books)
        else: 
            p = "Sorry, that title is not on your shelf!"
    return p



user_libraries = [{"user": "amyklopfen", "library": [{"author":"Sanderson", "title":"The Way of Kings", "genre":"sci-fi"}, 
{"author":"Tolkein", "title":"The Hobbit", "genre":"Young Adult Fiction"},
{"author":"Sanderson", "title":"The Hero of the Ages", "genre":"Fiction"},
{"author":"Flynn", "title":"Gone Girl", "genre":"Fiction"},
{"author":"Altwater-Rhodes", "title":"Hawksong", "genre":"Young Adult Fiction"},
{"author":"Hanley", "title":"The Seer and the Sword", "genre":"Young Adult Fiction"},
{"author":"Tolkein", "title":"The Fellowship of the Ring", "genre":"Fiction"},
{"author":"Bennett", "title":"City of Stairs", "genre":"Fiction"},
{"author":"Desmond", "title":"Evicted", "genre":"Non-Fiction"},
{"author":"Adichie", "title":"Purple Hibiscus", "genre":"Fiction"}]}, {"user": "dougschulte", "library": [{"author":"Giffin", "title":"Something Borrowed", "genre":"Fiction"}, 
{"author":"Giffin", "title":"Something Blue", "genre":"Fiction"},
{"author":"Levine", "title":"Ella Enchanted", "genre":"Juvenile Fiction"},
{"author":"Meyer", "title":"Eclipse", "genre":"Young Adult Fiction"},
{"author":"Herbert", "title":"Dune",  "genre":"Fiction"}]}, {"user": "sarahlazun", "library": [{"author":"Crichton", "title":"Jurassic Park",  "genre":"Fiction"}, 
{"author":"Herbert", "title":"Dune",  "genre":"Fiction"},
{"author":"Mantell", "title":"Wolf Hall", "genre":"Fiction"}]}]


#welcome user, give instructions on how to use library
print("Welcome to bookshare, a community of mini-libraries.")

#set up profile - append email to user email list
my_user_name = input("Enter a username to get started: ")

#create list for user to add titles to
list_of_books = []
user_dict = {"user": my_user_name, "library":list_of_books}

#ask user to add titles and set up library
library_create = input("Would you like to set up your own library?: ")

if library_create == "yes":
    book_lookup = input("Great, add a book from your shelf to get started: ")
    selected_author = input("Now enter the author of the book: ")
    book_request_url = f"https://www.googleapis.com/books/v1/volumes?q={book_lookup}+inauthor:{selected_author}&key={GOOGLE_BOOKS_API_KEY}"
    response = requests.get(book_request_url)
    parsed_response = json.loads(response.text)

    if parsed_response["totalItems"] == 0:
        print("Sorry, couldn't find any data for that title.") #courtesy of stack overflow on error handling with json loads
        quit()
    else: 
        book_keys = parsed_response["items"][0]["volumeInfo"]
        author_keys = book_keys["authors"]
        author_keys = ''.join(author_keys)
        title_keys = book_keys["title"]
        genre_keys = book_keys["categories"]
        genre_keys = ''.join(genre_keys)
        user_books = {"author":author_keys, "title":title_keys, "genre":genre_keys}
        list_of_books.append(user_books)
        print("Here is your current shelf", list_of_books)
        user_libraries.append(user_dict.copy())

    while browsing:
        add_books = input("Would you like to add or subtract from your shelf? Enter 'add' to add more books and 'remove' to remove books: ")
        #sets up the continuous loop for user to add/ subtract as they see fit
        if add_books == "add":
            browsing = True  
            book_lookup = input("Enter more titles to add books to your shelf. Enter 'done' when you are finished: ")
            selected_author = input("Now enter the author of the book: ")
            book_request_url = f"https://www.googleapis.com/books/v1/volumes?q={book_lookup}+inauthor:{selected_author}&key={GOOGLE_BOOKS_API_KEY}"
            response = requests.get(book_request_url)
            parsed_response = json.loads(response.text)

            if parsed_response["totalItems"] == 0:
                print("Sorry, couldn't find any data for that title.") #courtesy of stack overflow on error handling with json loads
                quit()
            elif book_lookup == "done".lower():
                break  
            else: 
                browsing = True
                if parsed_response["totalItems"] == 0:
                    print("Sorry, couldn't find any data for that title.") #courtesy of stack overflow on error handling with json loads
                    quit()
                else:
                    book_keys = parsed_response["items"][0]["volumeInfo"]
                    author_keys = book_keys["authors"]
                    author_keys = ''.join(author_keys)
                    title_keys = book_keys["title"]
                    genre_keys = book_keys["categories"]
                    genre_keys = ''.join(genre_keys)
                    user_books = {"author":author_keys, "title":title_keys, "genre":genre_keys}
                    list_of_books.append(user_books)
                    print("Here is your new shelf", list_of_books)
                    user_libraries.append(user_dict.copy()) #append user to user libraries 
                continue 
        if add_books == "remove":
            browsing = True  
            book_lookup = input("Enter the title you would like to remove from your shelf: ")
            book_remove = remove_verify(book_lookup)
            print(book_remove)
            break 
        else:
            browsing = not True
            print("Great! You can always add more books to your shelf later.")
            break #gives user a way out of the loop

browse = input("Would you like to borrow a book today? Type 'yes' to browse our shelves: ")
    #matching_products = [p for p in products if int(p["id"]) == int(selected_id)]

book_titles = []

for i in user_libraries[0:]: 
    for b in i["library"][0:]:
        title_list = (b["title"])
        book_titles.append(title_list)

if browse == "yes":
    borrow_book = input("Would you like to borrow a book today? Enter the name of a title to browse: ")
    if borrow_book in book_titles:    
        print("Hooray,", borrow_book, "is available!")
    else: 
        print("Sorry,", borrow_book, "is not available at this time!")
else: 
    print("Thanks for stopping by! Come again soon.")
    quit()

for i in user_libraries[0:]:
    for b in i["library"][0:]:
        if borrow_book == b["title"]:
            print(i["user"], "has a copy of", borrow_book)
    
selected_user = input("Please enter the name of the user you would like to borrow from: ")
book_request = input("Please enter the name of the book you would like to borrow: ")
my_user_email = input("Please enter your email address so you can coordinate pickups: ")

book_message = os.path.join(os.path.dirname(__file__), "%s.txt" % my_user_name)

with open(book_message, "w") as file: 
    file.write(my_user_name)
    file.write(" would like to borrow your copy of ")
    file.write(book_request)
    file.write("\n")
    file.write("Please reach out to them at ")
    file.write(my_user_email)
    file.write(" to coordinate pickup.")
    file.write("\n")
    file.write("Have a great day!")
    file.write("\n")

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS")
selected_user = os.environ.get(selected_user)

sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
from_email = Email(MY_EMAIL_ADDRESS)
to_email = Email(selected_user)
subject = "You have a new checkout request"

with open(book_message) as fp:
    message_text = fp.read()
content = Content("text/plain", message_text)
mail = Mail(from_email, subject, to_email, content)

response = sg.client.mail.send.post(request_body=mail.get())

pp = pprint.PrettyPrinter(indent=4)

print("----------------------")
print("Great! Your request has been sent. They will reach out to you within the next week. Enjoy the read!")
print("----------------------")
