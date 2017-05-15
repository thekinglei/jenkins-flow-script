__author__ = 'Administrator'

import conf
import fabric
class DeployServer():
    def __init__(self,IP, Port, WorkPath):
        self.Server_IP = IP
        self.Port = Port
        self.WorkPath = WorkPath

    def install_package(self):
        '''
        将编译后的包安装到服务器上
        :return:
        '''
        print "checkout package to server"

    def start(self):
        '''
        启动服务器
        :return:
        '''
        print "start server"

    def stop(self):
        '''
        stop service
        :return:
        '''
        print "[INFO]stop service"


    def restart(self):
        '''
        :return:
        '''
        self.stop()
        self.start()

    def js_server_start(self):
        '''
        start js-server
        :return:
        '''

    
