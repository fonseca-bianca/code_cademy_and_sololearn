"""
1 - What is the output of this code?
"""
def order():
  def prepare(): # função nested (aninhada): está DENTRO da função 'order()'
    return "Your meal is being prepared!"
  status = prepare()
  return status

print(order())
# output: "Your meal is being prepared!"