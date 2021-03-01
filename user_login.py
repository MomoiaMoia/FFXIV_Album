from flask_login import UserMixin


class User(UserMixin):

    def __init__(self,id,user_pwd,user_name) -> None:
        self.id = id
        self.user_pwd = user_pwd
        self.user_name = user_name.title()

    def is_authenticated(self,passwd):
        if str(self.user_pwd) == str(passwd):
            return True
        else:
            return False
        
