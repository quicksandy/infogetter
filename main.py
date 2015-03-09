__author__ = 'quicksand77'
__author__ = 'quicksand77'
def ask():
    a = raw_input("infogetter[1-3].py('1','2','3','q'): ")
    if a == "2":
        from infogetter import Remote
        Remote()
    elif a == "2":
        from infogetter2 import Remote
        Remote()
    elif a == "3":
        from infogetter3 import Remote
        Remote()
    elif a == "q":
        print
    else:
        print "Invalid entry."
        ask()
ask()