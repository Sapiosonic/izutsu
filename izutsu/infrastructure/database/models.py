
import uuid

from datetime import datetime, timezone

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from izutsu.infrastructure.database.base import Base


def generate_id() -> str:
    return str(uuid.uuid4())


def utc_now() -> datetime:
    return datetime.now(timezone.utc)

# Entity: Language
# Purpose: Supported languages
class Language(Base):
    __tablename__ = "languages"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=generate_id
    )

    code: Mapped[str] = mapped_column(
        String(16), unique=True, nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    native_name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    is_learning_supported: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    is_interface_supported: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )

    vocabulary_entries: Mapped[list["VocabularyEntry"]] = relationship(
        back_populates="language"
    )

# Entity: VocabularyEntry
# Purpose: Saved words and expressions
class VocabularyEntry(Base):
    __tablename__ = "vocabulary_entries"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=generate_id
    )

    language_id: Mapped[str] = mapped_column(
        ForeignKey("languages.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    headword: Mapped[str] = mapped_column(
        String(255), nullable=False
    )

    lemma: Mapped[str | None] = mapped_column(
        String(255), nullable=True, index=True
    )

    part_of_speech: Mapped[str | None] = mapped_column(
        String(50), nullable=True
    )

    pronunciation: Mapped[str | None] = mapped_column(
        String(255), nullable=True
    )

    phonetic_system: Mapped[str | None] = mapped_column(
        String(30), nullable=True
    )

    source_url: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )

    source_title: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )

    original_sentence: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )

    surrounding_context: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )

    translation: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )

    notes: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )

    domain: Mapped[str | None] = mapped_column(
        String(100), nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now,
        nullable=False,
    )

    language: Mapped["Language"] = relationship(
        back_populates="vocabulary_entries"
    )

    senses: Mapped[list["VocabularySense"]] = relationship(
        back_populates="entry",
        cascade="all, delete-orphan",
        order_by="VocabularySense.sense_order",
    )

    __table_args__ = (
        UniqueConstraint(
            "language_id",
            "headword",
            name="uq_vocabulary_language_headword",
        ),
    )

# Entity: VocabularySense	
# Purpose: Different meanings of a word
class VocabularySense(Base):
    __tablename__ = "vocabulary_senses"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=generate_id
    )

    vocabulary_entry_id: Mapped[str] = mapped_column(
        ForeignKey("vocabulary_entries.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    definition: Mapped[str] = mapped_column(
        Text, nullable=False
    )

    contextual_definition: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )

    translation: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )

    grammatical_function: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )

    register: Mapped[str | None] = mapped_column(
        String(50), nullable=True
    )

    domain: Mapped[str | None] = mapped_column(
        String(100), nullable=True
    )

    sense_order: Mapped[int] = mapped_column(
        Integer, default=1, nullable=False
    )

    entry: Mapped["VocabularyEntry"] = relationship(
        back_populates="senses"
    )

# Entity: AppSetting	
# Purpose: Application preferences
class AppSetting(Base):
    __tablename__ = "app_settings"

    key: Mapped[str] = mapped_column(
        String(150), primary_key=True
    )

    value: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now,
        nullable=False,
    )
