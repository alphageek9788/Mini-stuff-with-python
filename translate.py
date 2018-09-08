
dic = {"hello": "hola", "good": "bien"}
x = input('Type kar:').lower()

if x in dic.keys():
    print(dic[x])
else:
    print('Wrong input')
