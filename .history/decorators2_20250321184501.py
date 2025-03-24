"""
1 - What is the output of this code?
"""
def order():
  def prepare():
    return "Your meal is being prepared!"
  status = prepare()
  return status

print(order())
# output: "Your meal is being prepared!"