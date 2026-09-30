from datetime import datetime

from sqlalchemy import String, Unicode
from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db

STATUSES = {
    "pending": "Pendiente",
    "in_progress": "En progreso",
    "completed": "Completada",
}


class Task(db.Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(Unicode(150))
    description: Mapped[str | None] = mapped_column(Unicode)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    @property
    def status_label(self):
        return STATUSES.get(self.status, self.status)

