from pythonping import ping
import json
from Read_config import data_turnstile, turnstile_list
import os





class Ping_IP():
    def status_ping(self, data_turnstile, turnstile_list ): # Статус UP/DOWN
        state_connect = []
        for turnstile_number in turnstile_list:
            a = data_turnstile[turnstile_number]
            ip = a[0]
            location_turnstile = a[1]
            response = os.system("ping -n 1 " + ip)
            if response == 0:
                result = ['Турникет' + " " + turnstile_number + " / " + location_turnstile + " - " + 'На связи']
            else:
                result = ['Турникет' + " " + turnstile_number + " / " + location_turnstile + " - " + 'Не отвечает']
            state_connect.append(result)
        return state_connect

    def statusUP_ping(self,data_turnstile, turnstile_list):
        state_connect_UP = []
        for turnstile_number in turnstile_list:
            a = data_turnstile[turnstile_number]
            ip = a[0]
            location_turnstile = a[1]
            response = os.system("ping -n 1 " + ip)
            if response == 0:
                result = ['Турникет' + " " + turnstile_number + " / " + location_turnstile + " - " + 'На связи']
            state_connect_UP.append(result)
        return state_connect_UP

    def statusDOWN_ping(self,data_turnstile, turnstile_list):
        state_connect_DOWN = []
        for turnstile_number in turnstile_list:
            a = data_turnstile[turnstile_number]
            ip = a[0]
            location_turnstile = a[1]
            response = os.system("ping -n 1 " + ip)
            if response == 0:
                continue
            else:
                result = ['Турникет' + " " + turnstile_number + " / " + location_turnstile + " - " + 'Не отвечает']
            state_connect_DOWN.append(result)
        return state_connect_DOWN


if __name__ == '__main__':
    ping_IP(data, turnstile_list)







