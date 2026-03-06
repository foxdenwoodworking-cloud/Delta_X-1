from .intake_a_router import router as intake_a
from .intake_b_router import router as intake_b
from .health import router as health

def register(app):
    app.include_router(intake_a)
    app.include_router(intake_b)
    app.include_router(health)
