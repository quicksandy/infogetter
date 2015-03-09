__author__ = 'quicksand77'
__author__ = 'quicksand77'
# 2.7.9
import paramiko, re, shlex, os, sys, time
class Remote:
    def __init__(self):
        self.makePath()
        self.listToWrite = []
        self.check()
        if not self.quit:
            print "Welcome to infogetter. This program collects system model, firmware version, server temperature, and ip addresses. Please be patient as it does take time to ssh to the drac."
            self.goGetTheStuff("1")
            self.goGetTheStuff("2")
            self.export()
    def makePath(self):
        if os.path.exists(".\output.txt"):
            self.path = ".\output.txt"
        else:
            self.path = "./output.txt"
    def goGetTheStuff(self,which):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.server,port=22,username=self.username,password=self.passw)
        if which == "1":
            commands = ["System Model","Firmware Version","Current IP Address"]
            self.anotherFunction(commands,"getsysinfo")
        elif which == "2":
            commands = [0,0,0,"System Board Inlet Temp"]
            self.anotherFunction(commands,"getsensorinfo")
    def anotherFunction(self,list1,subcommand):
        for command in list1:
            stdin, stdout, stderr = self.ssh.exec_command("racadm "+subcommand)
            for line in stdout.readlines():
                j = line.split("\t")
                for item in j:
                    m = re.search(searchables,item)
                    if m:
                        shlexed = shlex.split(item)
                        if len(shlexed) > 1:
                            try:
                                if searchables == list1[0]:
                                    print "%s %s:\t%s %s"%(shlexed[0],shlexed[1],shlexed[-2],shlexed[-1])
                                    string1 = shlexed[-2]+","+shlexed[-1]
                                    self.listToWrite.append(string1)
                                elif searchables == list1[1]:
                                    print "%s %s:\t%s"%(shlexed[0],shlexed[1],shlexed[-1])
                                    string1 = shlexed[-1]
                                    self.listToWrite.append(string1)
                                elif searchables == list1[2]:
                                    if len(shlexed) == 5:
                                        print "%s %s:\t%s"%(shlexed[0],shlexed[1],shlexed[-1])
                                        string1 = shlexed[-1]
                                        self.listToWrite.append(string1)
                                elif searchables == list1[3]:
                                    cel = shlexed[5]
                                    shlexed[5] = str(int(shlexed[5])*1.8+32)
                                    shlexed[6] = "F"
                                    print "System Temp:\t%s %s or %s C"%(shlexed[5],shlexed[6],cel)
                                    string1 = shlexed[5]
                                    self.listToWrite.append(string1)
                            except Exception as e:
                                print e
                                continue
    def export(self):
        with open(self.path,"w") as f:
            for thing in self.listToWrite:
                f.write(thing+"\n")
    def check(self):
        if len(sys.argv) == 4:
            self.server = sys.argv[1]
            self.username = sys.argv[2]
            self.passw = sys.argv[3]
            self.quit = False
        else:
            print "Invalid argument count. Please rerun and use the format after script name:\nipaddress username password"
            self.quit = True