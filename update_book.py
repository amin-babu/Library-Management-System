from save_all_books import save_all_books

def update_book(all_books):
  isbn = int(input('Enter the ISBN of the book to update: '))
  for book in all_books:
    if book['isbn'] == isbn:
      print(f"Current Details: {book}")
      book['title'] = input('Enter new Title (or press Enter to keep current): ') or book['title']
      book['author'] = input('Enter new Author (or press Enter to keep current): ') or book['author']
      book['year'] = input('Enter new Year (or press Enter to keep current): ') or book['year']
      book['price'] = input('Enter new Price (or press Enter to keep current): ') or book['price']
      book['quantity'] = input('Enter new Quantity (or press Enter to keep current): ') or book['quantity']
      save_all_books(all_books)
      print('Book updated successfully.')
      return all_books
  print('Book not found!')
  return all_books
