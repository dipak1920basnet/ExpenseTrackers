from expense import Expenses

class User:
    def __init__(self,id, name:str=None, password:str=None, email:str=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.Expense = []

    def logged_in():
        return False

    def confirm_password(self, password:str)->bool:
        if self.password == password:
            return True
        return False

    def confirm_email(self, email:str) -> bool:
        if self.email == email:
            return True
        return False
    
    def change_password(self, old_password:str, new_password:str, confirm_password:str)->None:
        if self.confirm_password(old_password) and new_password == confirm_password:
            self.password = new_password

    def change_name(self, email:str, password:str, new_name:str)->None:
        if (self.confirm_email(email) and self.confirm_password(password)) or self.loged_in():
            self.name = new_name

    def add_Expense(self, expense:Expenses)->None:
        if isinstance(self.Expense) != list:
            self.Expense = []
        self.Expense.append(expense)

    def delete_expense(self):
        pass

    def total_expenses(self):
        pass

    def generate_expense_id(self):
        pass
    