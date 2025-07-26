import re
def classify_with_regex(log_message):
    regex_patterns = {
        r"User User\d+ logged (in|out).": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed succesfully.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded succesfully by user .*": "System Notification",
        r"Disk cleanup completed succesfully.": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Acoount with ID .* created by .*": "User Action"
    }
    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label
    return "Other"

if __name__ == "__main__":
    print(classify_with_regex("User User123 logged in."))
    print(classify_with_regex("Backup started at 12:00."))
    print(classify_with_regex("Backup completed succesfully."))
    print(classify_with_regex("System updated to version 1.0.0."))
    print(classify_with_regex("File file1.txt uploaded succesfully by user user1."))
    print(classify_with_regex("Disk cleanup completed succesfully."))
    print(classify_with_regex("System reboot initiated by user user1."))
    print(classify_with_regex("Hi !!."))