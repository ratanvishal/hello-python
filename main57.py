def searcher():
    import time
    # some 4 seconds time consuming task
    book="this is a book in a library"
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")
search= searcher()
next(search)
search.send("vishal")
input("press any key")
search.send("joker")
input("press any key")
search.send("plz learn")
search.close()