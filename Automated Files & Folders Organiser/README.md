# 📂 Automated File & Folder Organiser

## 📌 Project Overview
This Python script acts as a **"digital janitor"**, automating the organization of files and folders within a user-specified directory. It categorizes text files (`.txt`), CSV files (`.csv`), and directories, while also **removing unnecessary temporary folders**.

## 🔧 Features
- ✅ **Moves files into categorized subfolders** (`txt_files`, `csv_files`, `folders`).
- ✅ **Deletes unwanted "temp" directories** and their contents.
- ✅ **Moves all other files into a general storage directory (`closet`).**
- ✅ **Provides a summary report** after organizing the directory.

## 📂 Project Structure
```
|-- automated_folder_organiser_project.py # Main Python script
|-- messy_directory                       # Folder containing different files and folders that need sorting
|-- README.md                             # Project documentation
```


## 🚀 Technologies Used
- **Python**
- **Pathlib** (`from pathlib import Path`) → Handles file and directory paths.
- **Shutil** (`import shutil`) → Moves and deletes files/directories.

## 📜 Usage

1. **Navigate to the Project Directory**
   Copy and run the following link:
```
https://github.com/ChiomaScripts/My-Portfolio/tree/bde6e62310c82c08ba9af2d153c1dbab9659891c/Automated%20Files%20%26%20Folders%20Organiser
```

2. **Run the Script**
   `automated_folder_organiser_project.py`

3. **Provide Input**
   When prompted, enter the path of the **directory you want to organise**

4. **View Results**
   Once the script completes execution:
   - A **"closet"** folder will be created inside the specified directory.
   - The following subfolders will be inside "closet":
     - 📂 `txt_files` → Stores all `.txt` files.
     - 📂 `csv_files` → Stores all `.csv` files.
     - 📂 `folders` → Stores all non-temp folders.
   - **"temp" directories will be permanently deleted**.
   - A summary report will be displayed

## 📊 Example Run Output
```
Enter the path to the directory you want to organise: C:\Users\John\Documents\UnsortedFiles
The directory exists!
Subfolders successfully created

Project Summary:

3 temp folders successfully deleted
7 csv files successfully moved to the csv folder
5 txt files moved to the txt folder
4 folders moved to folders directory
8 other files moved into closet folder
Folder cleanup complete!
```

## 🛠 Future Improvements
- 🔹 Implement undo functionality in case of accidental file movement.
- 🔹 Add functionality (perhaps a `while loop`) to continuously prompt user to enter a valid path.
- 🔹 Add logging support to track file movements (perhaps using `logging` module in Python).
- 🔹 Enhance GUI version for user-friendly experience.

## ⚠️ Important Notes
- ❗ Use with caution: Deleting "temp" folders is permanent.
- It is advisable to use the files provided with this code as found in the `messy_folder`.

## 📜 License
This project is licensed under the **MIT License**.
