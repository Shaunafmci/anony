import os
import sys
import subprocess

# Hardcoded directories and files
HOME_DIR = os.path.expanduser("~")
ROOP_DIR = os.path.join(HOME_DIR, "roop/")
MASKING_FACE_PATH = os.path.join(ROOP_DIR, "test.jpg")
ANONY_VALIDATION_DIR = os.path.join(HOME_DIR, "face_recognition/examples/")

# Check if one argument is provided
if len(sys.argv) != 2:
    print("Usage: python script.py ORIGINAL_VIDEO_PATH")
    sys.exit(1)

# Assign provided argument
ORIGINAL_VIDEO_PATH = sys.argv[1]

# Extract filename from the provided path
ORIGINAL_FILENAME = os.path.basename(ORIGINAL_VIDEO_PATH)

# Define the prefix for the anonymized video
PREFIX = "anony_"
ANONY_VIDEO_FILENAME = f"{PREFIX}{ORIGINAL_FILENAME}"
ANONY_VIDEO_PATH = os.path.join(ROOP_DIR, ANONY_VIDEO_FILENAME)

# Navigate to the folder for the 'roop' project and run it
os.chdir(ROOP_DIR)
print(f"Current working directory: {os.getcwd()}")

subprocess.run([
    "python", "run.py",
    "-s", MASKING_FACE_PATH,
    "-t", ORIGINAL_VIDEO_PATH,
    "-o", ANONY_VIDEO_PATH,
    "--keep-fps", "--keep-frames", "--skip-audio", "--many-faces"
])

# After 'roop' is finished, navigate to the folder for the 'face_recognition' project
os.chdir(ANONY_VALIDATION_DIR)
print(f"Current working directory: {os.getcwd()}")

subprocess.run([
    "python", "facerec_comparison_between_two_video_files.py",
    "-v1", ORIGINAL_VIDEO_PATH,
    "-v2", ANONY_VIDEO_PATH
])

os.chdir(HOME_DIR)
print(f"Returned to home directory: {os.getcwd()}")
