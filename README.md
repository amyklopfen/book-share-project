# book-share-project

## Background

The goal is to create an app that will a) allow users to add books that they want to lend b) allow users to search and select books from other users and c) email users with a request to check out their books. 

## Set up

Start by forking the following repository in GitHub: https://github.com/amyklopfen/book-share-project

Once you've forked the repository, clone it to your GitHub desktop. 

Create a env file and a gitignore and save them to your repository

Make sure you have a Sendgrid account and a Sendgrid API Key. If you don't have an account, you can set one up here: https://sendgrid.com/solutions/email-api/.

## Securing Sensitive Information in ENV 

Once you have the Sendgrid API Key, save it to the env file with the variable Sendgrid_API_KEY:

```sh
SENDGRID_API_KEY = "Input Sendgrid API Here"
```

 Save the email address you used to set up the Sendgrid account to a variable MY_EMAIL_ADDRESS:

```sh
MY_EMAIL_ADDRESS = "Input Sendgrid Email Address Here"
```

Create an API with Google Books. You can follow the instructions listed here to get a Google Account and request a Google Books API: https://developers.google.com/books/docs/v1/using

Save the Google Books API to the env file with the variable GOOGLE_BOOKS_API_KEY:

```sh
GOOGLE_BOOKS_API_KEY = "Input Your API Key Here"
```

Save any usernames and their corresponding emails to the env file. For example, if the user janedoe's email address is janedoe@nyu.edu, save the information as: 

```sh
janedoe = janedoe@nyu.edu
```

Make sure any user you want to include in the app has an email address saved in the env file. 

There are currently dummy usernames (amyklopfen, line 36, dougschulte, line 45, and sarahlazun, line 49) in the user_libraries in the code. You will need to go into the code and replace the dummy usernames with the usernames you saved in the env file in order to run the app. 

## Setting up your virtual environment

Once you have your variables set up in the env file navigate to your repository on your command line:

```sh
cd book-share-project
```

Go to the Gitbash command line and set up your virtual environment: 

```sh
conda create -n books-env python=3.7
```

Then:

```sh
conda activate books-env
```


## Installing packages and modules

Now we will install some packages you'll need to run the app. Within your virtual environment, install this in the command line to enable the Google Books API key: 

```sh
pip install -U google-api-python-client
```

You may also need to use pip install to install the following packages if you have not already installed them: 

```sh
python-env
requests
sendgrid==5.6.0
```

## Run the App

Once you have finished installing, run the app in your command line:

```py
python book-share-app.py
```

Happy browsing!


