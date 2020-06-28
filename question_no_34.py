dic1 = {'key1': 10, 'key2': 20}
dic2 = {'key3': 30, 'key4': 40}
dic3 = {'key5': 50, 'key6': 60}

#merge dic2 and dic3 to dic1
dic1.update(dic2)
dic1.update(dic3)
print(dic1)