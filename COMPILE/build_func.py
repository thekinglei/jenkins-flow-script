#coding=utf-8
__author__ = 'Administrator'
import commands as cds
import os
#import package.Package as pp
from package.Package import package_manage

def ccs_build_func():
    #pp_obj = pp.package_manage(ccs)
    pp_obj = package_manage('ccs')
    component = pp_obj.get_component()
    if component == "wangleiaf_scm_test":
        print "[INFO]compile start"
        result = cds.getstatusoutput('mvn clean  -U package -Dmaven.test.skip=true')
        if result[0] == 0:
            print "[INFO]compile Success !"
            output_path = pp_obj.output_path()
            pp_obj.output_path_clean()
            workspace = os.environ['WORKSPACE']
            commands_list = "cp %s/target/wangleiaf-1.0.0.jar %s;cp %s/package_info.txt %s"%(workspace,output_path,workspace,output_path)
            res2 = cds.getstatusoutput(commands_list)
            if res2[0]:
                raise Exception("[ERROR] %s"%res2[1])
            else:
                return 1
        else:
            raise Exception("[ERROR] compile Failed! \n %s"%(result[1]))
    else:
        print "don't found %s"%component
        raise Exception("[ERROR]don't found %s"%component)

def bss_build_func(component):
    if component == "test":
        print 'test'
    else:
        raise Exception("[ERROR]don't found %s"%component)