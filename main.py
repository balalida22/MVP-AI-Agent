import ollama
import subprocess
import os
import re
MODEL = "mistral-nemo:12b"
CONTEXT = 1024000
MAX_CHARS = 3000
tokens_used = 0
system_prompt = open("agent.md", "r").read()+open("SKILL.md", "r").read()

def truncate_output(output: str, max_chars: int = MAX_CHARS) -> str:
    if len(output) <= max_chars:
        return output
    half = max_chars // 2
    omitted = len(output) - max_chars
    return output[:half] + f"\n\n... ({omitted} chars omitted) ...\n\n" + output[-half:]

def strip_thinking(reply: str) -> str:
    return re.sub(r"<think>.*?</think>", "", reply, flags=re.DOTALL).strip()

def confirm_and_run(command: str, verbose = True) -> str:
    choice = input(f"\n[Run Command?] {command} [y/N] ").strip().lower()
    if choice != "y":
        return "User chose not to execute the command."
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        # env=os.environ.copy()
    )
    output_lines = []
    for line in process.stdout:
        output_lines.append(line)
        if verbose:
            print(line, end="", flush=True)
    process.wait()
    return_code = process.returncode
    output = truncate_output("".join(output_lines))
    return output if output else f"(exit code {return_code}, no output)"

def reset_messages():
    return [{"role": "system", "content": system_prompt},
            {"role": "assistant", "content": "Hello! How can I assist you today?"}]

tokens_used = len(system_prompt)/4
messages = reset_messages()
print("[Commands: 'exit' to quit, 'reset' to clear history]")
while True:
    pct = round((tokens_used / CONTEXT) * 100, 1)
    user_input = input(f"\n[User({pct}%)] ")
    if user_input.lower() in ("exit", "quit"):
        print("Goodbye!")
        break
    if user_input.lower() == "reset":
        tokens_used = len(system_prompt)/4
        messages = reset_messages()
        continue
    if not user_input:
        continue
    messages.append({"role": "user", "content": user_input})
    while True:
        response = ollama.chat(model=MODEL, messages=messages,
                            #    options={"temperature": 0.1},
                            #    think=True
                               )
        tokens_used = response.get("prompt_eval_count", tokens_used)
        reply = response["message"]["content"]
        print(f"<DEBUG>{reply}<DEBUG>")
        
        messages.append({"role": "assistant", "content": reply})
        if reply.strip().startswith("FINISH:"):
            finish_message = reply.strip().split("FINISH:", 1)[1].strip()
            print(f"\n[Agent] {finish_message}")
            break
        if "COMMAND:" in reply:
            command_result = confirm_and_run(command = reply.strip().split("COMMAND:")[1].strip(), verbose = True)
            messages.append({"role": "user", "content": f"EXECUTED {command_result}"})
        else:
            messages.append({"role": "user", "content": "Invalid format. You must reply with either \nCOMMAND: <cmd> or \nFINISH: <msg>. Try again."})
        # print(messages)