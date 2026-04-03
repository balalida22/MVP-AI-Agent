"""
Interactive MVP agent runner.

The agent reads prompt context from `agent.md` and `SKILL.md`, then loops over
user input, calling either Ollama (local) or Claude API and executing commands returned as:
`COMMAND: <shell command>`.
"""


import os
import subprocess
from typing import Any

import anthropic
import ollama

from .configuration import Config

def _load_text(path: str, config: Config) -> str:
    with open(config.base_dir / path, "r", encoding="utf-8") as f:
        return f.read()


def _is_claude_model(model: str) -> bool:
    return model.startswith("claude-")


def _chat_with_ollama(model: str, chat_messages: list[dict[str, str]]) -> dict[str, Any]:
    response: dict[str, Any] = ollama.chat(
        model=model,
        messages=chat_messages,
        # options={"temperature": 0.1},
        think=True,
    )
    return {
        "reply": response["message"]["content"],
        "prompt_tokens": response.get("prompt_eval_count"),
    }


def _chat_with_claude(model: str, chat_messages: list[dict[str, str]]) -> dict[str, Any]:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError(
            "ANTHROPIC_API_KEY is not set. Set it before using Claude models."
        )

    system_parts = [m["content"] for m in chat_messages if m["role"] == "system"]
    non_system_messages = [
        {"role": m["role"], "content": m["content"]}
        for m in chat_messages
        if m["role"] in {"user", "assistant"}
    ]

    if not non_system_messages:
        non_system_messages = [{"role": "user", "content": "Hello."}]

    client = anthropic.Anthropic(api_key=api_key)
    kwargs: dict[str, Any] = {
        "model": model,
        "messages": non_system_messages,
        "max_tokens": 1024,
    }
    if system_parts:
        kwargs["system"] = "\n\n".join(system_parts)

    response = client.messages.create(**kwargs)
    reply_text = "".join(
        block.text for block in response.content if getattr(block, "type", "") == "text"
    )
    input_tokens = getattr(response.usage, "input_tokens", None)
    return {"reply": reply_text, "prompt_tokens": input_tokens}


def chat_with_model(model: str, chat_messages: list[dict[str, str]]) -> dict[str, Any]:
    """Call the correct backend based on the model name."""
    if _is_claude_model(model):
        return _chat_with_claude(model, chat_messages)
    return _chat_with_ollama(model, chat_messages)

def load_system_prompt(config: Config):
    system_prompt = _load_text("agent.md", config) + _load_text("SKILL.md", config)
    return system_prompt

def truncate_output(output: str, max_chars: int) -> str:
    if len(output) <= max_chars:
        return output
    half = max_chars // 2
    omitted = len(output) - max_chars
    return output[:half] + f"\n\n... ({omitted} chars omitted) ...\n\n" + output[-half:]


def confirm_and_run(command: str, config: Config) -> str:
    choice = input(f"\n[Run Command?] {command} [y/N] ").strip().lower()
    if choice != "y":
        return "User chose not to execute the command."
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    output_lines = []
    for line in process.stdout:
        output_lines.append(line)
        if config.verbose:
            print(line, end="", flush=True)
    process.wait()
    return_code = process.returncode
    output = truncate_output("".join(output_lines), config.max_chars)
    return output if output else f"(exit code {return_code}, no output)"


def reset(config: Config) -> tuple[float, list[dict[str, str]]]:
    """Reset conversation history and token usage estimation."""
    system_prompt = load_system_prompt(config)
    new_tokens_used = len(system_prompt) / config.chars_per_token_estimate
    new_messages = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": "Hello! How can I assist you today?"},
    ]
    return new_tokens_used, new_messages

