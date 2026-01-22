
































from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import flows, agents
from db.engine import init_db

app = FastAPI(
    title="FlowBrain API",
    description="Adaptive Workflow Engine for Multi-Agent Systems",
    version="0.1.0",
)

# Allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(flows.router, prefix="/flows", tags=["Flows"])
app.include_router(agents.router, prefix="/agents", tags=["Agents"])


@app.on_event("startup")
async def startup_event():
    await init_db()
    print("🚀 FlowBrain backend started successfully.")


@app.get("/")
async def root():
    return {"message": "Welcome to FlowBrain API"}
