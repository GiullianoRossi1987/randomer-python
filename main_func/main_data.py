# coding = utf-8
# using namespace std
from random import randint
# from typing import AnyStr
from main_func.logger import Logs

main_logs = Logs("./main_func/logs.json")  # visible on the APP_ROOT


class CPFSystem(object):
    """

    """
    nums = int

    class InvalidCPFValue(TypeError):
        args = "That's not a valid CPF Character!"

    class InvalidCPF(Exception):
        args = "That's not a valid CPF"

    def load_cpf_data(self, raw_cpf: str) -> str:
        """

        :param raw_cpf:
        :return:
        """
        dt = ""
        for i in raw_cpf:
            try:
                if i == "." or i == "-": pass
                a = int(i)
            except TypeError: pass
            except ValueError: pass
            else:
                dt += str(a)
        return dt

    def check_valid_cpf(self, cpf: str) -> bool:
        """

        :return:
        """
        rt = self.load_cpf_data(cpf)
        if len(rt) != 11: raise self.InvalidCPF()
        som = 0
        sam = 10
        for i in range(0, 9):
            if sam < 2: break
            som += int(rt[i]) * sam
            sam -= 1
        rt_sum = 11 - (som % 11)
        sum1 = 0
        sam2 = 11
        for a in range(0, 9):
            if sam2 < 2: break
            sum1 += int(rt[a]) * sam2
            sam2 -= 1
        rt2 = 11 - (sum1 % 11)
        if rt_sum > 9 and rt[-2] == "0": return True
        elif rt2 > 9 and rt[-1] == "0": return True
        elif str(rt_sum) == rt[-2] and str(rt2) == rt[-1]: return True
        else: return False

    def create_valid_cpf(self) -> str:
        """

        :return:
        """
        while True:
            try:
                ft1: str = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
                ft2: str = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
                ft3: str = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
                pp: str = str(str(randint(0, 9)) + str(randint(0, 9)))
                tt_cpf = f"{ft1}.{ft2}.{ft3}-{pp}"
                if self.check_valid_cpf(tt_cpf) is True: return tt_cpf
                else: continue
            except self.InvalidCPF: pass

    def create_invalid_cpf(self) -> str:
        """

        :return:
        """
        tt_cpf = ""
        while True:
            try:
                ft1: str = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
                ft2: str = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
                ft3: str = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
                pp: str = str(randint(0, 9)) + str(randint(0, 9))
                tt_cpf = f"{ft1}.{ft2}.{ft3}-{pp}"
                if self.check_valid_cpf(tt_cpf) is False:return tt_cpf
                else: continue
            except self.InvalidCPF: return tt_cpf

    def __init__(self): pass


class CNPJSystem(object):
    """

    """

    class InvalidCNPJ(Exception):
        args = "That's not a valid CNPJ"

    class InvalidChar(ValueError):
        args = "That's not a valid Char to a CNPJ number!"

    def load_cnpj_value(self, raw_cnpj: str) -> str:
        """

        :param raw_cnpj:
        :return:
        """
        rt = ""
        for i in raw_cnpj:
            try:
                a = int(i)
            except ValueError or TypeError: pass
            else:
                rt += str(a)
        if len(rt) != 14: raise self.InvalidCNPJ()
        return rt

    def check_valid_cnpj(self, cnpj: str) -> bool:
        """

        :param cnpj:
        :return:
        """
        rt = self.load_cnpj_value(cnpj)
        pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        sum1 = 0
        for value1 in range(0, 12):
            sum1 += int(rt[value1]) * pesos[value1]
        sum2 = 0
        for value2 in range(0, 13):
            if value2 == 0:
                 sum2 += int(rt[value2]) * 6
                 continue
            else: sum2 += int(rt[value2]) * pesos[value2 -1]
        mod_v1 = 11 - (sum1 % 11)
        mod_v2 = 11 - (sum2 % 11)
        if (mod_v1 < 2 and rt[-2] == "0") and (mod_v2 < 2 and rt[-1] == "0"): return True
        elif str(mod_v1) == rt[-2] and str(mod_v2) == rt[-1]: return True
        else: return False

    def create_valid_cnpj(self) -> str:
        """

        :return:
        """
        while True:
            try:
                rt1 = (str(randint(0, 9)) + str(randint(0, 9)))
                rt2 = (str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)))
                rt3 = (str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)))
                nums = (str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)))
                dv = str(str(randint(0, 9)) + str(randint(0, 9)))
                cnpj = f"{rt1}.{rt2}.{rt3}/{nums}-{dv}"
                if self.check_valid_cnpj(cnpj) is True: return cnpj
                else: pass
            except self.InvalidCNPJ() or self.InvalidChar(): pass

    def create_invalid_cnpj(self) -> str:
        """

        :return:
        """
        cnpj = ""
        while True:
            try:
                rt1 = (str(randint(0, 9)) + str(randint(0, 9)))
                rt2 = (str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)))
                rt3 = (str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)))
                nums = (str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)))
                dv = str(str(randint(0, 9)) + str(randint(0, 9)))
                cnpj = f"{rt1}.{rt2}.{rt3}/{nums}-{dv}"
                if self.check_valid_cnpj(cnpj) is True: pass
                else: return cnpj
            except self.InvalidCNPJ() or self.InvalidChar(): return cnpj














