# ACNH Recovery Tool
# Created on 17/3/2026
# Created by mitzikritzi2191

# Import the libraries this program will be using
import os
import shutil
from pathlib import Path

# Declare where the user's home directory is
home = Path.home()
# Assign a variable to where our recovered save file will be going
recovered_save = f"{home}\\Downloads\\ACNH_Save_File"
# Assign what directory Eden and Citron's recovered save will be going into
eden_recovered_save = f"{recovered_save}\\Eden"
citron_recovered_save =f"{recovered_save}\\Citron"
# Define where appdata is
app_data = os.getenv('APPDATA')
# Define where the save directories for acnh are in both Eden and Citron
acnh_save_path_eden = f"{app_data}\\eden\\nand\\user\\save\\0000000000000000\\00000000000000000000000000000000\\01006F8002326000"
acnh_save_path_citron = f"{app_data}\\citron\\nand\\user\\save\\0000000000000000\\00000000000000000000000000000000\\01006F8002326000"

# Inform the user what we want to do
print("Welcome to the save recovery tool for ACNH!!")
print("What this tool aims to do is enter Eden and Citron's appdata folder and extract your save file")
print("Then I will store the file in your computer's Downloads folder!")
# ...and ask the user to press enter once they have read it
user_input = input("Press enter once you have read this message!")

# Create the folders
def makeFolder(eden_recovered_save, citron_recovered_save):
    # Tell the user we are making the folder
    print("Now creating the recovery folder...")
    try:
        # Make the folders
        os.makedirs(eden_recovered_save)
        os.makedirs(citron_recovered_save)
    except FileExistsError:
        # If the folders already exist, remove them and recreate them
        print("Looks like the folders already exist! I will remove them, then remake them!")
        shutil.rmtree(eden_recovered_save)
        shutil.rmtree(citron_recovered_save)
        os.makedirs(eden_recovered_save)
        os.makedirs(citron_recovered_save)
    # Inform the user that the folder is successfully created
    print("Recovery folders created!")
# Run the function
makeFolder(eden_recovered_save, citron_recovered_save)
# Inform the user what we are doing next
print("I am now going to search your Eden and Citron Appdata folders for any ACNH save files!")

# Move the folders
def moveFolders(acnh_save_path_eden, acnh_save_path_citron, eden_recovered_save, citron_recovered_save):
    try:
        # Moving time
        shutil.move(acnh_save_path_eden, eden_recovered_save)
        print(f"Your Eden save data has been moved to {eden_recovered_save}\\01006F8002326000!!")
    # If we can't find the folder we need, inform the user that we can't find it
    except FileNotFoundError:
        print("No Eden Save Data Detected in Appdata!")
    # This does what lines 54 - 60 do but for Citron instead of Eden
    try:
        shutil.move(acnh_save_path_citron, citron_recovered_save)
        print(f"Your Citron save data has been moved to {citron_recovered_save}\\01006F8002326000!!")
    except FileNotFoundError:
        print("No Citron Save Data Detected in Appdata!")
# Execute the function
moveFolders(acnh_save_path_eden, acnh_save_path_citron, eden_recovered_save, citron_recovered_save)
# Tell the user we moved em and explain what to do with the moved files
print("Your save file has been moved!")
print("Please open your emulator, right click ACNH, then click 'Open Save Data Location' and move the contents of the '01006F8002326000' folder")
print("into the window that opens!")