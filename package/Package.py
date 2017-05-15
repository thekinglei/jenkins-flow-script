#coding-=utf-8
import CONF.package_store_conf as cc
import CONF.get_property as cp
import os
import commands as cds
__author__ = 'wangleiaf'

class package_manage():
    def __init__(self, product_name):
        self.product = product_name
        self.jenkins_job_name = os.environ['JOB_NAME']
        self.FROM = self.jenkins_job_name.split('__')[0].split('-')[0]
        self.TO = self.jenkins_job_name.split('__')[0].split('-')[2]
        self.component_name = self.jenkins_job_name.split('__')[1]
        self.Svn_info = cp.get_svn_info(self.TO, cp.get_sid(self.product, self.component_name))


    def get_component(self):
        return self.component_name

    def submit_package(self):
        print 'commit to svn:test inte moni prod'

    def update_package(self):
        print "[INFO]update svn"


    def get_from_path(self):
        if self.FROM == "BUILD":
            from_path = self.output_path(self.product)
            return from_path
        else:
            from_path = cc.BUILD_DATA + '/' + self.product + '/' + self.component_name + '/' + self.FROM + '_DOWNLOAD'
            return from_path

    def get_to_path(self):
        to_path = cc.BUILD_DATA + '/' + self.product + '/' + self.component_name + '/' + self.TO + "_SUBMIT"
        return to_path

    def get_package_info_file(self):
        package_info_file = self.get_to_path() + '/' + 'package_info.txt'
        return package_info_file

    def outputpath_to_submitpath(self):
        output_path = self.output_path()
        commands_list = "rsync -av --delete %s %s" % (output_path)
        #cds.getstatusoutput("yrsnc")

    def output_path(self):
        if self.component_name:
            OUTPUT_PATH = cc.OUTPUT_PATH + "/" + self.product + '/' + self.component_name + "/" + self.TO
        else:
            raise Exception("[ERROR] component_name is null")
        return OUTPUT_PATH

    def output_path_clean(self):
        OUTPUT_PATH = self.output_path()
        result = cds.getstatusoutput("rm -rf %s;mkdir -p %s" % (OUTPUT_PATH, OUTPUT_PATH))
        if result[0] ==0:
            return 1
        else:
            raise Exception("[ERROR]clean OUTPUT_PATH FAILED")


