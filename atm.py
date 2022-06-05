class cashcounter:
    def __init__(self,cardnumber,pin):
        self.pin=pin
        self.cardnumber=cardnumber
        print('cardnumber,pin')
    
    
    
    def balancenquiry(self):
        print('kya hain balance?')
        
    def withdrawl(self,amount): 
        new_amount = 50000 - amount 
        print("you have withdrawn amount " + str(amount) + " Your remaining balance is " + str(new_amount)) 
        
        
        
    def main():
        name = input('aapka naam kya hain?')
        print('heloo '+ name)
        cardnumber=input('cardnumber likho')
        pin=input('pin number?')
        user=cashcounter(cardnumber,pin)
    
        print('choose an acitvity. u want to 1. withdrwal or 2. balance enquiry?')
        act=int(input('enter activity  '))
        
        
        if(act == 1):
            user.balancenquiry()
        elif(act == 2): 
              amount = int(input('enter amount'))
              user.withdrawl(amount)
        else:
            print('enter a valid num')
            
if __name__ ** "__main__":
   main()