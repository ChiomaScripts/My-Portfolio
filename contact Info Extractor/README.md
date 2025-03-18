# 📌 Contact Info Extractor

## 📌 Project Overview
This Python script scans a text file for **phone numbers, email addresses, and website URLs**, then extracts them into **separate text files** for easy access. It uses **regular expressions (regex)** to perform the extraction and **file operations** to store the results.

## 🔧 Features
- ✅ **Extracts phone numbers**, email addresses, and websites from a text file.
- ✅ **Uses regex patterns** to identify and categorise contact details.
- ✅ **Saves extracted data** into separate files (`phone_numbers.txt`, `email.txt`, `websites.txt`).
- ✅ **Avoids duplicates** to ensure unique results.
- ✅ **Simple and efficient**—ideal for automating contact information retrieval.

---

## 📂 Project Structure
```
|-- contact_info_extractor_project.py # Main script to extract contact details 
|-- example_email.txt                 # Sample email file for testing 
|-- phone_numbers.txt                 # Extracted phone numbers (generated output) 
|-- email.txt                         # Extracted email addresses (generated output) 
|-- websites.txt                      # Extracted website URLs (generated output) 
|-- README.md # Project documentation
```

---

## 🚀 Technologies Used
- **Python**
- **Regular Expressions (`re`)** → For pattern matching
- **File Handling (`open()` function)** → To read input and write output

---

## 📜 Usage

1. **Navigate to the Project Directory**
   Copy and run the following link:
```
https://github.com/ChiomaScripts/My-Portfolio/tree/bde6e62310c82c08ba9af2d153c1dbab9659891c/Automated%20Files%20%26%20Folders%20Organiser
```

2. **Prepare the input file**
   Ensure the text file `(example_email.txt)` contains the contact information you want to extract.

3. **Run the Script**
   `python contact_info_extractor_project.py`

4. **View Extracted Data**
   The script will create and store extracted details in:
   - `phone_numbers.txt` → Contains extracted phone numbers.
   - `email.txt` → Contains extracted email addresses.
   - `websites.txt` → Contains extracted website URLs.
  

## 🛠 Future Improvements
- 🔹 **Improve phone number regex** to support international formats (e.g., +44, +234).
- 🔹 **Extract social media links** in addition to websites.
- 🔹 **Improve website regex** to support websites other than those ending with `.com`, `.net`, or `.org`.
- 🔹 **Enhance error handling** to manage corrupt or missing input files.
- 🔹 **GUI interface** for easier file selection and extraction.


## 📜 License
This project is licensed under the **MIT License**.






