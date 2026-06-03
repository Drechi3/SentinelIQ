from pydantic import BaseModel

class EventIn(BaseModel):
    user_id: str
    event_type: str
    ip_address: str