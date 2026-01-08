# FastAPI + Strawberry GraphQL Learning Project

A minimal GraphQL API built with **FastAPI** and **Strawberry** to help you learn GraphQL concepts. This project demonstrates Queries, Mutations, and Subscriptions using a simple `Book` model.

## What You Can Do (All GraphQL Operations)

### 1. Queries - Read Data

Fetch the list of books with optional filters.

**Field:** `books(author: String, year: Int): [Book!]!`

**Capabilities:**
- Get all books (no arguments)
- Filter by author (case-insensitive partial match, e.g., "orwell" will match "George Orwell")
- Filter by exact year
- Combine author and year filters

**Example Queries**

```graphql
# Get all books
query GetAllBooks {
  books {
    title
    author
    year
  }
}

# Filter by author
query FilterByAuthor {
  books(author: "orwell") {
    title
    author
    year
  }
}

# Filter by year
query FilterByYear {
  books(year: 1925) {
    title
    author
    year
  }
}

# Combine both filters
query CombinedFilter {
  books(author: "lee", year: 1960) {
    title
    author
    year
  }
}

```graphql
type Mutation {
  addBook(title: String!, author: String!, year: Int!): Book!
}
```

```graphql
mutation {
  addBook(title: "Brave New World", author: "Aldous Huxley", year: 1932) {
    title
    author
    year
  }
}
```

```graphql
mutation AddNewBook {
  addBook(
    title: "Brave New World"
    author: "Aldous Huxley"
    year: 1932
  ) {
    title
    author
    year
  }
}
```

```graphql
subscription ListenForNewBooks {
  newBookAdded {
    title
    author
    year
  }
}
```

```graphql
{
  "data": {
    "newBookAdded": {
      "title": "New Book",
      "author": "Some Author",
      "year": 2023
    }
  }
}
```
