# We import the argparse library to accept arguments from the command line (Terminal).
import argparse
# We add the sys library to terminate the program safely in case of error situations (sys.exit).
import sys
# We add the operating system module to check file and folder paths (os.path).
import os

def analyze_log(log_file_path):
    # We check if the file exists on the computer with os.path.exists, and if it is really a file with os.path.isfile.
    # If the file does not exist, we establish this security wall to prevent the program from crashing, meaning blowing up.
    if not os.path.exists(log_file_path) or not os.path.isfile(log_file_path):
        print(f" ERROR: '{log_file_path}' is not a valid log file or was not found!")
        # We close the program safely by giving code '1' (Error occurred) to the operating system.
        sys.exit(1)
        
    # We check whether the file size is 0, meaning empty, with os.path.getsize.
    if os.path.getsize(log_file_path) == 0:
        print(f" WARNING: '{log_file_path}' file is empty. No data to analyze.")
        # If the file is empty, we close the program with code 0, meaning the hassle-free code, stating that the process finished successfully.
        sys.exit(0)

    # We create this dictionary that I created in a way that it will hold the total number of lines, the crisis line list, error counts, and the frequencies of suspicious IP addresses.
    analysis_data = {
        "total_lines": 0,
        "crisis_lines": [],
        # We open an empty List to accumulate matching error lines.
        "log_counts": {"CRITICAL": 0, "ERROR": 0, "WARNING": 0},
        # Our counter that accumulates numbers.
        "suspicious_ips": {}
        # We open an empty IP frequency dictionary for suspicious IP detection.
    }

    # Here, when the process is finished or if the code throws an error, it automatically closes the file safely.
    with open(log_file_path, "r", encoding="utf-8") as file:
        # We read the file line by line, not as a whole text, with a 'for' loop.
        # We number the lines starting from 1 using the enumerate(file, 1) function (For the tracking of the line number).
        for line_num, line in enumerate(file, 1):
            # We increment the total line counter in our dictionary by 1 on every line.
            analysis_data["total_lines"] += 1
            # We clean invisible spaces or newline (\n) characters at the beginning and end of the line with .strip().
            clean_line = line.strip()

            # We loop through the log level keys ('CRITICAL', 'ERROR', 'WARNING') inside our dictionary one by one.
            for level in analysis_data["log_counts"]:
                # We normalize the text by converting the line to uppercase with .upper() for a case-insensitive search.
                if level in clean_line.upper():
                    # If the current log level is found inside the line, we increment the counter of that log level in the dictionary by 1.
                    analysis_data["log_counts"][level] += 1
                    # If the log level is 'ERROR' or 'CRITICAL', which are the most dangerous ones, we save it to the list (.append method we use) by adding the line number to the front so the error can be found.
                    if level in ("ERROR", "CRITICAL"):
                        analysis_data["crisis_lines"].append(f"[Line {line_num}] {clean_line}\n")

            # # If the keyword 'IP:' is found inside the cleaned line...
            if "IP:" in clean_line.upper():
                # We established a try-except block to prevent the code from crashing if a malformed line or something occurs.
                try:
                    # We split the line from the 'IP:' keyword and take the right side (with [1]).
                    # Then we isolate the IP address from other text on its right by applying .strip().split()[0].
                    ip_address = clean_line.upper().split("IP:")[-1].strip().split()[0]
                    
                    # If this IP already exists in the dictionary, we increment its count by 1, if it is seen for the first time in the dictionary, we start it from 0 and add 1 without getting an error with the .get() method.
                    analysis_data["suspicious_ips"][ip_address] = \
                        analysis_data["suspicious_ips"].get(ip_address, 0) + 1
                except IndexError:
                    # If an index error occurs during the split process, do not crash the program, just skip (with continue) that line.
                    continue

    # After the entire file is scanned line by line, we return the dictionary that we filled to where the function was called.
    return analysis_data