import requests

API_KEY = 'YUOR_API_KEY'
BASE_URL = 'https://api.etherscan.io/api?module=account'

def get_balance(address):
	url = BASE_URL + '&action=balance&address=' + address + '&tag=latest&apikey=' + API_KEY
	print(url)
	r = requests.get(url)
	print(r.text)

def run():
	address = '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a'
	get_balance(address)


if __name__ == "__main__":
    run()
