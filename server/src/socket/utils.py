from typing import Optional
from fastapi import Query, WebSocket, status
from ..redis.config import Redis

redis = Redis()

async def get_token(websocket: WebSocket, token: Optional[str] = Query(None)):
  if token is None or token == "":
    await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
  
  redis_client = await redis.create_connection()
  exists = await redis_client.exists(token)

  if exists == 1:
    return token
  else:
    await websocket.close(
      code=status.WS_1008_POLICY_VIOLATION, 
      reason="Session not authenticated or expired token"
    )