import add_books
import view_all_books
import update_book
import remove_book

all_books = []

while True:
  print('Welcome to Library Management System')
  print('0. Exit')
  print('1. Add Books')
  print('2. View All Books')
  print('3. Update Book')
  print('4. Remove Book')

  option = input('Select a Number: ')

  if option == '0':
      print('Thanks for using Library Management System')
      break
  elif option == '1':
      all_books = add_books.add_books(all_books)
  elif option == '2':
      view_all_books.view_all_books(all_books)
  elif option == '3':
      all_books = update_book.update_book(all_books)
  elif option == '4':
      all_books = remove_book.remove_book(all_books)
  else:
      print('Choose a valid number')
