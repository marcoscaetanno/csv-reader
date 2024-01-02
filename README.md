# CSV Reader API

- Welcome to the CSV reader API, an project made to import a CSV, send a email with the debt and due date.
- This project runs with FastApi
### Requirements to run this project locally
- python sdk installed on your machine
- Docker and docker-compose

## Run locally

### First step
- go to directory docker-compose and run this command:
> docker-compose up -d

### Second step
- back to root project folder, and run the command to start the api:
> uvicorn controller:app --reload
- The api run by default on http://localhost:8000

### Swagger
> http://localhost:8000/docs
