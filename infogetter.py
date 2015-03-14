__author__ = 'quicksand77'
# 2.7.9
import paramiko, re, shlex, os, sys, datetime, time
class Remote:
    def __init__(self):
        self.makePath()
        # self.time()
        self.listToWrite = []
        self.check()
        if not self.quit:
            print "Welcome to infogetter. This program collects system model, firmware version, server temperature, and ip addresses. Please be patient as it does take time to ssh to the drac."
            self.racadm = "racadm"
            self.command = "getsysinfo"
            self.searchForFirm = "Firmware Version"
            self.searchForIP = "Current IP Address"
            self.searchForModel = "System Model"
            self.searchForTemp = "System Board Inlet Temp"
            self.collectInfo(self.searchForModel)
            self.collectInfo(self.searchForFirm)
            self.collectInfo(self.searchForIP)
            self.command = "getsensorinfo"
            self.collectInfo(self.searchForTemp)
            self.export()
    # def time(self):
    #     self.month1 = int(datetime.datetime.now().strftime(("%m")))
    #     self.day1 = int(datetime.datetime.now().strftime(("%d")))
    #     self.hour1 = int(datetime.datetime.now().strftime(("%H")))
    #     self.minute1 = int(datetime.datetime.now().strftime(("%M")))
    def makePath(self):
        if os.path.exists(".\output.txt"):
            self.path = ".\output.txt"
        else:
            self.path = "./output.txt"
    def collectInfo(self,searchables):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.server,port=22,username=self.username,password=self.passw)
        stdin, stdout, stderr = ssh.exec_command(self.racadm+" "+self.command)
        for line in stdout.readlines():
            j = line.split("\t")
            for item in j:
                m = re.search(searchables,item)
                if m:
                    shlexed = shlex.split(item)
                    if len(shlexed) > 1:
                        try:
                            if searchables == self.searchForModel:
                                print "%s %s:\t%s %s"%(shlexed[0],shlexed[1],shlexed[-2],shlexed[-1])
                                string1 = shlexed[-2]+","+shlexed[-1]
                                self.listToWrite.append(string1)
                            elif searchables == self.searchForFirm:
                                print "%s %s:\t%s"%(shlexed[0],shlexed[1],shlexed[-1])
                                string1 = shlexed[-1]
                                self.listToWrite.append(string1)
                            elif searchables == self.searchForIP:
                                if len(shlexed) == 5:
                                    print "%s %s:\t%s"%(shlexed[0],shlexed[1],shlexed[-1])
                                    string1 = shlexed[-1]
                                    self.listToWrite.append(string1)
                            elif searchables == self.searchForTemp:
                                cel = shlexed[5]
                                shlexed[5] = str(int(shlexed[5])*1.8+32)
                                shlexed[6] = "F"
                                print "System Temp:\t%s %s or %s C"%(shlexed[5],shlexed[6],cel)
                                now = time.time()
                                string1 = "t"+str(now)+","+shlexed[5]
                                self.listToWrite.append(string1)
                        except Exception as e:
                            print e
                            continue
    def export(self):
        if not os.path.exists(self.path):
            with open(self.path,"w") as f:
                print self.path+" not found, creating now."
        with open(self.path,"a") as f:
            for thing in self.listToWrite:
                f.write(thing+"\n")
    def check(self):
        if len(sys.argv) == 4:
            self.server = sys.argv[1]
            self.username = sys.argv[2]
            self.passw = sys.argv[3]
            self.quit = False
            self.rerun = "no"
        elif len(sys.argv) == 5:
            self.server = sys.argv[1]
            self.username = sys.argv[2]
            self.passw = sys.argv[3]
            self.quit = False
            self.rerun = sys.argv[4]
        else:
            print "Invalid argument count. Please rerun and use the format after script name:\nipaddress username password [number of times to run(optional)]"
            self.quit = True