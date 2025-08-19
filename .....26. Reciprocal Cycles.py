from decimal import Decimal , getcontext
getcontext().prec = 50

def kaçıncı_basamaktan_itibaren_devrediyor(string):
    return 5
#Devretmeyen son basamağı dönücek

def devreden_basamak_sayısı(string):
    x = kaçıncı_basamaktan_itibaren_devrediyor(string)
    string = string[x+1::]

    output = 1
    while True:
        str_1 = string[:output]
        str_2 = string[output:output*2]
        if str_1 == str_2:
            break         

        output += 1

    return output



max_devreden = 0
max_devreden_sayı = 0
for i in range(2,11):
    result = str(Decimal(1)/Decimal(i))
    result = result[2::]
    şimdiki_devreden = devreden_basamak_sayısı(result)
    if şimdiki_devreden > max_devreden:
        max_devreden = şimdiki_devreden
        max_devreden_sayı = i
        print("Şu anki max devirli sayı: ",result)


print("Devretme sayısı: ",max_devreden)
print("En çok devreden sayı: ",max_devreden_sayı)













