__author__ = 'quicksand77'
# 2.7.9
import paramiko, re, shlex, os, sys, time
class Remote:
    def __init__(self):
        self.makePath()
        self.listToWrite = []
        self.checkArgs()
        self.initialRunCheck()
        if not self.quit:
            print "Welcome to infogetter. This program collects system model, firmware version, server temperature, and ip addresses. Please be patient as it does take time to ssh to the drac."
            self.goGetTheStuff()
            self.export()
            count = 1
            if self.rerun == "no":
                print "program end"
            else:
                while (int(self.rerun) - count) != 0:
                    print "Rerunning %s more times."%(str(int(self.rerun) - count))
                    self.goGetTheStuff()
                    self.export()
                    count += 1
    def makePath(self):
        if os.path.exists(".\output.txt"):
            self.path = ".\output.txt"
        else:
            self.path = "./output.txt"
    def goGetTheStuff(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.server,port=22,username=self.username,password=self.passw)
        self.commands = ["System Model","Firmware Version","Current IP Address","System Board Inlet Temp"]
        if not self.hasRun:
            self.anotherFunction(self.commands,"getsysinfo")
        else:
            self.commands = ["System Board Inlet Temp"]
            self.anotherFunction(self.commands,"getsysinfo")
    def anotherFunction(self,list1,subcommand):
        for thingy in list1:
            if thingy == "System Board Inlet Temp":
                subcommand = "getsensorinfo"
            stdin, stdout, stderr = self.ssh.exec_command("racadm "+subcommand)
            for line in stdout.readlines():
                j = line.split("\t")
                for item in j:
                    m = re.search(thingy,item)
                    if m:
                        shlexed = shlex.split(item)
                        if len(shlexed) > 1:
                            try:
                                if thingy == "System Model":
                                    print "%s %s:\t%s %s"%(shlexed[0],shlexed[1],shlexed[-2],shlexed[-1])
                                    string1 = shlexed[-2]+","+shlexed[-1]
                                    self.listToWrite.append(string1)
                                elif thingy == "Firmware Version":
                                    print "%s %s:\t%s"%(shlexed[0],shlexed[1],shlexed[-1])
                                    string1 = shlexed[-1]
                                    self.listToWrite.append(string1)
                                elif thingy == "Current IP Address":
                                    if len(shlexed) == 5:
                                        print "%s %s:\t%s"%(shlexed[0],shlexed[1],shlexed[-1])
                                        string1 = shlexed[-1]
                                        self.listToWrite.append(string1)
                                elif thingy == "System Board Inlet Temp":
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
    def initialRunCheck(self):
        if not os.path.exists(self.path):
            with open(self.path,"w") as f:
                self.hasRun = False
        else:
            self.hasRun = True
    def export(self):
        with open(self.path,"a") as f:
            for thing in self.listToWrite:
                f.write(thing+"\n")
    def checkArgs(self):
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