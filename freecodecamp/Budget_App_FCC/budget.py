class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
        return True

    def get_balance(self):
        balance = 0
        for items in self.ledger:
            balance += items['amount']
        return balance

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) is True:
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def transfer(self, amount, new_budget):
        if self.check_funds(amount) is True:
            self.withdraw(amount, f"Transfer to {new_budget.name}")
            new_budget.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

# DISPLAY RECEIPTS
    def __str__(self):
        output = self.name.center(30, "*") + '\n'
        for items in self.ledger:
            output += f"{(items['description'][:23]).ljust(23)}{format(items['amount'], '0.2f').rjust(7)}\n"
        output += "Total: " + format(self.get_balance(), '0.2f')
        return output


# DISPLAY BAR CHART --->> copied from Dhruv_Rajesh :))
def create_spend_chart(categories):
    category_names = []
    spent = []
    final_spent = []

    for category in categories:  # logic from Beau, checking spent items
        total = 0
        for i in category.ledger:
            if i['amount'] < 0:
                total -= i['amount']
        spent.append(round(total, 2))
        category_names.append(category.name)

    for percents in spent:
        final_spent.append(round(percents / sum(spent), 2) * 100)

    graph_return = "Percentage spent by category\n"

    axis = range(100, -10, -10)

    for label in axis:  # logic from Beau, right alignment similar to arithmetic arranger
        graph_return += str(label).rjust(3) + "| "
        for percents in final_spent:
            if percents >= label:
                graph_return += "o  "
            else:
                graph_return += "   "
        graph_return += "\n"

    graph_return += "    ----" + ("---" * (len(category_names) - 1))
    graph_return += "\n     "

    len_longest = 0

    for names in category_names:
        if len_longest < len(names):
            len_longest = len(names)

    for i in range(len_longest):  # logic from Beau, formatting
        for names in category_names:
            if len(names) > i:
                graph_return += names[i] + "  "
            else:
                graph_return += "   "
        if i < len_longest - 1:
            graph_return += "\n     "

    return graph_return


