import os
import datetime

# Read input correctly (GitHub sets it as "INPUT_NAME")
name = os.getenv("INPUT_NAME", "Developer")  # ✅ Corrected input handling

# Print output
print(f"Hello, {name}!")

# Get current time
current_time = datetime.datetime.utcnow().isoformat()

# ✅ Fix: Use Environment File Instead of `set-output`
env_file = os.getenv("GITHUB_ENV")  # GitHub provides this path
with open(env_file, "a") as file:
    file.write(f"CURRENT_TIME={current_time}\n")