import re
from typing import Any


def setint(obj: object, name: str, value: Any) -> None:
    int_found = re.search(r'\d+', value)
    if int_found:
        setattr(obj, name, int(int_found.group()))
