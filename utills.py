from configparser import ConfigParser

def get_conf_values(path):
    conf = ConfigParser()
    conf.read(path)
    
    config_dict = {section: dict(conf.items(section)) for section in conf.sections()}    
    return config_dict