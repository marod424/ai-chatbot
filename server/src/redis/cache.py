from rejson import Path

class Cache:
  def __init__(self, json_client):
    self.json_cleint = json_client

  async def get_chat_history(self, token: str):
    data = self.json_cleint.jsonget(str(token), Path.rootPath())
    return data