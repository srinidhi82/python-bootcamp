Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dict[('key5')])

print(Dict.keys())

Dict["Name"] = "MJ"
print(Dict.values())


Dict1={"A":1,"B":2,"C":[3,3,3],"D":(4,4,4),'E':5,'F':6}

print("The values we need are:" , Dict1["B"], Dict1["D"])