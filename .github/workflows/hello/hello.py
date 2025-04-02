import os
import datetime

name = os.getenv("INPUT_NAME", "Developer")
print(f"Hello, {name}!")

current_time = datetime.datetime.utcnow().isoformat()
print(f"::set-output name=current_time::{current_time}")