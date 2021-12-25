# debugger.py
from os import getenv

import debugpy


def init_debug():
    if getenv("DEBUGGER") == "True":
        debugpy.listen(("0.0.0.0", 10002))
        print("⏳ VS Code debugger can now be attached, press F5 in VS Code ⏳")
        debugpy.wait_for_client()
        print("🎉 VS Code debugger attached, enjoy debugging 🎉")
