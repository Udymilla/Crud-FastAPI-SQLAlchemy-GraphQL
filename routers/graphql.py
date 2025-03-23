import strawberry
from strawberry.fastapi import GraphQLRouter
from sqlalchemy.orm import Session
from database import get_db
from models.user import User

@strawberry.type
class UserType:
    id: int
    name: str
    email: str

@strawberry.type
class Query:
    @strawberry.field
    def get_user(self, id: int, db: Session = Depends(get_db)) -> UserType:
        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise ValueError("Usuário não encontrado")
        return UserType(id=user.id, name=user.name, email=user.email)

    @strawberry.field
    def list_users(self, db: Session = Depends(get_db)) -> list[UserType]:
        return db.query(User).all()

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)
