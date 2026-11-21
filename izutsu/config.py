
from pathlib import Path

from platformdirs import PlatformDirs

APP_NAME = "Izutsu"
APP_AUTHOR = "Izutsu Project"

dirs = PlatformDirs(
    appname=APP_NAME,
    appauthor=APP_AUTHOR,
)

DATA_DIR = Path(dirs.user_data_dir)
CONFIG_DIR = Path(dirs.user_config_dir)
CACHE_DIR = Path(dirs.user_cache_dir)

DATABASE_DIR = DATA_DIR / "database"
DOCUMENTS_DIR = DATA_DIR / "documents"
BACKUPS_DIR = DATA_DIR / "backups"

DATABASE_PATH = DATABASE_DIR / "izutsu.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"

def initialize_directories() -> None:
    """Create the required application directories."""

    for directory in (
        DATA_DIR,
        CONFIG_DIR,
        CACHE_DIR,
        DATABASE_DIR,
        DOCUMENTS_DIR,
        BACKUPS_DIR,
    ):
        directory.mkdir(parents=True, exist_ok=True)
