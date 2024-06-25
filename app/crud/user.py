from sqlalchemy.orm import Session
import app.models.user as user
from app.schemas import user_schema
from fastapi import HTTPException, status
from app.utils import hashing


def create(request: user_schema.User, db: Session):
    existing_user = db.query(user.User).filter(user.User.email == request.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    new_user = user.User(
        name=request.name,
        email=request.email,
        password=hashing.Hash.bcrypt(request.password),
        vectorstore=request.vectorstore,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):
    user_found = db.query(user.User).filter(user.User.id == id).first()
    if not user_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    return user_found


def show_by_email(email: str, db: Session):
    user_found = db.query(user.User).filter(user.User.email == email).first()
    if not user_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with email {email} not found",
        )
    return user_found

def update_user(id: int, request: user_schema.User, db: Session):
    user_found = db.query(user.User).filter(user.User.id == id).first()
    if not user_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )

    user_found.name = request.name
    user_found.vectorstore = request.vectorstore

    db.add(user_found)
    db.commit()
    db.refresh(user_found)
    return user_found
