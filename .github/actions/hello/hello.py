import os
import datetime

# Correctly retrieve the input variable
name = os.getenv("INPUT_NAME", "Developer")  # GitHub passes inputs with "INPUT_" prefix
print(f"Hello, {name}!")

# Set output
current_time = datetime.datetime.utcnow().isoformat()
print(f"::set-output name=current_time::{current_time}")