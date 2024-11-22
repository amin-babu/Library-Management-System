import save_book_list

def include_books(book_list):
  title = input('Enter Book Title : ')
  author = input('Enter Author Name : ')
  isbn = int(input('Enter ISBN Number : '))
  year = int(input('Enter Publishing Year Number : '))
  price = int(input('Enter Book Price : '))
  quantity = int(input('Enter Quantity Number : '))

  book = {
    'title': title,
    'author': author,
    'isbn': isbn,
    'year': year,
    'price': price,
    'quantity': quantity,
  }

  book_list.append(book)
  save_book_list.save_books(book_list)
  print('Book added Successfully')
  return book_list