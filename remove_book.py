import save_book_list

def delet_book(book_list):
  isbn = int(input('Enter the Book ISBN : '))
  for book in book_list:
    if book['isbn'] == isbn:
      book_list.remove(book)
      save_book_list.save_books(book_list)
      print('Book Removed Successfully')
      return book_list
  
  print('No Book Found')
  return book_list