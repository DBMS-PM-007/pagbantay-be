from models.base import User

class UserRepository:
    def __init__(self, db):
        self.db = db

    def create_user(self, user_data):
        user = User(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            is_admin=user_data.is_admin,
            password=user_data.password,
            contact_info=user_data.contact_info,
            status=user_data.status,
            email=user_data.email,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_all_users(self):
        return self.db.query(User).all()
