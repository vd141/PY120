class Wallet:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return f'Wallet with ${self.amount}.'

    def __add__(self, other):
        return Wallet(self.amount + other.amount)
    
    # best practice is to check if other is a wallet instance before adding
    # this ensures that a non wallet object's behavior add behavior is fully defined

    @property
    def amount(self):
        return self._value

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True
print(merged_wallet) # Wallet with $80.