from dataclasses import dataclass
from typing import Any


@dataclass
class APIResponse:
    status: int
    result: dict[Any, Any] | list[dict[Any, Any]] | None
