from pathlib import Path
import shutil

# The input fxn receives user-specified path, and can thankfully read it as a raw string
user_input = input("Enter the path to the directory you want to organise: ")

# instantiate a path object, using the Path class as a constructor
user_path = Path(user_input)

# check existence of the user-specified directory, and create 1 parent folder & 3 sub-folders inside it namely: closet (parent) and text_files, csv_files, folders (subfolders inside closet)
if user_path.exists():
    print("The directory exists!")

    # Define the parent folder and the list of subfolders
    closet_path = user_path / "closet"
    subfolders = ["txt_files", "csv_files", "folders"]  # while it is possible to achieve same result by manually creating the subfolders one after the other, this method avails us the use of for loops to programmatically create the folders, both ensuring that our code is DRY and scalable

    # Create parent folder
    closet_path.mkdir(exist_ok=True, parents=True)

    # Create the subfolders inside closet folder
    for sub_folder in subfolders:
        (closet_path/sub_folder).mkdir(exist_ok=True)

    print("Subfolders successfully created")

else:
    print("The directory does not exist.")


# Now iterate through the files and folders in the user-specified directory, and programmatically clean it, assigning it to the newly created subfolders, depending on the file type


count_temp = 0
count_csv = 0
count_txt = 0
count_folders = 0
count_other_files = 0

for item in user_path.iterdir():
    if item == closet_path:
        continue

    # Manage folders (move the specified and delete those with the word "temp")
    if item.is_dir():
        if "temp" in item.name.lower():
            shutil.rmtree(item)
            count_temp += 1
        else:
            destination_folder = closet_path / "folders"
            shutil.move(item, destination_folder)
            count_folders += 1

    # Manage CSV files
    elif item.is_file() and item.suffix == ".csv":
        destination_csv = closet_path / "csv_files" / item.name
        shutil.move(item, destination_csv)
        count_csv += 1

    # Manage TXT files
    elif item.is_file() and item.suffix == ".txt":
        destination_txt = closet_path / "txt_files" / item.name
        shutil.move(item, destination_txt)
        count_txt += 1

    # Manage all other files (using an else statement here rather than an elif would result in moving the closet folder as well, which is now what we want. Hence, using an elif to explicitly move all other files (not folders) is the safer way
    elif item.is_file():
        destination_other_files = closet_path / item.name
        shutil.move(item, destination_other_files)
        count_other_files += 1


print("\n")
print("Project Summary:\n")
print(f"{count_temp} temp folders successfully deleted")
print(f"{count_csv} csv files successfully moved to the csv folder")
print(f"{count_txt} txt files moved to the txt folder")
print(f"{count_folders} folders moved to folders directory")
print(f"{count_other_files} other files moves into closet folder")
print("Folder cleanup complete!")