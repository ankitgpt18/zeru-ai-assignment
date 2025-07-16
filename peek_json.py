import json
try:
    with open('data/user-wallet-transactions.json') as f:
        data = json.load(f)
    print("Number of records:", len(data))
    if len(data) > 0:
        print("First record:", data[0])
    else:
        print("The file is empty.")
except Exception as e:
    print("Error:", e)