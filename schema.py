from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from typing import List
import asyncio

# Define the GraphQL types
@strawberry.type
class Book:
    title: str
    author: str
    year: int

# Define Query, Mutation, Subscription, and other operations
@strawberry.type
class Query:
    @strawberry.field
    def books(self, author: str = None, year: int = None) -> List[Book]:
        all_books = [
            Book(title="1984", author="George Orwell", year=1949),
            Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960),
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925),
        ]
        if author:
            all_books = [book for book in all_books if author.lower() in book.author.lower()]
        if year:
            all_books = [book for book in all_books if book.year == year]
        return all_books

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str, year: int) -> Book:
        new_book = Book(title=title, author=author, year=year)
        # In a real app, you'd save to a database here.
        return new_book

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def new_book_added(self) -> Book:
        # Simulate waiting for a new book to be added
        await asyncio.sleep(5)
        return Book(title="New Book", author="Some Author", year=2023)

# Create the schema
schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)

# FastAPI setup
app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
