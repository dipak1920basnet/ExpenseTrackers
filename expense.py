class Expenses:

    def __init__(self, id,name, description, amount, expense_date):
        self.id = id
        self.name = name
        self.descpription = description 
        self.expense_date = expense_date
        self.amount = amount

    def change_name(self, new_name):
        self.name = new_name

    def change_description(self, new_description):
        self.descpription = new_description

    def change_expense_date(self, new_date):
        self.expense_date = new_date

    def change_amount(self, new_amount):
        self.amount = new_amount