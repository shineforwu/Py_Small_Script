# -*- coding: utf-8 -*-
# @Author: Shine Wu
# @Date:   2025-02-15 16:32:15
# @Last Modified by:   Shine Wu
# @Last Modified time: 2025-02-15 16:49:00
# @Description:This is the window  for port scanner  by tkinter.

import tkinter as tk
from tkinter import ttk

from My_Utils.MyLogger import MyLogger

class Port_Scanner_view:
    def __init__(self,root:tk.Tk):
        self.root = root
        self.logger = MyLogger()
        self.logger.set_log_base_name("MyTest")
        self.logger.set_module_name("Port_Scanner_view")
        self.logger.info("Port_Scanner_view initialized")
    
    def addNotebookToRoot(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')
        self.tabnote = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text='扫描端口')



