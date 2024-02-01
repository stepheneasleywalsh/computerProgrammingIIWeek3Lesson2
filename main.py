import csv

# Create Files
try:
    f=open("books.csv","r")
    f.close()
    print("Book database found")
except FileNotFoundError:
    f=open("books.csv","w")
    f.write("name,price")
    f.close()
    print("Creating database file")

# Choose
choice = input("Do you want to ADD to the database, EDIT a price or SEARCH it? Type ADD, EDIT or SEARCH.")

# ADD BOOK
if choice.upper() == "ADD":
    while True:
        name = input("name: ")
        price = input("price: ")
        if name == "":
            break
        else:
            f=open("books.csv","a")
            f.write("\n"+name+","+price)
            f.close()

# EDIT BOOk
elif choice.upper() == "EDIT":
    name = input("name: ")
    price = input("new price: ")
    found = False
    newRows = []
    with open("books.csv", encoding='utf-8-sig') as f:
        readCSV = csv.reader(f)
        for row in readCSV:
            if row[0].lower() == name.lower():
                found = True
                print("Book Found, its price is", row[1])
                newRows.append([row[0],price])
            else:
                newRows.append(row)
    if found == False:
        print("Book Not Found")
    else:
        f = open("books.csv","w")
        f.write("name,price")
        for row in newRows:
            f.write("\n"+row[0]+","+row[1])
        f.close()

# SEARCH BOOk
else:
    name = input("name: ")
    found = False
    with open("books.csv", encoding='utf-8-sig') as f:
        readCSV = csv.reader(f)
        for row in readCSV:
            if row[0].lower() == name.lower():
                found = True
                print("Book Found, its price is", row[1])
    if found == False:
        print("Book Not Found")

quit()