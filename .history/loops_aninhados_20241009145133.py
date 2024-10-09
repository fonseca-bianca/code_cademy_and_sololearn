"""
Um loop pode ter outro loop aninhado dentro dele. Isso significa que pra cada 
iteração do loop externo (principal), o loop interno será executado inteiramente.
Cada iteração do loop externo executa completamente o loop interno, com valores de
iterador correspondentes.
"""

ranks = ['Ace', 'King', 'Queen']
suits = ['Hearts', 'Clubs', 'Diamonds']

for rank in ranks:
    for suit in suits:
        print(f"{rank} of {suit}")
        
# Output:
# Ace of Hearts
# Ace of Clubs
# Ace of Diamonds
    # King of Hearts
    # King of Clubs
    # King of Diamonds
        # Queen of Hearts
        # Queen of Clubs
        # Queen of Diamonds