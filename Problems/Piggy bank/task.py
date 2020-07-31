class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        if deposit_cents + self.cents < 99:
            self.dollars += deposit_dollars
            self.cents += deposit_cents
        else:
            self.dollars += (deposit_dollars + (deposit_cents + self.cents) // 100)
            self.cents = ((deposit_cents + self.cents) % 100)
