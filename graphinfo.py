__author__ = 'quicksand77'
__author__ = 'quicksand77'
import matplotlib,pylab, platform, re
matplotlib.use('Agg')
import matplotlib.pyplot as plt
class InfoPlot:
    def __init__(self):
        self.makePath()
        self.x = []
        self.y = []
        self.makeLists()
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
        else:
            self.path = ".//"+path
    def makeLists(self):
        self.tempTimeList = []
        with open(self.path,'r') as readFile:
            sepFile = readFile.read().split('\n')
        for thingy in sepFile:
            if re.match(r"^t",thingy):
                self.tempTimeList.append(thingy)
        self.newTempTimeList = ([s.replace('t', '') for s in self.tempTimeList])
        for plotPair in self.newTempTimeList:
            if plotPair == "":
                continue
            xAndY = plotPair.split(',')
            self.x.append(xAndY[0])
            self.y.append(int(float(xAndY[1])))
    def doPlot(self):
        plt.plot(self.y,'r-',linewidth=2.0)
        plt.xticks(range(len(self.x)),self.x)
        plt.xlabel('Time(seconds since January 1, 1970)')
        plt.ylabel('Temperature(F)')
        plt.ylim(50,110)
        plt.show()
        pylab.savefig('plotpic.png',bbox_inches='tight')
        # plt.savefig('plotpic.png')
        plt.close()

        # plt.figure(1)                # the first figure
        # plt.subplot(211)             # the first subplot in the first figure
        # plt.plot([1,2,3])
        # plt.subplot(212)             # the second subplot in the first figure
        # plt.plot([4,5,6])
        #
        #
        # plt.figure(2)                # a second figure
        # plt.plot([4,5,6])            # creates a subplot(111) by default
        #
        # plt.figure(1)                # figure 1 current; subplot(212) still current
        # plt.subplot(211)             # make subplot(211) in figure1 current
        # plt.title('Easy as 1,2,3')   # subplot 211 title
        # plt.show()
        # plt.close()