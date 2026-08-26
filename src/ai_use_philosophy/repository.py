# repository.py
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from ai_use_philosophy.logger import logger
from ai_use_philosophy.models import Base, Principle
from ai_use_philosophy.schemas import PrincipleOut


class PrincipleRepository:
    def __init__(self, db_url: str = "sqlite:///principles.db"):
        logger.info(f"Initializing PrincipleRepository (db_url={db_url})")
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)

    def get_all(self) -> list[PrincipleOut]:
        logger.debug("Fetching all principles")
        with Session(self.engine) as session:
            rows = session.query(Principle).all()
            logger.debug(f"Fetched {len(rows)} principles")
            return [PrincipleOut(id=row.id, principle=row.principle) for row in rows]

    def add(self, text: str) -> None:
        logger.info(f"Adding principle: {text!r}")
        with Session(self.engine) as session:
            session.add(Principle(principle=text))
            session.commit()

    def get_by_id(self, principle_id: int) -> str | None:
        logger.debug(f"Fetching principle id={principle_id}")
        with Session(self.engine) as session:
            row = session.get(Principle, principle_id)
            if row is None:
                logger.warning(f"No principle found with id={principle_id}")
            return row.principle if row else None

    def delete(self, principle_id: int) -> bool:
        logger.info(f"Deleting principle id={principle_id}")
        with Session(self.engine) as session:
            row = session.get(Principle, principle_id)
            if row is None:
                logger.warning(f"Delete failed: no principle found with id={principle_id}")
                return False
            session.delete(row)
            session.commit()
            logger.info(f"Deleted principle id={principle_id}")
            return True

    def update(self, principle_id: int, new_text: str) -> bool:
        logger.info(f"Updating principle id={principle_id}")
        with Session(self.engine) as session:
            row = session.get(Principle, principle_id)
            if row is None:
                logger.warning(f"Update failed: no principle found with id={principle_id}")
                return False
            row.principle = new_text
            session.commit()
            logger.info(f"Updated principle id={principle_id}")
            return True
