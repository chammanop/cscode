import pickle
import csv

f='user_data.dat'
book='Books_data.csv'
borrow='borrower_data.csv'
details=[]

def return_book():
    file=open(borrow,'r',newline='\r\n')
    data=csv.reader(file)
    for i in data:
        if i[0]==details[0]:
            print(f'''
Borrowed Books....
1.Book Code->{i[1]}
2.Book Name->{i[2]}
3.Days remaining->{i[4]}

''')
    ch=input('Enter Book Code to return>>')
    lst=[]
    for i in data:
        if i[1]==ch:
            i.clear()
            f.close()





def display_book():
    with open(book,'r',newline='\r\n') as file:
        data=csv.reader(file)
        for i in data:
            print(i[0],':',i[1],'->',i[3])

def search_book():
    with open(book,'r',newline='\r\n') as file:
        data=csv.reader(file)
        print('....SEARCH BOOKS....')
        bname=input('Enter Book Name>>')
        for i in data:
            if i[0].lower()==bname.lower():
                print(f'''
Book Name->{i[1]}
Available Quantity->{i[2]}
Price->{i[3]}
''')

    

def borrow_data():
    display_book()
    bcode=input('\nEnter Book Code>>')
    details.append(bcode)
    ndays=input('ENter no days to return>>')
    with open(book,'r',newline='\r\n') as f:
        data=csv.reader(f)
        for i in data:
            if i[0]==bcode:
                details.append(i[1])
                details.append(i[2])
                print(f'\nAmount to be paid->{i[3]}')
        details.append(ndays)
    with open(borrow,'a',newline='\n') as file:
        writer=csv.writer(file)
        #print(details)
        writer.writerow(details)

def write():
    print('''
           1.Search Book>>1
           2.Borrow Book>>2
           3.Display Available Books>>3
           4.Return Book    
                    ''')
    
    ch=input('\nEnter>>')
    if ch=='1':
        search_book()
    elif ch=='2':
        borrow_data()
    elif ch=='3':
        display_book()
    elif ch=='4':
        return_book()
    

     

def new_usr():
    with open(f,'ab') as file:
        usr_name=input('Enter User name>>')
        details.append(usr_name)
        password=input('Enter Passowrd>>')
        record={'Username':usr_name,'Password':password}
        pickle.dump(record,file)
        print('\n....LOGIINED SUCCESSFULLY.....\n')
        write()


def existing_usr():
    file=open(f,'rb')
    usr_name=input('Enter User name>>')
    
    while True:
        try:
            data=pickle.load(file)
            if data['Username']==usr_name:
                details.append(usr_name)
                password=input('Enter password>>')
                if data['Password']==password:
                    write()
                    break
                else:
                    print('Wrong Password')
                    
        except EOFError:
            file.close()
            break

print(
    '''
#1. New User/Sign Up>> 1
#2. Login>> 2
'''
)
ch=input('Enter>>')
if ch=='1':
    new_usr()
elif ch=='2':
    existing_usr()
