# -*- coding: utf-8 -*-
# @Author: Shine Wu
# @Date:   2025-02-15 19:54:09
# @Last Modified by:   Shine Wu
# @Last Modified time: 2025-02-16 13:22:08

from socket import *
import threading
import ipaddress

class Port_Scanner_Logic:
    def __init__(self,logger):
        self._send_mes_listeners  = []
        self.logger = logger
        self.logger.info("Port_Scanner_Logic init")
        self.thread_list = []
        self.thread_lock = threading.Lock()
        self.thread_event = threading.Event()
        # 确保线程安全的锁
        self.lock = threading.Lock()
        self._ip_start=ipaddress.ip_address('192.168.0.1')
        self._ip_end=ipaddress.ip_address('192.168.0.1')
        self._port_start:int=0
        self._port_end:int=0
        self._thread_is_running=False
    def register_send_mes_listener(self, listener ):
        #注册事件处理函数  注册监听
        self._send_mes_listeners.append(listener )

    def _trigger_send_mes(self,event_data):
        """
        触发事件，遍历事件监听器列表并调用每个处理函数
        """
        for listener  in self._send_mes_listeners:
            listener (event_data)

    def TestFunc(self):
        self._trigger_send_mes("This is a test")

    def set_ip(self,ip_start,ip_end,port_start:int,port_end:int):
        self._ip_start=ipaddress.ip_address(ip_start)
        self._ip_end=ipaddress.ip_address(ip_end)
        self._port_start=port_start
        self._port_end=port_end

    def Run_Port_Scanner(self):
        #创建线程
        thread=threading.Thread(target=self._Port_Scan)
        if self._thread_is_running==True:
            return
        self._thread_is_running=True
        thread.start()
        # 等待线程完成
        # thread.join()
        # 设置线程运行标志为 False
        self._thread_is_running = False
        


    def _Port_Scan(self):
        self.logger.info("Port_Scanner start")
        for ip_int in range(int(self._ip_start), int(self._ip_end) + 1):
            ip = ipaddress.ip_address(ip_int)
            for port in range(self._port_start,self._port_end+1):   
                result=-100                 
                try:
                    # 创建一个 TCP/IP 套接字
                    s = socket(AF_INET, SOCK_STREAM)
                    # 设置超时时间为1秒
                    s.settimeout(5) 
                    result = s.connect_ex((ip, port))
                    s.close()
                    if result == 0:
                        with self.lock:
                            self._trigger_send_mes(f"IP: {ip}, 端口: {port} 可连接\n")
                    else:
                        with self.lock:
                            self._trigger_send_mes(f"IP: {ip}, 端口: {port} 不可连接  and result :{result}\n")
                except Exception as e:
                    self.logger.error(f"IP: {ip}, 端口: {port}  result :{result} error\n")
                    self.logger.error(e)
                    
        self._thread_is_running = False
        self.logger.info("Port_Scanner end")
                    
            
