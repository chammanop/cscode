import csv
#file names
book_data='Books_data.csv'
borrow='borrow_data.csv'



def instrutions():
    print('''
          1.Enter Book Data
          2.Edit Book qty
          3.View Borrowed Books
''')
def books():
    with open(book_data,'a',newline='\n') as file:
        writer=csv.writer(file)
        while True:
            book=input('Enter Book name>>')
            if book.lower()=='n':
                break
            else:
                qty=int(input('Enter Qty>>'))
                price=int(input("Enter Price>>"))
                print()
                writer.writerow([book,qty,price]) 
def book_qty_edit():
    file=open(book_data,'r',newline='\r\n')
    data=csv.reader(file)
    print('Edittting Qty and Price....')
    book=input('Enter Book Name>>')
    lst=[]
    for i in data:
        if i[0]==book:
            i.remove(i[1])
            i.remove(i[1])
            qty=int(input('Enter Qty>>'))
            price=int(input('Enter new Price>>'))
            lst.append([i[0],qty,price])
        else:
            lst.append(i)
    file.close()
    print('Editiing Successful')
    file=open(book_data,'w',newline='\n')
    writer=csv.writer(file)
    writer.writerows(lst)
    file.close()

def borrow():
    file=open(borrow,'r',newline='\r\n')
    print('''
          1.Display Borrowers>> 1
          2.Search by book>> 2
                   
''')
    ch=input('Enter>>')
    if ch=='1':
        data=csv.reader(file)
        for i in data:
            #username bookname price returafterday
            print(i[0],i[1],i[2],i[3])
    if ch=='2':
        data=csv.reader(file)
        book_name=input('\nEnter Book name>>')
        for i in data:
            if i[1]==book_name:
                print(i[0],i[1],i[2],i[3])
            else:
                print('BOOK NOT BORROWED')

 
