from balanceRetreive import getBalance
import sys
import csv

def findBalance(name):
    with open('account_db.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        index = 0
        for row in csv_reader:
            index += 1
            if index == 1:
                print(f'{row[0]}, {row[1]}, {row[2]}')
                # Ignore header
            elif row[1] == name:
                print(f'{row[0]}, {row[1]}, {row[2]}')
                return getBalance(12388, index) - int(row[2])

    print("Not found, adding")
    print(str(lines) + "," + name + "," + "0", file=open("account_db.csv", 'a'))
    return 0

findBalance(sys.argv[1])
