__author__ = 'quicksand77'
__author__ = 'quicksand77'

##################################################
# not working yet, has only been set up
##################################################
import matplotlib.pyplot as plt
import platform
class InfoPlot:
    def __init__(self):
        self.makePath()
        self.x = []
        self.y = []
        self.makeStuff()
        self.doPlot()
    def makePath(self):
        a = platform.system()
        path = "output.txt"
        if a == "Linux":
            self.isWindows = False
        elif a == "Windows":
            self.isWindows = True
        if self.isWindows:
            self.path = ".\\"+path
        elif not self.isWindows:
            self.path = ".//"+path
        else:
            self.path = ".\\"+path
    def makeStuff(self):
        with open(self.path,'r') as readFile:
            sepFile = readFile.read().split('\n')
        for plotPair in sepFile:
            if plotPair == "":
                continue
            xAndY = plotPair.split(',')
            print xAndY
            self.x.append(int(xAndY[0]))
            self.y.append(int(xAndY[1]))
    def doPlot(self):
        # plt.plot(self.x,self.y,'r--',linewidth=2.0)
        # plt.xlabel('temperatures')
        # plt.ylabel('time')
        # plt.ylim(50,110)
        # plt.show()
        # plt.close()
        plt.figure(1)                # the first figure
        plt.subplot(211)             # the first subplot in the first figure
        plt.plot([1,2,3])
        plt.subplot(212)             # the second subplot in the first figure
        plt.plot([4,5,6])


        plt.figure(2)                # a second figure
        plt.plot([4,5,6])            # creates a subplot(111) by default

        plt.figure(1)                # figure 1 current; subplot(212) still current
        plt.subplot(211)             # make subplot(211) in figure1 current
        plt.title('Easy as 1,2,3')   # subplot 211 title
        plt.show()
        plt.close()
InfoPlot()