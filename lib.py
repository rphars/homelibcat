import csv
import urllib.request, json

#search for ISBN on google books
def isbn_websearch(isbn):
    try:
        with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn) as url:
            bookdata = json.load(url)
            #link right info to right variables
            title=bookdata['items'][0]['volumeInfo']['title']
            pages=bookdata['items'][0]['volumeInfo']['pageCount']
            languages=bookdata['items'][0]['volumeInfo']['language']
            authorname=bookdata['items'][0]['volumeInfo']['authors'][0]
                        
    except:
        authorname=""
        pass
    #for user to check output
    if authorname:
        print("Author: ",authorname)
        print("Title: ",title)
        print("Number of pages: ",pages)
        print("Languages: ",languages)
        #if output makes sense, add to database?
        confirm_to_db=input("Do you want to add this book to the database yes/no?")
        if confirm_to_db=="yes":
            #todo: add check if already in db
            #add book to csv
            with open("libdat.csv", "a",newline="") as file:
                writer = csv.writer(file)
                # Write the values to the file
                writer.writerow([title, authorname, pages,languages])
                #confirm to user
                print("\n"+"added")
        else:
            print("\n"+"not added")

    else:
        print("Info not found")


#selection options; main menu
def menu():
    while True:

        print("1: add book, 2: search, 3: view database, 4: exit ")
        choice=int(input('Please choose an option '))
        while choice in range(1,5):
            match choice:
                case 1:
                    #add book option
                    title_search=input("To add a book, please enter ISBN ")
                    isbn_websearch(title_search)
                    
                    menu()
                case 2: 
                    #book search option: currently only exact matches. todo: improve for partials!
                    search_value = input('please enter your search query\n').lower()
                    with open("libdat.csv", "r") as file:
                        reader = csv.reader(file)
                        #Loop through the rows in the file
                        for row in reader:
                            #If the search value matches any of the fields
                            if search_value in row[0].lower() or search_value in row[1].lower():
                                # Show the book details in a message box
                                print(f"Title: {row[0]}\nAuthor: {row[1]}")
                    menu()
                case 3:
                    #view entire database
                    with open("libdat.csv","r") as file:
                        reader=csv.reader(file)
                        for row in reader:
                            print(row)
                        menu()
                case 4:
                    #exit program
                    print("Thanks")
                    exit()
                    
menu()




    


