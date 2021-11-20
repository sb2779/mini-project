#Library management System (book details)

#I have planned to create a library in which the user have multiple choices. Options include adding a book in which user can add how many
#books he wants to add. The user can search the book details using the book id,author name, quantity of book, amount of book
#also they can delete the record of the books from the list. The user can exit from the book whenever they want by going back to main page.

#Function for adding the book details
def addNew(bookId,name,qty,amount,author):

#Taking input from the user of student details
    bookid = int(input("Please Enter Book Id    : "))
    bookName = str(input("Please Enter Book Name : "))
    bookAuthor = str(input("Please Enter Author Of Book : "))
    bookQty = int(input("Please Enter Quantity of Book      : "))
    bookAmount = float(input("Please Enter Amount of book      : "))
#Appending the details in the arrays
    bookId.append(bookid)
    name.append(bookName)
    qty.append(bookQty)
    amount.append(bookAmount)
    author.append(bookAuthor)
#Displaying message after adding the details
    print("Data Added Successfully")
    print()

#Function for searching the book details
def searchBook(bookId,name,qty,amount,author):
    #Taking input for the book id
    no = int(input("Please Enter the Book Id : "))
    #Taking temporary variable for checking if the book id exists or not
    pad = 0
    #Running for loop till the end of the book id array
    for i in range(0,len(bookId)):
        #Checking if the book id exists or not
        if(bookId[i] == no):
            #Incrementing  the flag if the book id found
            pad = pad + 1
            #Printing the details of the book
            print("Book Id Of Student : ",bookId[i])
            print("Name Of Book       : ",name[i])
            print("Author Of Book     : ",author[i])
            print("Quantity Of Books  : ",qty[i])
            print("Amount Of Book     : ",amount[i])
            print("==============================")
            print("Total Amount of Books : ",(qty[i]*amount[i]))
    #If pad is 0 then it means  the book is not found
    if(pad==0):
        print("Book Id Not Found.")
    #Else book is found
    else:
        print("Data Of Book is  Displayed.")
    print()

#Function for deleting the book details 
def deleteBook(bookId,name,qty,amount,author):

#Taking input for the book id
    no = int(input("Please Enter Book Id : "))
    #Taking temporary variable for checking if the book id exists or not
    pad = 0
    #Running for loop till the end of the book id array
    for i in range(0,len(bookId)):
        #Checking if the book id exists or not
        if(bookId[i] == no):
            #Incrementing  the pad if the book id found
            pad = pad + 1
#Printing the details of the book            
            print("Book Id Of Student : ",bookId[i])
            print("Name Of Book       : ",name[i])
            print("Author Of Book     : ",author[i])
            print("Quantity Of Books  : ",qty[i])
            print("Amount Of Book     : ",amount[i])
            print("==============================")
            print("Total Amount of Books : ",(qty[i]*amount[i]))
            print()
#Confirming from user to delete book
            s = str(input("Are you sure you want to delete(y/n) : "))
#If the user says yes then deleteing the details from the array and breaking the loop
            if(s=="y"):
                bookId.pop(i)
                name.pop(i)
                author.pop(i)
                qty.pop(i)
                amount.pop(i)
                break
#If the user says no then exiting the loop
            else:
                flag = 2
                break
    if(pad==0):
        print("Book Id Not Found.")
    elif(pad==1):
        print("Data Of Book Deleted profitably.")
    print()

#Function for displaying the menu
def menu():
    print("===============================")
    print("== Library Management System ==")
    print("===============================")
    print("== 0. Exit                   ==")
    print("== 1. Add New Book           ==")
    print("== 2. Search Book            ==")
    print("== 3. Delete Book            ==")
    print("===============================")

#Project function to call menu function and decide which function to call
def project(bookId,name,qty,amount,author):
    #Running infinite loop so that user can use options multiple times
    while(True):
        print()
        print()
#Calling the menu function from which user can choose
        menu()
#Taking the input of user choice
        ch = int(input("Please Enter Your Choice : "))
        #If the user chooses 0 then we will exit the program
        if(ch == 0):
            print("Thank you for using")
            break
        #If the user chooses 1 then we will call the add function
        elif(ch == 1):
            addNew(bookId,name,qty,amount,author)
        #If the user chooses 2 then we will call search function
        elif(ch == 2):
            searchBook(bookId,name,qty,amount,author)
        #If the user chooses 3 then we will delete function
        elif(ch == 3):
            deleteBook(bookId,name,qty,amount,author)
        #If the user enters something else, displaying the message
        else:
            print("Wrong Input!")
        
#Creating the arrays for storing the data
bookId = list()
name = list()
qty = list()
amount = list()
author = list()

#Calling the main function and passing arrays as parameters
project(bookId,name,qty,amount,author)
