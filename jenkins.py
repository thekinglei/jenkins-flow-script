#coding=utf-8
'''
jenkins build 脚本python化
'''

import coverage
import commands as cs
from COMPILE import build_func
from optparse import OptionParser
import os

def jenkins_compile():
    print
    print "[INFO]开始编译"
    print "[INFO] start to exec compile"
    print "mvn compile -Dmaven.test.skip=true"
    print "[INFO]end"

#def clone(giturl,branch):
#    print '[INFO] start to clone code from gitlab:giturl'
#    print "[INFO]giturl:"
#    print "[INFO]branch:"

def package_info():
    print "\n\n\n"
    print "[INFO]打包信息-start"
    print "[INFO]WORKSPACE path %s"%(os.environ['WORKSPACE'])
    print "[INFO]JOB_NAME %s"%(os.environ['JOB_NAME'])
    print "[INFO]BUILD_NUMBER %s"%(os.environ['BUILD_NUMBER'])
    print "[INFO]BUILD_ID %s"%(os.environ['BUILD_ID'])
    print "[INFO]GIT_URL %s"%(os.environ['GIT_URL'])
    print "[INFO]jenkins_build_id:"
    CUR_SHA = cs.getstatusoutput("git rev-parse HEAD")[1]
    print "[INFO]COMMIT_ID %s"%(CUR_SHA)
    print "[INFO]打包信息-end"
    print "\n\n\n"
    f = open(os.environ['WORKSPACE'] + '/package_info.txt', 'w')
    f.write("[INFO]WORKSPACE path %s"%(os.environ['WORKSPACE']))
    f.write("[INFO]JOB_NAME %s"%(os.environ['JOB_NAME']))
    f.write("[INFO]BUILD_NUMBER %s"%(os.environ['BUILD_NUMBER']))
    f.write("[INFO]BUILD_ID %s"%(os.environ['BUILD_ID']))
    f.write("[INFO]GIT_URL %s"%(os.environ['GIT_URL']))
    f.write("[INFO]COMMIT_ID %s"%(CUR_SHA))
    f.close()


def deploy():
    '''
    调用rundeck部署
    '''
    print "\n\n\n"
    print "[INFO]开始部署机器"
    print "[INFO]server IP:"
    print "[INFO]start to deploy server"
    print "[INFO]deploy success !"
    print "\n\n\n"


def third_catalog_main():
    '''
    三级目录调用方式
    '''
    print "[INFO]开始编译部署"
    print "[INFO]start CICD"

def package_store():
    '''
    保存编译生成的包或者文件，提交svn或者文件系统
    '''
    print "[INFO]UPLOAD SUCCESS !"

def sid_main(product):
    '''
    Sid方式调用部署
    '''
    global PRODUCT
    global COMPONENT
    PRODUCT = product
    jenkins_job_name = os.environ['JOB_NAME']
    COMPONENT = jenkins_job_name.split('__')[1]
    #component = jenkins_job_name.split('__')[1]
    FROM = jenkins_job_name.split('__')[0].split('-')[0]
    TO = jenkins_job_name.split('__')[0].split('-')[2]
    print COMPONENT, FROM, TO

    #-----------开始构建 ------------
    print "[INFO]开始编译部署"
    print "[INFO]start CICD"

    #-----------打包信息 ------------
    package_info()

    #-----------开始编译 ------------
    print "[INFO]开始编译"
    eval("build_func.%s_build_func()"% PRODUCT)

    #-----------包管理 ------------
    print "[INFO]提交包到svn"

    #-----------开始部署 ------------
    print "[INFO]部署信息"
    deploy()

    #-----------发布结束 ------------
    print "[INFO]发布结束"
if __name__ == "__main__":
    #parser = OptionParser()
    #parser.add_option("-p", "--product", action="store", type="string", dest="product", help="product_name")
    #parser.add_option("-c", "--component", action="store", type="string", dest="component", help="component_name")

    sid_main('ccs')
