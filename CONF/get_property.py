#coding=utf-8
__author__ = 'wangleiaf'



import ConfigParser as cr
import os

build_data = "/var/data/com/build_data"
build_script = '/opt/py_script/CONF'

def get_sid(project, component):
    '''
    :param project: 项目名，类似gitlab上组名
    :param component: 工程名，类似gitlab上库名
    :return:返回sid，即服务序列号
    '''
    '''
    :param project:
    :param component:
    :return:
    '''
    cf = cr.ConfigParser()
    #conf_file = os.getcwd() + '/' + project
    conf_file = build_script + '/' + 'cmdb.conf'
    print conf_file
    cf.read(conf_file)
    return cf.get(component, 'sid')

def set_sid(project, component, sid):
    '''
    :param project:
    :param component:
    :return:
    '''
    cf = cr.ConfigParser()
    conf_file = os.getcwd() + '/' + project
    cf.read(conf_file)
    cf.set(component, 'sid', sid)


def submit_data_path(project, component):
    '''
    :param project:
    :param component:
    :return:编译数据存放地址
    '''
    submit_path = build_data + '/' + project + '/' + component
    return submit_path


def output_path(project, component):
    '''
    :param project:
    :param component:
    :return:output_path是代码提交前的一次中间数据
    '''
    output = build_data + '/' + project + '/' + component
    return output

def allow_from_list():
    '''
    :return:
    '''
    cf = cr.ConfigParser()
    conf_file = os.getcwd() + '/' + "env_conf.py"
    cf.read(conf_file)
    return cf.get("FROM_TO", 'ALLOW_FROM_LIST')

def allow_to_list():
    '''
    :return:
    '''
    cf = cr.ConfigParser()
    conf_file = os.getcwd() + '/' + "env_conf.py"
    cf.read(conf_file)
    return cf.get("FROM_TO", 'ALLOW_FROM_LIST')

def get_svn_info(env, sid):
    '''
    :return:
    '''
    if env == "TEST" or env == "ALIYUN_TEST":
        env = "TEST"
    elif env == "INTE" or env == "ALIYUN_INTE":
        env = "INTE"
    elif env == "PORD":
        env = "PROD"
    elif env == "ONLINE" or env == "ALIYUN_ONLINE":
        env = "ONLINE"
    else:
        print "[ERROR]not found %s "%env
        raise Exception("[ERROR]")
    svn_info = []
    cf = cr.ConfigParser()
    conf_file = build_script + '/' + "env_conf.py"
    cf.read(conf_file)
    svn_info.append(cf.get(env, "CMDB_SVN_URL") + "/" + sid)
    svn_info.append(cf.get(env,"CMDB_SVN_USER"))
    svn_info.append(cf.get(env,"CMDB_SVN_PASSWD"))
    return svn_info

def get_rundeck_info(env):
    '''
    :return:
    '''
    if env == "TEST" or env == "ALIYUN_TEST":
        env = "TEST"
    elif env == "INTE" or env == "ALIYUN_INTE":
        env = "INTE"
    elif env == "PORD":
        env = "PROD"
    elif env == "ONLINE" or env == "ALIYUN_ONLINE":
        env = "ONLINE"
    else:
        print "[ERROR]not found %s "%env
        raise Exception("[ERROR]")
    rundeck__info = []
    cf = cr.ConfigParser()
    conf_file = build_script + '/' + "env_conf.py"
    cf.read(conf_file)
    rundeck__info.append(cf.get(env, "CMDB_RUNDECK_URL"))
    rundeck__info.append(cf.get(env, "CMDB_RUNDECK_USER"))
    rundeck__info.append(cf.get(env, "CMDB_RUNDECK_PASSWD"))
    rundeck__info.append(cf.get(env, "CMDB_RUNDECK_PROJECT"))
    return rundeck__info

if __name__ == "__main__":
    #print get_rundeck_info('TEST')
    print get_sid('ccs', 'wangleiaf_scm_test')



