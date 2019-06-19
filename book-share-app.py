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

#list of user emails? 
#set up profile - append email to user email list

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