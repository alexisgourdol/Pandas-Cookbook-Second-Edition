import os
import platform
import sys

import numpy as np
import pandas as pd


def show_versions():
    print(
        "OS:",
        os.name,
        "| Platform system:",
        platform.system(),
        "| Platform release:",
        platform.release(),
        "| Platform architecture:",
        platform.architecture(),
    )
    print("Python executable:", sys.executable, "| Python version:", sys.version)
    print("Python path:", sys.path)
    print("Pandas version:", pd.__version__)
    print("NumPy version:", np.__version__)


if __name__ == "__main__":
    show_versions()
