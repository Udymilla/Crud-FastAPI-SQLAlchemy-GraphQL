from fastapi import FastAPI
from routers import user, graphql

app = FastAPI()

app.include_router(user.router, prefix="/api", tags=["users"])
app.include_router(graphql.graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
