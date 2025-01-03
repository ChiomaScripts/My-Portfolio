# Password Security Checker

This project leverages the [Have I Been Pwned API](https://haveibeenpwned.com/) to check if a password has been exposed in a data breach. By hashing the password and querying the API, the program ensures that the password itself is never exposed in transit.

## Features

- **Hashing Passwords:** Converts plain-text passwords to SHA-1 hash format.
- **Secure API Queries:** Uses the first 5 characters of the hashed password to query the API, maintaining security and privacy.
- **Leak Detection:** Returns the number of times a password has been leaked in breaches.

## Technologies Used

- Python
- `requests` library for HTTP requests
- `hashlib` for hashing passwords
- `sys` module for command-line input handling (future expansion)

---

## How It Works

1. **Hashing the Password:**
   - The password is hashed using SHA-1 to ensure it is not transmitted in plain text.
2. **Partial Hash Query:**
   - The first 5 characters of the hash are sent to the [Pwned Passwords API](https://haveibeenpwned.com/Passwords) to fetch possible matches.
3. **Tail Comparison:**
   - The remaining hash characters are compared locally with the API response to determine if the password has been compromised.

---

## Code Overview

### Functions

1. `get_data_pawned_url(head_password)`
   - Fetches hash ranges from the API.
   - **Input:** The first 5 characters of the hashed password.
   - **Output:** API response object.

2. `read_response(response)`
   - Outputs the API response text for debugging purposes (optional).

3. `count_password_leaks(hashes_from_response, your_hashed_tail)`
   - Iterates over API results to check if the hashed password tail exists.
   - **Output:** Number of times the password has been leaked.

4. `check_password(your_password)`
   - Combines the above functions to hash the password, query the API, and check for leaks.
   - **Output:** Displays the leak count or confirms password safety.

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/password-security-checker.git

