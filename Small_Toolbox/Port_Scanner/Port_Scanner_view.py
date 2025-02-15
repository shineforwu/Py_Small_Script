# -*- coding: utf-8 -*-
# @Author: Shine Wu
# @Date:   2025-02-15 16:32:15
# @Last Modified by:   Shine Wu
# @Last Modified time: 2025-02-15 21:15:52
# @Description:This is the window  for port scanner  by tkinter.

import tkinter as tk
from tkinter import ttk

from Port_Scanner.Port_Scanner_Logic import Port_Scanner_Logic


class Port_Scanner_view:
    def __init__(self,root,logger):
        self.root = root #主窗口的top 部分
        self.logger = logger
        self.logger.set_module_name("Port_Scanner")
        self.logger.info("Port_Scanner_view initialized")

        self.logic= Port_Scanner_Logic(logger)
        self.logic.register_send_mes_listener(self.addStringToView)
        self._addNotebookToRoot()

    
    def _addNotebookToRoot(self):
        
        self.tabnote = ttk.Frame(self.root)
        self.root.add(self.tabnote, text='扫描端口')

        self._addElementFun(self.tabnote)

    
    def _addElementFun(self, parentObj):
        self.label_1 = tk.Label(parentObj, text="请输入ip:", font=("Arial", 12))
        self.label_1.grid(row=0, column=0, pady=5, padx=5)
        self.label_2 = tk.Label(parentObj, text="请输入ip:", font=("Arial", 12))
        self.label_2.grid(row=1, column=0, pady=5, padx=5)
        self.label_3 = tk.Label(parentObj, text="请输入ip:", font=("Arial", 12))
        self.label_3.grid(row=2, column=0, pady=5, padx=5)
        self.label_11 = tk.Label(parentObj, text="请输入ip:", font=("Arial", 12))
        self.label_11.grid(row=0, column=1, pady=5, padx=5)
        self.label_12 = tk.Label(parentObj, text="请输入ip:", font=("Arial", 12))
        self.label_12.grid(row=1, column=1, pady=5, padx=5)
        self.label_13 = tk.Label(parentObj, text="请输入ip:", font=("Arial", 12))
        self.label_13.grid(row=2, column=1, pady=5, padx=5)

        self.test_btn = tk.Button(parentObj,text="Test",font=("Arial", 12),command=self.testFun)
        self.test_btn.grid(row=4, pady=5, padx=5)
        self.result_text = tk.Text(parentObj)
        self.result_text.grid(row=5, pady=5, padx=5)

    def testFun(self):
        self.logic.TestFunc()
    def addStringToView(self,string):
        self.result_text.insert(tk.END,string)



