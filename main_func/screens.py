# coding = utf-8
# using namespace std
from time import sleep
from main_func.main_data import CPFSystem
from main_func.main_data import CNPJSystem
from sys import platform
from os import system
from main_func.logger import Logs

local_plat: bool = platform == "windows"


class CPFSystemScreens(object):
    """

    """

    class InvalidOption(Exception):
        args = "That's not a valid Option!"

    class EndUsage(SystemExit):
        args = "End of the use!"

    help_str = """
    """

    logger = Logs("./main_func/logs.json")

    def __init__(self):
        """

        """
        local_obj = CPFSystem()
        while True:
            # main screen
            if local_plat is True: system("cls")
            else: system("clear")
            while True:
                # here goes the string from the command (linux) 'figlet'
                print("""

[1] Validate CPF
[2] Create Valid CPF
[3] Create Invalid CPF
[4] Help
[5] Exit
                """)
                opc = int(input(">>> "))
                con = int(input("Confirm?\n[1]Yes\n[2]No\n>>> "))
                if con == 1: break
            if opc == 1:
                c = True
                while True:
                    cpf_input = str(input("Type the CPF value (mask = '###.###.###-##'): "))
                    con = int(input("Confirm Data? \n[1]Yes\n[2]No\n[3]Abort\n>>> "))
                    if con == 3:
                        c = False
                        break
                    if con == 1: break
                if c is True:
                    try:
                        dt = local_obj.check_valid_cpf(cpf_input)
                        if dt is True:
                            print("That's a valid CPF!\nValue: '"+cpf_input+"'")
                        else:
                            print("That's not a valid CPF\nValue: '"+cpf_input+"'")
                    except local_obj.InvalidCPF or local_obj.InvalidCPFValue:
                        print("That's not a valid CPF\nValue: '" + cpf_input + "'")
                    finally:
                        self.logger.add_log(f"Check Valid CPF. Value = '{cpf_input}'", 1, "04004")
                    self.logger.add_log(f"check valid CPF. Value = '{cpf_input}'")
                continue
            elif opc == 2:
                a = local_obj.create_valid_cpf()
                print("There's: "+a)
                self.logger.add_log(f"deployed valid CPF '{a}'")
                input("<<press any button to return>>")
                continue
            elif opc == 3:
                sleep(2)
                a = local_obj.create_invalid_cpf()
                print("There's: "+a)
                input("<<press any button to return>>")
                continue
            elif opc == 4:
                sleep(2)
                print(self.help_str)
                input("<< press any button to return>>")
                continue
            elif opc == 5:
                self.logger.close()
                raise self.EndUsage()
            else:
                print("That's not a valid option!")
                continue


class CNPJSystemScreens(object):
    """
    """
    local_obj = CNPJSystem()
    help_txt = """
    """

    class InvalidOption(Exception):
        args = "That's not a valid Option"

    class EndUsage(SystemExit):
        args = "End of usage!"

    logger = Logs("./main_func/logs.json")

    def __init__(self):
        """

        """
        while True:
            # clear the command line screen
            if local_plat is True: system("cls")
            else: system("clear")
            while True:
                print("""
[1] Validate CNPJ
[2] Create Valid CNPJ
[3] Create Invalid CNPJ
[4] Help
[5] Exit
                """)
                opc = int(input(">>> "))
                con1 = int(input("Confirm?\n[1]Yes\n[2]No\n>>> "))
                if con1 == 1: break
            if opc == 1:
                c = True
                while True:
                    cnpj = str(input("Type the CNPJ: "))
                    con2 = int(input("Confirm?\n[1]Yes\n[2]No\n[3]Abort\n>>> "))
                    if con2 == 3:
                        c = False
                        break
                    if con2 == 1: break
                if c is True:
                    try:
                        rs_vl = self.local_obj.check_valid_cnpj(cnpj)
                        if rs_vl is True:
                            print("That's CNPJ is valid!")
                        else:
                            print("That's a invalid CNPJ")
                        self.logger.add_log(f"validation CNPJ '{cnpj}'")
                    except self.local_obj.InvalidCNPJ:
                        print("That's a invalid CNPJ")
                    finally:
                        self.logger.add_log(f"validation CNPJ '{cnpj}'", 1, "04004")
                continue
            elif opc == 2:
                a = ""
                try:
                    sleep(2)
                    a = self.local_obj.create_valid_cnpj()
                    print("Valid CNPJ: "+a)
                    self.logger.add_log(f"deployed valid CNPJ '{a}'")
                    input("<<press any button to return>>")
                except Exception as e:
                    self.logger.add_log(f"deployed valid CNPJ '{a}'", 1, "04004")
                    raise e  # to any error
                continue
            elif opc == 3:
                a = ""
                try:
                    sleep(2)
                    a = self.local_obj.create_invalid_cnpj()
                    print("Invalid CNPJ: "+a)
                    self.logger.add_log(f"deployed invalid CNPJ '{a}'")
                    input("<<press any button to return>>")
                except Exception as e:
                    self.logger.add_log(f"deployed invalid CNPJ '{a}'", 1, "04004")
                    raise e
                continue
            elif opc == 4:
                sleep(2)
                print(self.help_txt)
                input("<<press any button to return>>")
                continue
            elif opc == 5:
                self.logger.close()
                raise self.EndUsage()
            else:
                print("That's not a valid option!")
                continue




