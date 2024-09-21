from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class BaseUseCase(ABC):
    @abstractmethod
    async def execute(self, *args: Any, **kwargs: Any) -> Any:
        pass
