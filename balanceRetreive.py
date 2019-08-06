import sys
import json, requests

headers = {
    'Content-Type': 'application/json',
}

data = '{"jsonrpc":"2.0","id":"0","method":"get_balance","params":{"account_index":' + sys.argv[2] + '}}'

response = requests.post('http://127.0.0.1:' + sys.argv[1] + '/json_rpc', headers=headers, data=data).json()

print(response)
