import pathlib
import subprocess
import sys

codeFolder = pathlib.Path(__file__).parent.parent.resolve()
pybricks = codeFolder.joinpath(".venv", "Scripts", "pybricksdev.exe")

fileToRun = sys.argv[1]

robot_hub = ""
hub_file_path = codeFolder.joinpath("hub.txt")
if hub_file_path.exists():
    lines = hub_file_path.read_text().splitlines()
    if len(lines) > 0:
        robot_hub = lines[0]

process_args = [
    pybricks,
    "run",
    "ble",
    # "--name",
    # robot_hub,
    # "C:\\git\\submerged\\code\\r01_unexpected_encounter.py",
    fileToRun,
]

if robot_hub != "":
    process_args.extend(["--name", robot_hub])

subprocess.run(process_args)
