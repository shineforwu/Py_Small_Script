# -*- coding: utf-8 -*-
# @Author: Shine Wu
# @Date:   2025-02-15 14:30:29
# @Last Modified by:   Shine Wu
# @Last Modified time: 2025-02-15 17:13:45
# @Description:This is a class for logging info.

from datetime import datetime
from enum import Enum
import os

class LogLevel(Enum):
    DEBUG = (10, "DEBUG")
    INFO = (20, "INFO")
    WARNING = (30, "WARNING")
    ERROR = (40, "ERROR")
    CRITICAL = (50, "CRITICAL")# critical level 是最严重的



class My_Logger:

    def __init__(self, is_to_wirte=1,log_base_name="MyLog",module_name="Test", log_level=LogLevel.DEBUG):
        self._base_file_name = log_base_name
        self._log_file = log_base_name+".log"
        self._log_level = log_level
        self._is_to_wirte = is_to_wirte
        self._module_name = module_name
        _num=0
    def set_module_name(self,module_name):
        self._module_name = module_name
    def set_log_base_name(self,log_base_name):
        self._base_file_name = log_base_name
        self._log_file = log_base_name+".log"

    def log(self, level, message):
        if level >= self._log_level:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            level_name = self._log_level.value[1]
            print(f"[{timestamp}] [{level_name}] [{self._module_name}]: [{message}"+"\n")
            if self._is_to_wirte == 1:
                self.ensure_log_file_exists(self._log_file)
                with open(self._log_file, 'a') as file:  # 使用 'a' 模式追加内容
                    file.write(f"[{timestamp}] [{level_name}] [{self._module_name}]: [{message}"+"\n")
                    file.close()

    def info(self, message):
        self.log(LogLevel.INFO, message)

    def debug(self, message):
        self.log(LogLevel.DEBUG, message)

    def warning(self, message):
        self.log(LogLevel.WARNING, message)

    def error(self, message):
        self.log(LogLevel.ERROR, message)

    def critical(self, message):
        self.log(LogLevel.CRITICAL, message)

    def ensure_log_file_exists(self):
        num=0
        if num<self._num:
            num=self._num
        while True:
            fileName = f"{self._base_file_name}_{num}.log"
            if not os.path.exists(fileName):
                with open(fileName, 'w') as file:
                    file.write(f"Log file created on {datetime.datetime.now()}\n")
                    file.close()
                self._log_file=fileName    
                return
            else: 
                file_size = os.path.getsize(fileName) # 获取文件大小
                if file_size > 1024*1024*1024:
                    self._num += 1
                    num+=1
                else:
                    self._log_file=fileName
                    return

My_Utils/__init__.py
                
        
