import json


with open('IP_list','r', encoding='utf-8') as f: #
    data_turnstile = json.load(f)
    turnstile_list = data_turnstile.keys()

with open('config','r', encoding='utf-8') as f: #
    config = json.load(f)
    TOKEN = config['TOKEN']
    time_connect = int(config['time_connect'])
    chat_id = config['chat_id'].split(',')



if __name__ == '__main__':
    print (TOKEN)
    print(turnstile_list)
    print(data)