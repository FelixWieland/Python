import json
import requests

def get_btc_json(webapi):
    try:
        resp = requests.get(webapi, dict())
        return json.loads(resp.text)
    except Exception:
        print("Keine Internetverbindung vorhanden")

def print_json(btc_json):
    print(btc_json["time"]["updated"], btc_json["bpi"]["EUR"]["rate"])

def main():
    btc_json = get_btc_json("https://api.coindesk.com/v1/bpi/currentprice.json")
    print_json(btc_json)

if __name__ == '__main__':
    main()
