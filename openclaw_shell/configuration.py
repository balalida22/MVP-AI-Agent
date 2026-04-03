from dataclasses import dataclass, fields
from pathlib import Path

from typing import Any, Self

@dataclass
class Config:
    base_dir: Path
    session_dir: Path
    workspace_dir: Path
    max_chars: int = 3000
    context: int = 1_024_000
    chars_per_token_estimate: int = 4
    finish_prefix: str = "FINISH:"
    command_key: str = "COMMAND:"
    verbose: bool = True
    think: bool = True
    stylize_with_colorama: bool = True

    def construct(obj: dict[str, Any]) -> Self:
        ans = Config(base_dir=None, session_dir=None, workspace_dir=None)
        for field in fields(ans):
            key = field.name
            value = Path(obj[key]) if key.endswith("_dir") else obj[key]
            setattr(ans, key, value)
        return ans

    def serialize(self) -> dict[str, Any]:
        result = {}
        for field in fields(self):
            key = field.name
            value = getattr(self, key)
            if not isinstance(value, int) and not isinstance(value, float) and not isinstance(value, bool) and value is not None:
                result[key] = str(value)
            else:
                result[key] = value
        return result