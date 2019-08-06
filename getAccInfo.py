from rpc_calls import *
import sys
import csv

def findInfo(name):
    with open('account_db.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        index = 0
        for row in csv_reader:
            if row[1] == name and index > 0: 
                return {
                    "index" : index, 
                    "spent" : int(row[2]),
                    "balance" : getBalance(12388, index) - int(row[2]),
                    "address" : getAddress(12388, index)
                }
            index += 1

    print(str(index) + "," + name + "," + "0",
        file=open("account_db.csv", 'a')) # Create a new account for the user
    createAccount(12388, index)
    return findInfo(name)

theirInfo = findInfo(sys.argv[1])
print(theirInfo)
