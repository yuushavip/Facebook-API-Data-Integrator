import facebook
import configparser
import yaml
import os

def get_config():
    config = configparser.ConfigParser()
    file_name = 'config.ini'
    file_path = f"config/{file_name}"
        
    config.read(file_path)
    
    return config

def get_config_from_session(session):
    config = get_config()
    config_session = config[session]
    config_data = {}
    
    for key, item in config_session.items():
        config_data[key] = item
        
    return config_data

def get_graph_api():
    config = get_config_from_session('AUTH')
    access_token = config['access_token']
    api_version = config['api_version']
    
    graph = facebook.GraphAPI(access_token=access_token, version=api_version)
    
    return graph