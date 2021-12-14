"""
        Vore MIT © 2021 Zoda

Linkler / Links
Github: https://github.com/kerem3338/vore
License / Lisans: https://github.com/kerem3338/vore/blob/main/LICENSE

Türkçe
Vore yazılımcılar için geliştirilmiş bir konsoldur içersinde daha kolay yazılım geliştirmeyi sağlamak için
araçlar bulunur.

English
To enable easier software development in a console developed for Vore developers.
tools are available.
"""
import os
import sys
import re


class Com:
    def __init__(self, command):
        self.command = command
        self.version = "1.1"
        self.ch_list = ["\"", "'", "::"]
        self.command_list = {
            "test": self.test,
            "echo": self.echo,
            "restart": self.restart,
            "version": self.ver,
            "exc-file": self.fileexecuter,
            "exit": sys.exit,
            "cominfo": self.cominfo,
            "clear": self.clear
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
        """Yakında"""
        print("Yakında...")

    def cominfo(self):
        """Gets command info"""
        if self.command.split()[1] in self.command_list:
            com=f"print(self.command_list[self.command.split()[1]].__doc__)"
            eval(com)
        else:
            print("Error: Command not found!")

    def clear(self):
        """clear screen"""
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("cls")

    def echo(self):
        try:
            print(re.findall('"([^"]*)"', self.command)[0])
        except IndexError:
            print("String Error: quotes not closed")

    def ver(self):
        """return vore version"""
        print(self.version)

    def restart(self):
        os.system(f"python {__file__}")
        sys.exit()

    def test(self):
        print("Merhaba Vore!")

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
    except EOFError:
        sys.exit()