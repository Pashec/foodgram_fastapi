from sqlalchemy import CheckConstraint, UniqueConstraint, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from core.db import Base


class Subscription(Base):

    __tablename__ = 'subscriptions'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))

    __table_args__ = (
        UniqueConstraint('user_id', 'author_id', name='uq_user_author_subscription'),
        CheckConstraint('user_id != author_id', name='check_prevent_self_subscription'),
    )

    def __repr__(self) -> str:
        return f'<Subscription {self.user_id} -> {self.author_id}>'