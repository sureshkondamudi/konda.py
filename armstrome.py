number=int(input('enter your number: '))
def check_armstrom(num):  
    order =len(str(num))
    sum=0
    original=num

    while num>0:
        digit=num%10
        sum+=digit ** order
        num=num // 10
    if sum==original:
        return True
    return False
if check_armstrom(number):
    print(number,'is armstrong')
else:
    print(number ,'is not armstrom')

