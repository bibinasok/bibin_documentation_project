import os
import subprocess
import shutil

# Check if a folder exists, else create it
folder_name = "my_project"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Created folder: {folder_name}")

# Check if Docker is installed
if shutil.which("docker") is None:
    print("Docker is not installed. Please install it manually.")
else:
    print("Docker is installed.")

# Run a shell command (pull an image)
subprocess.run("docker pull nginx", shell=True)
