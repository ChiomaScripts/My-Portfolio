import re

# lists to store the extracted data
phone_numbers = []
email_addresses = []
websites = []

# regex patterns
regex_numbers = r"(\d{3}[- ]\d{3}[- ]\d{4})|(\(\d{3}\)[- ]\d{3}[- ]\d{4})"
regex_emails = r"(\w+@\w+\.\w{3})|(\w+\.\w+@\w+\.\w{3})"
regex_websites = r"\w{6,}\.\w{3}"


# read input file
with open("example_email.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:

        # find matches
        matched_numbers = re.findall(regex_numbers, line)
        matched_emails = re.findall(regex_emails, line, flags=re.IGNORECASE)
        matched_website = re.findall(regex_websites, line, flags=re.IGNORECASE)

        # store unique contact details
        for number in matched_numbers:
            if number is not None and phone_numbers.count(number) == 0:
                phone_numbers.append(number)

        for email in matched_emails:
            if email is not None and email_addresses.count(email) == 0:
                email_addresses.append(email)

        for website in matched_website:
            if website is not None and websites.count(website) == 0:
                websites.append(website)


# print(phone_numbers)
# print(email_addresses)
# print(websites)

with open("phone_numbers.txt", "w") as file:
    for item in phone_numbers:
        file.writelines(item)
        file.write("\n")

with open("email.txt", "w") as file:
    for item in email_addresses:
        file.writelines(item)
        file.write("\n")

with open("websites.txt", "w") as file:
    for item in websites:
        file.writelines(item)
        file.write("\n")