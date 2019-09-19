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










