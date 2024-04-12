from utils import confighandler

def get_user_info():
    graph = confighandler.get_graph_api()
    user_info = graph.get_object('me?fields=id,name')
    
    return user_info