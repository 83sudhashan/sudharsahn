# class kart:
#     quantity={'tv':10,'mobile':20,'laptop':10}
#     price={'tv':15000,'mobile':10000,'laptop':25000}

# def __init__(self,name,mob,loc):
#     self.name=name
#     self.mob=mob
#     self.loc=loc
#     self.product_qty=0
#     self.total_price=0

def details():
    print('enter your name:-  ')
    name=input(   )
    print('enter your mobile number:-  ')
    mobile=int(input(   ))
    print('enter your location')
    loc=input(   )
details()

def products():
    print('available product are tv, mobile,laptop')
products()

def product():
    print('welcome to my kart....')
    print('select the following')
    print('''enter 
          1.tv
          2.mobile
          3.loptop''')
    
    if '1':
        print('enter a number of products')
        products=int(input('enter no of pro'))
        if products<=10:
            total_price=products*15000
            print(total_price)
        else:
            print('sorry for this unconvinience')
    elif '2':
        print('enter number of products:-')
        product=int(input(    ))
        if products<20:
            total_price=products*10000
            print(total_price)
        else:
            print('sorry for this unconvinience')
    elif '3':
        print('enter number of products:-')
        product=int(input(    ))
        if products<=10:
            total_price=products*25000
            print(total_price)
        else:
            print('sorry for this unconvinience')
    else:
        print('sorry at present we have only this items')

product()



