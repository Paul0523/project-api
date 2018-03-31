import socket
hostname = socket.gethostname()
isDebug = False
if (hostname == 'VM-39-130-ubuntu'):
    from config.env import production as envconfig
    isDebug = False
else:
    from config.env import local as envconfig
    isDebug = True


def get_config(config_name):
    """
    返回对应的配置文件属性
    :param config_name:
    :return:
    """
    return getattr(envconfig, config_name)