from datetime import datetime

class Snowflake(str):
    def __new__(cls, value):
        return str.__new__(cls, value)

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        elif isinstance(other, int):
            return int(self) == other
        return False

class Timestamp(str):
    def __new__(cls, value):
        if value is None:
            return None
        result = datetime.fromisoformat(str(value)).timestamp()
        return super().__new__(cls, result)