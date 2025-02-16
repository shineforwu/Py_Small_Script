# -*- coding: utf-8 -*-
# @Author: Shine Wu
# @Date:   2025-02-15 16:32:15
# @Last Modified by:   Shine Wu
# @Last Modified time: 2025-02-16 01:13:40
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
        self.label_1 = tk.Label(parentObj, text="请输入ip起始地址:", font=("Arial", 12))
        self.label_1.grid(row=0, column=0, pady=5, padx=5)
        self.ip_s_txt = tk.Entry(parentObj, font=("Arial", 12))
        self.ip_s_txt.grid(row=0, column=1, pady=5, padx=5)
        
        
        self.label_2 = tk.Label(parentObj, text="请输入ip结束地址:", font=("Arial", 12))
        self.label_2.grid(row=0, column=2, pady=5, padx=5)
        self.ip_e_txt = tk.Entry(parentObj, font=("Arial", 12))
        self.ip_e_txt.grid(row=0, column=3, pady=5, padx=5)
        

        self.label_3 = tk.Label(parentObj, text="请输入port起始地址:", font=("Arial", 12))
        self.label_3.grid(row=1, column=0, pady=5, padx=5)
        self.port_s_txt = tk.Entry(parentObj, font=("Arial", 12))
        self.port_s_txt.grid(row=1, column=1, pady=5, padx=5)

        
        self.label_4 = tk.Label(parentObj, text="请输入port结束地址:", font=("Arial", 12))
        self.label_4.grid(row=1, column=2, pady=5, padx=5)
        self.port_e_txt = tk.Entry(parentObj, font=("Arial", 12))
        self.port_e_txt.grid(row=1, column=3, pady=5, padx=5)
        
        # 添加水平分割线
        self.separator = ttk.Separator(parentObj, orient='horizontal')
        self.separator.grid(row=2,columnspan=4,sticky='ew', pady=10)

        self.reset_ip_btn = tk.Button(parentObj, text="重置 ip 信息", command=self.reset_info)
        self.reset_ip_btn.grid(row=3,column=0 ,pady=5, padx=5)

        self.reset_mes_btn = tk.Button(parentObj, text="清空信息", command=self.clear_mes)
        self.reset_mes_btn.grid(row=3,column=1 ,pady=5, padx=5)

        self.scaner_btn = tk.Button(parentObj, text="扫描", command=self.run_scaner)
        self.scaner_btn.grid(row=3,column=3 ,pady=5, padx=5)

        # 添加水平分割线
        self.separator_2 = ttk.Separator(parentObj, orient='horizontal')
        self.separator_2.grid(row=4,columnspan=4,sticky='ew', pady=10)

        self.test_btn = tk.Button(parentObj,text="Test",font=("Arial", 12),command=self.testFun)
        self.test_btn.grid(row=5, pady=5, padx=5)
        
        self.label_5 = tk.Label(parentObj, text="消息:", font=("Arial", 12))
        self.label_5.grid(row=6, column=0, pady=5, padx=5)
        self.result_text = tk.Text(parentObj)
        self.result_text.grid(row=7,column=0, columnspan=4,sticky='nsew' ,pady=10, padx=10)

        self.reset_info()
        self.clear_mes()
    def reset_info(self):
        self.ip_s_txt.delete(0, tk.END)
        self.ip_s_txt.insert(0,"192.168.0.90")
        self.ip_e_txt.delete(0, tk.END)
        self.ip_e_txt.insert(0,"192.168.0.100")

        self.port_s_txt.delete(0, tk.END)
        self.port_s_txt.insert(0,"5660")
        self.port_e_txt.delete(0, tk.END)
        self.port_e_txt.insert(0,"5669")

    def clear_mes(self):
        self.result_text.delete(1.0, tk.END)

    def run_scaner(self):
        self.logic.set_ip(self.ip_s_txt.get(),self.ip_e_txt.get(),int(self.port_s_txt.get()),int(self.port_e_txt.get()))
        self.logic.Run_Port_Scanner()
        
    def testFun(self):
        self.logic.TestFunc()
    def addStringToView(self,string):
        self.result_text.insert(tk.END,string)



