# coding = utf-8
# using namespace std
from main_func.main_data import ArgvSystem
from main_func.screens import CNPJSystemScreens, CPFSystemScreens
from os import system
from sys import platform

to_windows = platform == "windows"

help_str = """
"""

about_ = """
"""

# checks the args
ArgvSystem()

# if not args
while True:
    # index screen
    if to_windows is True: system("cls")
    else: system("clear")
    while True:
        print("""
        
[1] CPF System
[2] CNPJ System
[3] Help
[4] About
[5] Exit
        """)
        opc = int(input(">>> "))
        conf = int(input("Confirm choice?\n[1]Yes\n[2]No\n>>> "))
        if conf == 1: break
    if opc == 1:
        try:
            CPFSystemScreens()
        except CPFSystemScreens.EndUsage: continue
    elif opc == 2:
        try:
            CNPJSystemScreens()
        except CNPJSystemScreens.EndUsage: continue
    elif opc == 3:
        print(help_str)
        input("<<press any button to return>>")
        continue
    elif opc == 4:
        print(about_)
        input("<<press any button to return>>")
        continue
    elif opc == 5: exit(0)
    else:
        input("That's not a valid option!\n<<press any button to return>>")
        continue
# end of the code :)



