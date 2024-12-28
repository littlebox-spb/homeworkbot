from datetime import datetime, date

from pydantic import BaseModel


class HomeTask(BaseModel):
    number: int
    is_done: bool
    last_try_time: datetime | None = None
    amount_tries: int = 0


class HomeWork(BaseModel):
    number: int
    deadline: date
    tasks: list[HomeTask]
    is_done: bool
    end_time: datetime | None = None


class DisciplineHomeWork(BaseModel):
    home_work: list[HomeWork]
