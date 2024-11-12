from pydantic import BaseModel, ConfigDict


class StatisticIn(BaseModel):
    row_count: int
    column_count: int
    duration: int

    model_config = ConfigDict(from_attributes=True)


class StatisticOut(BaseModel):
    id: int
    user_id: int
    row_count: int
    column_count: int
    duration: int

    model_config = ConfigDict(from_attributes=True)
