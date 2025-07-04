from fastapi import FastAPI
from app.routes.operator_routes import router as operator_router
from app.middleware.auth_middleware import AuthMiddleware

app = FastAPI(title="Operator Management Service")

app.add_middleware(AuthMiddleware)

app.include_router(operator_router, prefix="/api/operators")

# Correr: uvicorn app.main:app --reload --port 8001
