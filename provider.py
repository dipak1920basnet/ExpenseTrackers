from user import User
class Controller:

    def __init__(self):
        self.name = None
        self.user_list:list[User] = []

    def add_user(self,name:str=None, password:str=None, email:str=None):
        id = self.generate_user_id()
        user = User(id,name,password,email)
        self.user_list.append(user)

    def delete_user(self, user:User):
        pass

    def generate_user_id(self):
        pass
