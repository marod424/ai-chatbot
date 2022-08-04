from typing import Optional
from fastapi import Query, WebSocket, status

async def get_token(websocket: WebSocket, token: Optional[str] = Query(None)):
  if token is None or token == "":
    await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
  
  return token