# book-share-project

#Background

The goal is to create an app that will a) allow users to add books that they want to lend b) allow users to search and select books from other users and c) email users with a request to check out their books. 

#Set up

Start by creating a repository in GitHub, including a gitignore file and a readme file

Once you have the file saved to your GitHub desktop, create a env file as well

Make sure you have a Sendgrid account and a Sendgrid API Key. If you don't have an account, you can set one up here: https://sendgrid.com/solutions/email-api/.

Once you have the Sendgrid API Key, save it to the env file with a variable like Sendgrid_API_KEY. Save the email address you used to set up the Sendgrid account to a variable like MY_EMAIL_ADDRESS

Create an API with Google Books. You can follow the instructions listed here to get a Google Account and request a Google Books API: https://developers.google.com/books/docs/v1/using

Save the Google Books API to the env file with a variable like Google_Books_API_Key

Save any usernames and their corresponding emails to the env file. For example, if janedoe's email address is janedoe@nyu.edu, save the information as: 

    janedoe = janedoe@nyu.edu

Make sure any user you want to include in the app has an email address saved in the env file

#Setting up your virtual environment

Once you have your variables set up in the env file, go to the Gitbash command line and set up your virtual environment: 

    conda create -n books-env python = 3.7

Then:

    conda activate books-env

Since we will be using a Google API Key, also install this in the command line: 

    pip install -U google-api-python-client

#Installing packages and modules

In the code, import the following packages/modules to your python file: 

    import os
    import json
    from dotenv import load_dotenv
    import sendgrid
    from sendgrid.helpers.mail import * 
    import datetime
    import requests 
    import apiclient
    from apiclient import discovery
    import pprint

Make sure you also include: 

    load_dotenv()

This will ensure the info you saved in the env file is properly called later in the code

#Initial code set up

At the top of the file, write: 

    browsing = True

We'll need this later for adding/subtracting items from user shelves

Retrieve the Google API Key from the env document using the following command: 

    GOOGLE_BOOKS_API_KEY = os.environ.get("GOOGLE_BOOKS_API_KEY")

There's also a function you'll need to call later you should add to the top of the code: 

    def remove_verify(book_name):
        for i in list_of_books:
        if i['title'] == book_lookup:
            list_of_books.remove(i)
            p = "Here is your new list" + str(list_of_books)
        else: 
            p = "Sorry, that title is not on your shelf!"
        return p

It will allow users to remove an unwanted book from their book list, and will validate whether the book exists in their list. I think it's nice to define functions before getting into the rest of the code, so add that function at the top after the import commands and the Google API command

#Dummy library set up

Set up a list called 'user_libraries.' Within user_libraries, create dictionaries corresponding to the users you added to the env file. Create another list of dictionaries (a library, or "shelf") for each user that contains book, title, and genre information for each book to be included in the demo. 

In a real-world scenario, users would add their "shelves" organically as they signed up for the app. But, we need something to demo, so add a few by hand to serve as an example. 

For example:

    user_libraries = [{"user": "janedoe", "library":[{"author":"author1," "title": "title1", "genre": "genre1"}, {"author":"author2"....}]}, {"user": "johndoe", "library": [{"author":"author1", ...}]}]

Ultimately, you should set up a few users, each of whom have a few books, to properly demo the app

#Greet the user and invite them to set up an account

Now, it's finally time to greet the user. I would print a little welcome statement with an explanation about the function of the app, like: 

    print("Welcome to bookshare, a community of mini-libraries.")

Next, use input() to prompt the user to enter a username. Store the username in some sort of variable, like 'my_user_name', because we'll need it later

#set up storage lists and dictionaries

set up a list and a dictionary to store data we'll process later. For now, make the list empty and give it a name like 'list_of_books.' Give the dictionary a name like 'user_dict' and set it up like this: 

    user_dict = {"user": my_user_name, "library":list_of_books}

This will allow us to add the user's book data to list_of_books. We can then drop that list in the 'library' in user_dict and connect it back to the user's username. 

#prompt user to create their own library

Use the input() prompt to ask whether a user wants to set up a library - i.e. lend books of their own. They have the option of saying 'no', which will take them to part b) browsing. But if the user says 'yes', we will go into next steps for adding/validating books

#User enters 'yes': instructions for setting up a library

First, we will use input() to prompt the user to enter the title of a book that they want to add to their library. Save the input in a variable like 'book_lookup.' We'll need it later.

Use input() again to prompt the user to enter the author of the book they want to add. Assign it a variable like 'selected_author.'

Next, 




