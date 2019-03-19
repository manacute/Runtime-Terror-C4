import os
import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]
os.environ['TCL_LIBRARY'] = r"C:\Users\max7h\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\max7h\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6"

cx_Freeze.setup(
    name="FourInARow",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":[]}},
    executables = executables

    )