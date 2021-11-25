import os
import sys
import re

class Com:
    def __init__(self, command):
        self.command = command
        self.version = "1.0"
        self.ch_list = ["\"", "'", "::"]
        self.command_list = {
            "test": self.test,
            "echo": self.echo,
            "restart": self.restart,
            "version": self.ver,
            "exc-file": self.fileexecuter,
            "exit": sys.exit,
        }
        self.execute()
    
    def execute(self):
        try:
            command = self.command.split()[0]
        except IndexError:
            pass
            command=""
            #Boş komut
        if command in self.command_list:
            exec("self.command_list[command]()")
        elif command in self.ch_list:
            pass
        else:
            try:
                print(f"InvalidCommand: {command.split()[0]}")
            except IndexError:
                pass
    def fileexecuter(self):
        print("Yakında...")

    def echo(self):
        #tırnak içindeki yazıları alır
        print(re.findall('"([^"]*)"', self.command.split()[1]))

    def ver(self):
        print(self.version)

    def restart(self):
        os.system(f"python {__file__}")
        sys.exit()

    def test(self):
        print("Merhaba Vore")
print("Vore Shell")
history_list=[]
while True:
    try:
        command=input(">>")
        if command == "":
            pass
        else:
            history_list.append(command)
        if command == "history":
            print(history_list)
        else:
            Com(command)
    except KeyboardInterrupt:
        sys.exit()