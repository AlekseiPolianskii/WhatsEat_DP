import sys
import os
import json


def load_configs():
    config_keys = [
        'DEFAULT_IP_ADDRESS',
        'DEFAULT_PORT',
        'ENCODING'
    ]
    if not os.path.exists('config.json'):
        print('Файл конфигурации не найден')
        sys.exit(1)
    with open('config.json') as config_file:
        CONFIGS = json.load(config_file)
    loaded_configs_keys = list(CONFIGS.keys())
    for key in config_keys:
        if key not in loaded_configs_keys:
            print(f'В файле конфигурации не хватает ключа: {key}')
            sys.exit(1)
    return CONFIGS


def get_response(address, response):
    return str(address + response)


def get_address(CONFIG):
    return f'http://{CONFIG["DEFAULT_IP_ADDRESS"]}:{CONFIG["DEFAULT_PORT"]}/whatseat/'


def get_items_response_recipes(items='products'):
    return f'api/v1/dishes?{items}='


def get_response_server(address, items, search=None):
    if search:
        return f'{address}{items}{search}'
    else:
        return f'{address}{items}'

def get_image_address(image_url):
    return f'http://185.46.8.32:8080/whatseat/{image_url}'