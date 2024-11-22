import add_books
import update_books
import remove_book
import vew_books

all_books = []

while True:
  print('Welcome to Library Management System')
  print('0. Exit')
  print('1. Add Books')
  print('2. Update Book')
  print('3. Remove Book')
  print('4. View All Books')

  option = int(input('Select an option : '))

  if option == 0:
    print('Thanks for using Library Management System')
    break
  elif option == 1:
    all_books =  add_books.include_books(all_books)
  elif option == 2:
    all_books = update_books.change_books_item(all_books)
  elif option == 3:
    all_books = remove_book.delet_book(all_books)
  elif option == 4:
    vew_books.see_all_books(all_books)
  else:
    print('Select Valid Number')
