from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def list_users(self):
        return self.user_repo.list_all()

    def delete_user(self, user_id: str):
        return self.user_repo.delete(user_id)
