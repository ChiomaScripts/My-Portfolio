# 📂 Automated File & Folder Organizer

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

1. **Navigate to the Directory**
   Copy and run the following command:
```
https://github.com/ChiomaScripts/My-Portfolio.git
```
   Then, navigate to the project folder:
`cd My-Portfolio/automated_files_&_folders_organiser`

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
