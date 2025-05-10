import csv
import hashlib



with open('Amir_python1_code.csv') as f:
    reader = csv.reader(f)
    test = {row[0] : row[1] for row in reader}

#print(test,type(test))

test_hash = dict()

for i in range(10000):
    row = str(i)
    result = hashlib.sha256(row.encode())
    hash_value = result.hexdigest()
    test_hash[row] = hash_value

#print(test_hash)

list_sample = list(test.values())
for key in test_hash:
    if test_hash[key] in list_sample:
        print(key)
