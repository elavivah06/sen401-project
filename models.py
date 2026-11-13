"""Pydantic models — Lab 4 refactor."""
from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str = Field(..., min_length=1)
    score: float = Field(..., ge=0, le=100)


class InventoryItem(BaseModel):
    item_name: str
    quantity: int = Field(..., ge=0)
    price: float = Field(..., ge=0)