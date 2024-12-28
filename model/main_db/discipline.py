from sqlalchemy import Column, Integer, String, JSON

from database.main_db.database import Base


class Discipline(Base):
    __tablename__ = "discipline"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    short_name = Column(String, nullable=False)
    path_to_test = Column(String, nullable=False)
    path_to_answer = Column(String, nullable=False)
    language = Column(String, nullable=False)
    max_tasks = Column(Integer, nullable=False)
    max_home_work = Column(Integer, nullable=False)
    works = Column(JSON, nullable=False)

    def __repr__(self) -> str:
        return f"Discipline [{self.short_name}, max_tasks: {self.max_tasks},\
             works: {self.works}]"
