from utils import confighandler

def fetch_post_data():
    graph_api = confighandler.get_graph_api()
    page_id = ''
    fetch_posts_data_items = graph_api.get_object(f'{page_id}/feed?since=2023-01-01&until=2023-03-01')
    
    return fetch_posts_data_items