__author__ = 'quicksand77'
import platform
class MakeHtml():
    def __init__(self):
        self.makePath()
        self.getText()
        self.makeHtml()
    def makePath(self):
        a = platform.system()
        path = "output.txt"
        if a == "Linux":
            self.isWindows = False
        elif a == "Windows":
            self.isWindows = True
        if self.isWindows:
            self.path = ".\\"+path
        else:
            self.path = ".//"+path
    def getText(self):
        with open(self.path,"r") as f:
            self.lineList = f.readlines()
        self.lineList.pop(0)
        self.lineList.pop(0)
        self.lineList.pop(0)
        self.newLineList = []
        for line in self.lineList:
            self.newLineList.append(line.split(','))
    def makeHtml(self):
        with open(".\\infogetterplot.html","w") as f:
            f.write('<html>\n')
            f.write('<head>\n')
            f.write('<title>Infogetter html plot</title>\n')
            f.write('</head>\n')
            f.write('<h1>infogetter title</h1>\n')
            f.write('<body>\n')
            f.write('<p>')
            for line in self.newLineList:
                f.write(line[0].strip()+'space'+line[1].strip()+'\n')
            f.write('</p>')
            f.write('\n<img = src="plotpic.png" width="300" height="250"\n')
            f.write('</body>\n')
            # f.write()
            # f.write("close")