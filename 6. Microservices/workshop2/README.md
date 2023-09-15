# Microservice FastAPI Demo

## run
- docker compose up --build

## services

                            ┌───────────┐
                            │           │
                            │  Browser  │
                            │           │
                            └─────┬─────┘
                                  │
                                  │ (1) /movies or /books
                                  │
                                  ▼
                            ┌───────────┐
                            │           │
                            │   NGINX   │
                            │           │
                            └───┬───────┘
                ┌───────────────┴───────────────┐
                │ (2) /movies                   │ (3) /books
                │                               │
        ┌───────▼───────┐               ┌───────▼───────┐
        │               │               │               │
        │  Movie Service│               │  Book Service │
        │               │               │               │
        └───────┬───────┘               └───────┬───────┘
                │ (4) /auth_service             │ (5) /auth_service
                │                               │
                └──────────────────────┬────────┘
                                       │
                                       ▼
                              ┌─────────────────┐
                              │                 │
                              │  Auth Service   │
                              │                 │
                              └─────────────────┘

## Test
- checkout the book_service docs
  - by going to http://localhost/books/docs
- checkout the movie_service docs
  - by going to http://localhost/movies/docs
- test the apis
  - can use the tool like [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client) VS Code extension or [Postman](https://www.postman.com/)
  - or can use curl cli command
```
curl -X GET http://localhost/movies/ -H "X-Api-Key: thisiscool"
curl -X GET http://localhost/books/ -H "X-Api-Key: thisiscool"
```

## stop services
- docker compose down