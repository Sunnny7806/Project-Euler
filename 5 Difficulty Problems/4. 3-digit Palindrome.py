polindrom_numbers = []
for first in range(100,1000):
    for second in range(100,1000):
        product = first * second
        print(f"{product}  ==   {first}  x   {second}")
        product = str(product)
        if len(product) == 6:
            if product[0] == product[5]:
                if product[1] == product[4]:
                    if product[2] == product[3]:
                        polindrom_numbers.append(product)
        
                
polindrom_numbers.sort()
print(polindrom_numbers)

                

