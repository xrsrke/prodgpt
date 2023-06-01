from pydantic import BaseModel


class InferenceLog(BaseModel):
    input: str
    output: str
    model_id: str
    user_id: str
