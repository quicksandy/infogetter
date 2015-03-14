__author__ = 'quicksand77'
__author__ = 'quicksand77'
def ask():
    print "****use infogetter2.py please****"
    a = raw_input("infogetter[1-3].py('1','2','3','g','show','html','q'): ")
    if a == "1":
        from infogetter import Remote
        Remote()
    elif a == "2":
        from infogetter2 import Remote
        Remote()
    elif a == "3":
        from infogetter3 import Remote
        Remote()
    elif a == "q":
        print "exiting"
    elif a == "g":
        from graphinfo import InfoPlot
        InfoPlot()
    elif a == "html":
        from infogetterhtml import MakeHtml
        MakeHtml()
    elif a == "show":
        try:
            with open(".\output.txt","r") as f:
                a = f.readlines()
                for line in a:
                    print line.strip()
        except Exception as e:
            print "No file found, error: %s"%(e)
    else:
        print "Invalid entry."
        ask()
ask()