import sys
import json, requests

def getBalance(wallet_rpc_port, account_index):
    headers = {
        'Content-Type': 'application/json',
    }
    
    data = '{"jsonrpc":"2.0","id":"0","method":"get_balance","params":{"account_index":' + str(account_index) + '}}'
    
    response = requests.post('http://127.0.0.1:' + str(wallet_rpc_port) + '/json_rpc', headers=headers, data=data).json()
    
    return response["result"]["unlocked_balance"]

def getAddress(wallet_rpc_port, account_index):
    headers = {
        'Content-Type': 'application/json',
    }
    
    data = '{"jsonrpc":"2.0","id":"0","method":"get_address","params":{"account_index":' + str(account_index) + '}}'
    
    response = requests.post('http://127.0.0.1:' + str(wallet_rpc_port) + '/json_rpc', headers=headers, data=data).json()

    return response["result"]["address"]

def createAccount(wallet_rpc_port, account_index):
    headers = {
        'Content-Type': 'application/json',
    }

    data = '{"jsonrpc":"2.0","id":"0","method":"create_account","params":{"label":"' + str(account_index) + '"}}'

    response = requests.post('http://127.0.0.1:' + str(wallet_rpc_port) + '/json_rpc', headers=headers, data=data).json()
