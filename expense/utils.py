import json
import requests


headers = {
        'Host': 'irkkt-mobile.nalog.ru:8888',
        'Accept': '*/*',
        'Device-OS': 'Android',
        'Device-Id': '7C82010F-16CC-446B-8F66-FC4080C66521',
        'clientVersion': '2.9.0',
        'Accept-Language': 'ru-RU;q=1, en-US;q=0.9',
        'User-Agent': 'billchecker/2.9.0 (iPhone; iOS 13.6; Scale/2.00)',
    }

def set_session_id(phone) -> None:
    phone = phone
    url = f'https://irkkt-mobile.nalog.ru:8888/v2/auth/phone/request'
    payload = {
        'phone': phone,
        'client_secret': "IyvrAbKt9h/8p6a7QPh8gpkXYQ4=",
        'os': "Android"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response

def get_ticket_id( qr: str) -> str:
    url = f'https://irkkt-mobile.nalog.ru:8888/v2/ticket'
    payload = {'qr': qr}
    resp = requests.post(url, json=payload, headers=headers)
    return resp.json()["id"]

def get_ticket( qr: str) -> dict:
    ticket_id = get_ticket_id(qr)
    print(ticket_id)
    url = f'https://irkkt-mobile.nalog.ru:8888/v2/tickets/{ticket_id}'
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_products_by_code(phone,code,qr):
    url = 'https://irkkt-mobile.nalog.ru:8888/v2/auth/phone/verify'
    payload = {
        'phone': phone,
        'client_secret': "IyvrAbKt9h/8p6a7QPh8gpkXYQ4=",
        'code': code,
        "os": "Android"
        }
    response = requests.post(url, json=payload, headers=headers)
    __session_id = response.json()['sessionId']
    __refresh_token = response.json()['refresh_token']
    headers['sessionId'] =  __session_id
    ticket = get_ticket(qr)
    return ticket
