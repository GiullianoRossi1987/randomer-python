# coding = utf-8
# using namespace std
import json
from typing import AnyStr
from time import strftime


class Logs(object):
    """
    """
    log_file = AnyStr
    doc_logs = list()
    got_data = False

    class UnloadedLogs(Exception):
        """
        """
        args = "The system can't do that action without the log file loaded"
    
    class InvalidLogFile(Exception):
        """
        """
        args = "That's not a valid logs file!"
    
    class AlreadyLodedLogs(Exception):
        """
        """
        args = "The system's already connected to a logs file!"
    
    class InvalidFailuresValue(Exception):
        args = "That's not a valid number of failures!"

    class InvalidFailureCode(Exception):
        args = "That's not a valid Failure code!"

    @staticmethod
    def check_logs_file(file_name: AnyStr, creating_file = False):
        """
        """
        sp = str(file_name).split(".")
        to_create = ""
        if creating_file is True: to_create = "+"
        if sp[-1] != "json": return False
        try:
            with open(file_name, "r"+to_create) as log_test:
                dt = json.loads(log_test.read())
                # if dt is not list: return False
        except FileNotFoundError:
            return False
        return True
    
    def commit(self):
        """
        """
        if self.got_data is False: raise self.UnloadedLogs()
        with open(self.log_file, "w") as logs_file:
            dumped_data = json.dumps(self.doc_logs)
            logs_file.write(dumped_data)
        del dumped_data
    
    def __init__(self, logs_file = "./core/logs.json"):
        """
        """
        if self.check_logs_file(logs_file) is False: raise self.InvalidLogFile()
        if self.got_data is True: raise self.AlreadyLodedLogs()
        self.log_file = logs_file
        with open(self.log_file, "r") as logs:
            self.doc_logs = json.loads(logs.read())
        self.got_data = True
    
    def add_log(self, action: str, failures = 0, failure_code = "0000000"):
        """
        """
        if self.got_data is False: raise self.UnloadedLogs()
        if failures < 0: raise self.InvalidFailuresValue()
        if len(failure_code) <= 0: raise self.InvalidFailureCode()
        date_time = strftime("%Y-%m-%d %H:%m:%S")
        dt_dict = {
            "DateTime": date_time,
            "Action": action,
            "Failures": failures,
            "Code": failure_code
        }
        self.doc_logs.append(dt_dict)
        del dt_dict
        del date_time
        self.commit()  # automatically
    
    def clear_logs(self):
        """
        """
        if self.got_data is False: raise self.UnloadedLogs()
        self.doc_logs = []
        self.commit()

    def show_logs(self) -> str:
        """

        :return:
        """
        rs = ""
        for log_item in self.doc_logs:
            rs += f"[{log_item['DateTime']}] - {log_item['Action']} - {log_item['Failures']} ({log_item['Code']})\n"
        return rs

    def close(self):
        """

        :return:
        """
        if self.got_data is False: raise self.UnloadedLogs()
        self.log_file = ""
        self.doc_logs = []
        self.got_data = False
