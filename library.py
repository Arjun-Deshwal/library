
class Library:
    #constructor of the class 
  def __init__(self, libraryname, list_of_books ):
    self.libraryname= libraryname
    self.list_of_books= list_of_books
    self.lenddict={}
    #All the function needed to create library
  def db (self):#Display books function
    print(f"Here are the books in the library{self.libraryname}:{self.list_of_books}")
    
  def lb (self, name, book):#lend book function
    if book in self.list_of_books:
      print ("This book has been lended to you.")
      self.lenddict.append(book)
    elif book in self.lenddict:
      print(f"Sorry! this book is already lended to {name} ")  
    else : print("Oops! this book is not in our library")
    
  def rb (self, name, book):#Return book function
    if book in self.lenddict:
      self.lenddict.remove(book)
      print(f"{name} have successfully returned the book.")
    else:
      print(f"{name}, this book is not lended")
      
  def ab (self, book):#add book function
    self.list_of_books.append(book) 
    print("This book is successfully added to our library.")
    
  def delbook(self, name, book):#delete book function
    self.list_of_books.remove(book)
    self.lenddict.remove(book)
    print(f"{name}, this book is successfully removed. ")
print("Hi there, welcome.")     
#Performing operations with Library
def mainn():
    arjun=Library("Arjun Library",["1.Bhagvad Gita""2.The Monk who sold his Farrari","3.Attitude is everything","4.Tears of the school"])
    operation=int(input("Hi, what operation do you want to perform, press '1' for displaying books, press'2' for lending book, press '3' for returning book, press '4' for adding book, and press '5' for deleting book."))
    key=20063
    #Displaying books
    if operation==1:
        arjun.db()
    # lending books    
    elif operation==2:
        user=input('Please enter your name here\n ')
        bookl=input('Which book you want to lend from the library?\n')
        arjun.lb(user,bookl)
        #returning books
    elif operation==3:
        user=input('Please enter your name here\n ')
        bookl=input('Which book you want to return to the library?\n')
        arjun.rb(user,bookl)
        #adding books
    elif operation==4:
        bookl=input('Which book you want to add to the library?\n')
        arjun.ab(bookl)
        #deleting book
    elif operation==5:
        user=input('Please enter your name here\n ')
        bookl=input('Which book you want to delete from the library?\n')
        sec=int(input('Enter the key of library to delete book.\n'))
        if sec==key:
            print("Accessed!")
            print(f"{user}, the book was deleted successfully!")
            arjun.delbook
        else:
            
            print("Access denied! Wrong key.")
    else:
        print("Invalid operation!")
        ques=input("Press 'q' to quit and 'c' for continue")

    if ques=="q":
        exit()
    else:
      mainn()

if __name__ == "__main__":
    mainn()   
