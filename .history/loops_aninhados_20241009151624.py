"""
Um loop pode ter outro loop aninhado dentro dele. Isso significa que pra cada 
iteração do loop externo (principal), o loop interno será executado inteiramente.
Cada iteração do loop externo executa completamente o loop interno, com valores 
de iterador correspondentes.
"""

ranks = ['Ace', 'King', 'Queen']
suits = ['Hearts', 'Clubs', 'Diamonds']

for rank in ranks: # loop externo
    for suit in suits: # loop inter
        print(f"{rank} of {suit}")
        
# Output:
# Ace of Hearts     # 1 - 1
# Ace of Clubs      # 1 - 2
# Ace of Diamonds   # 1 - 3
    # King of Hearts    # 2 - 1
    # King of Clubs     # 2 - 2
    # King of Diamonds  # 2 - 3
        # Queen of Hearts   # 3 - 1
        # Queen of Clubs    # 3 - 2
        # Queen of Diamonds # 3 - 3
        
print()
       
vehicles = ['car', 'bike']
colors = ['red', 'blue']
for vehicle in vehicles:
  for color in colors:
    print(color, vehicle)
    
print()

days = ['Monday', 'Tuesday', 'Wednesday']
tasks = ['Gym', 'Homework', 'Pool']
for day in days:
  for task in tasks:
    print(day, task)