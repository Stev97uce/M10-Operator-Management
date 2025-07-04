from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
from app.core.config import settings
import httpx

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Excepciones para rutas públicas (opcional)
        if request.url.path.startswith("/docs") or request.url.path.startswith("/openapi.json"):
            return await call_next(request)

        session_token = request.cookies.get("session_token")
        if not session_token:
            return Response(content="Unauthorized: No session_token", status_code=401)

        # Validar token con user-profile-service
        async with httpx.AsyncClient() as client:
            try:
                resp = await client.get(f"{settings.USER_SERVICE}/users/{session_token}", timeout=5.0)
                if resp.status_code != 200:
                    return Response(content="Unauthorized: Invalid token", status_code=401)
            except httpx.RequestError:
                return Response(content="User validation service unavailable", status_code=503)

        # Token válido, continuar con la solicitud
        response = await call_next(request)
        return response
