from enum import Enum
class CommandEnum(Enum):
    IMPORT_FILE = "--import-file"
    IMPORT_TEXT = "--import-text"
    FIND = "-f"
    PREDICT = "-p"