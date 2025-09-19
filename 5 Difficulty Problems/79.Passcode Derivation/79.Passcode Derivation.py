with open("79.Passcode Derivation/0079_keylog.txt","r") as f:
    dif_codes = set()
    content = f.read()
    content = content.split("\n")
    for i in content:
        dif_codes.add(i)

password = []
for i in dif_codes:
    x , y , z = i[0] , i[1] , i[2]
    if x not in password:  
        password.append(x)
    if y not in password:    
        password.append(y)
    if z not in password:
        password.append(z)
    if password.index(x) > password.index(y):
        password.pop(password.index(x))
        password.insert(password.index(y),x)
    if password.index(y) > password.index(z):
        password.pop(password.index(y))
        password.insert(password.index(z),y)

for i in password:
    print(i,end="")




