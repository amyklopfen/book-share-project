browsing = True 

import os
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import * # info drawn from send notification exercise.

load_dotenv()

import pprint

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

#lender_list = [amyklopfen, dougschulte, sarahlazun]

amyklopfen_library = [{"author":"Sanderson", "title":"The Way of Kings", "ISBN": 9780765365279, "genre":"sci-fi"}, 
{"author":"Tolkein", "title":"The Hobbit", "ISBN": 9780345339683, "genre":"fantasy"},
{"author":"Sanderson", "title":"The Hero of the Ages", "ISBN": 9780765377159, "genre":"sci-fi"},
{"author":"FLynn", "title":"Gone Girl", "ISBN": 9780307588371, "genre":"thriller"},
{"author":"Altwater-Rhodes", "title":"Hawksong", "ISBN": 9780440238034, "genre":"romance"},
{"author":"Hanley", "title":"The Seer and the Sword", "ISBN": 9780823415328, "genre":"fantasy"},
{"author":"Tolkein", "title":"The Fellowship of the Ring", "ISBN": 9780395489314, "genre":"fantasy"},
{"author":"Bennett", "title":"City of Stairs", "ISBN": 9780804137171, "genre":"fantasy"},
{"author":"Desmond", "title":"Evicted", "ISBN": 9780553447453, "genre":"non-fiction"},
{"author":"Adichie", "title":"Purple Hibiscus", "ISBN": 9781616202415, "genre":"literary"}]

dougschulte_library = [{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"}, 
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"}]

sarahlazun_library = [{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"}, 
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"},
{"author":"author", "title":"title", "ISBN": "ISBN", "genre":"genre"}]

user_libraries = [amyklopfen_library, sarahlazun_library, dougschulte_library]

#welcome user, give instructions on how to use library
print("Welcome to bookshare, a community of mini-libraries. Search for a title, author, or genre to get started.")

#list of user emails? 
#set up profile - append email to user email list
my_user_name = input("Enter a username to get started: ")

library_create = input("Would you like to set up your own library?")

if library_create == "yes":
    user_input = input("Great, add books from your shelf to get started: ")
    list_of_books = user_input.split()
    print("Here is your current shelf", list_of_books)
    add_books = input("Would you like to add or subtract from your shelf? Enter 'add' to add more books and 'remove' to remove books: ")
    
while browsing: #sets up the continuous loop for user to add/ subtract as they see fit
    if add_books == "add":
        browsing = True  
        new_shelf = input("Enter more titles to add books to your shelf: ")
        list_of_books.append(new_shelf) #append allows user to continue to add items to list
        print("Here is your new shelf", list_of_books)
        break 
    elif add_books == "remove":
        browsing = True  
        new_shelf = input("Enter the titles you would like to remove from your shelf: ")
        list_of_books.remove(new_shelf)
        print("Here is your new shelf", list_of_books)
        break 
    else:
        browsing = not True
        print("Great! You can always add more books to your shelf later.")
        break #gives user a way out of the loop



#borrowing
print("Input a list of books you would like to lend to gest started")

#background
    #install packages
    #set up API 
    #env with sendgrid API, dummy library emails
    #use web scraper to get ISBN, author, and cover for Goodreads/Amazon
    #set up lists to demo

#ask user to add titles and set up library
    #user input
    #validate user inputs
        #check Goodreads API to make sure title exists
        #ensure input is valid (not int)
        #use "done" or "exit" to allow user to leave library when complete
    #enter email???

#ask user to search for title
    #user input
    #set up way to select titles

#search list of libraries
    #group by zip code
    #search other libraries

#give user ability to send email request to book buddy 
    #sendgrid API
    #set up message function to other user - email?
    #set up existing user emails in .env, assign them each a unique variable by username
    #user selects amyklopfen_library
    #.env has amyklopfen = ak6266@stern.nyu.edu 
    #code has request_email = input("Please enter the user you would like to borrow from.")
    #sendgrid code has request_email embedded

selected_user = input("Please enter the name of the user you would like to borrow from: ")
selected_user = os.environ.get(selected_user, "OOPS, please set env var called 'selected_user'")
book_request = input("Please enter the name of the book you would like to borrow: ")


from_email = Email(MY_EMAIL_ADDRESS)
to_email = Email(selected_user)
subject = "You have a new checkout request"
message_text = "Amy" + "would like to borrow your copy of" + "book name" + "please reach out to them at" + "user email" + "to coordinate pickup"
content = Content("text/plain", message_text)
mail = Mail(from_email, subject, to_email, content)


response = sg.client.mail.send.post(request_body=mail.get())



pp = pprint.PrettyPrinter(indent=4)

print("----------------------")
print("EMAIL")
print("----------------------")
print("RESPONSE: ", type(response))
print("STATUS:", response.status_code) 
print("HEADERS:")
pp.pprint(dict(response.headers))
print("BODY:")
print(response.body) 
