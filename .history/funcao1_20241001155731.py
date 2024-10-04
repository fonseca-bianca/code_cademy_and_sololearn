def tax(bill): # bill: conta
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print ("With tax: %f.2" % bill)
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print ("With tip: %f.2" % bill)
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax) # tip = gorjeta