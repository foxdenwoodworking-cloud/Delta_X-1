from fastapi import FastAPI
from .intake_a_router import router as intake_a_router
from .intake_b_router import router as intake_b_router

app = FastAPI(title="Delta SentinelXL Dual Intake")

app.include_router(intake_a_router)
app.include_router(intake_b_router)
