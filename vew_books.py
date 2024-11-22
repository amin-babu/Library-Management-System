def see_all_books(book_list):
  if book_list != []:
    for book in book_list:
      print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']}")
  else:
    print('No Book Found')