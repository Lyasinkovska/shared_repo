import sys

def phonebook(n):
    book = {}
    for i in range(n):
        data = input()
        name = data.split()[0]
        number = data.split()[1]
        book[name] = number
    return book

def query(n):
    book = phonebook(n)
    query = sys.stdin.readlines().rstrip()
    for line in query:
        if query in book.keys():
            print("{}={}".format(query, book[query]))
        else:
            print("Not found")


n = int(input())

query(n)

