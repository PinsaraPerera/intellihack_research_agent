from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base
from app.db.session import engine
from app.api.endpoints import users, agentConfiguration, graph, quiz, research

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "https://intellihack-web-cloud-run-rcbmvyttca-uc.a.run.app",
    "https://intellihack-backend-rcbmvyttca-uc.a.run.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(agentConfiguration.router)
app.include_router(graph.router)
app.include_router(quiz.router)
app.include_router(research.router)


