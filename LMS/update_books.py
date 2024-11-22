import save_book_list

def change_books_item(book_list):
  isbn = int(input("Enter the books ISBN : "))

  for book in book_list:
    if book['isbn'] == isbn:
      print(f"Current Details : {book}")
      book['title'] = input('Enter new Title : ') or book['title']
      book['author'] = input('Enter new author name : ') or book['author']
      book['isbn'] = int(input('Enter new ISBN Number : ')) or book['isbn']
      book['year'] = int(input('Enter new year : ')) or book['year']
      book['price'] = int(input('Enter new price : ')) or book['price']
      book['quantity'] = int(input('Enter new quantity : ')) or book['quantity']

      save_book_list.save_books(book_list)
      print('Book Updated Successfully')
      return book_list
  
  print('No Book Found')
  return book_list