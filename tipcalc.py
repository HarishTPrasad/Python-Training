
def tipcalc(bill,tip):


  amount = bill + (bill*tip)/100

  return(amount)


bill = int(input("How much is your bill :"))
tip = int(input("How much tip :"))
x = tipcalc(bill,tip)
print (x)


