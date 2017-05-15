__author__ = 'Administrator'

import commands as cs
class java_compile():
    def __init__(self,WorkPath):
        self.WorkPath = WorkPath

    def mvn_package(self):
        result = cs.getstatusoutput("cd %s;mvn package -Dmaven.test.skip=true"%(self.WorkPath))
        if result[0] ==0:
            print "[INFO]BUILD SUCCESS!"

        else:
            print "[ERROR]BUILD FAILED"
            print result[1]
            raise("[ERROR]commands 'mvn package'run failed")

    def mvn_deploy(self,):
        print "[INFO]mvn deploy !"
