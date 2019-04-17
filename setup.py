import cx_Freeze
executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(name = "OS",options={"build_exe":{"packages":["gi"]}},executables=executables)
