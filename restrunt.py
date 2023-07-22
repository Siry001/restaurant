# GUI code 
from tkinter import *
from tkinter import Tk
ob=Tk()
 
ob.mainloop()
# prgram code 
name=input(str('\nwhat is your name? '))
print('welcom to our restrunt',name)
def restrunt():
    Menu={'big mac': 40 ,'big tasty': 70 ,'cheese burger': 50 ,'mc royal': 30 ,'little tasty': 10,'mc chicken':40,'chicken mac':50,'grand chicken':60,'grand chicken spicy':70,'salad':5,'fries':10,'pepsi':5,'cola':5,'sprite':5}
    cart=[]
    order=input('Start an order or Contact us? ')    
    if order=='contact us':
      print('\nOkay these are our contact details \n phone number     : 19666 \n Address          : 12 street elsafa and elmarwa beside CIB Bank hadayek helwan \n email address    : restrunt001@gmail.com')
      return_1=input(str('go back or exit ? '))
      if return_1=='go back':
            restrunt()
      else:
         print('the program has ended')
    elif order=='start an order':
        print('\n------------------------------\nprduct                 price\n------------------------------\nbig mac                 40$ \nbig tasty               70$ \ncheese burger           50$ \nmc royal                30$ \nlittle tasty            10$ \nmc chicken              40$ \nchicken mac             50$ \ngngrand chicken         60$ \ngngrand chicken spicy   70$ \nsalad                    5$ \nfries                    5$ \npepsi                    5$ \ncola                     5$ \nsprite                   5$\n------------------------------')
        def check():
            order_input=input('what would you like to order?: ') 
            if order_input in Menu:
                cart.append(order_input)
            else:
                print('your entery is incorrect',name,'\n')
                check()
        check()
        return_1=input('would you like to add anything to order?(answer yes or No): ')
        if return_1=='yes':
            return_2='yes'
            while return_2=='yes':
                check()
                return_2=input('would you like to add anything to order?:(enter yes or No)')
            return_3=input('go back or go to cart?: ')
            if return_3=='go to cart':     
                sum=0
                for i in range(len(cart)):
                    sum=sum+Menu[cart[i]]+0.14*Menu[cart[i]]
                    print('\nnproduct',i+1,'is:',cart[i])
                    print('the price is:',Menu[cart[i]]+0.14*Menu[cart[i]],'$')
                print('\nthe total price is: ',format(sum,'.2f'),'$')
                option2=input('go back or exit?: ')
                if option2=='go back':
                   restrunt()
                else:
                    print('the program has ended')
            else:
               restrunt()
        else: 
            return_4=input('go back or go to cart?: ')
            if return_4=='go to cart':
                print('\nproduct is:',cart[0])
                print('the total price is:',Menu[cart[0]]+0.14*Menu[cart[0]],'$')
                option3=input('go back or exit?: ')
                if option3=='exit':
                   print('the program has ended')
                else:
                   restrunt()
            else:
               restrunt()
    else:
        print('your entery is incorrect',name,'\n')
        restrunt()
restrunt()
