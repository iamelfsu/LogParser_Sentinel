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


def generate_crisis_report(data, output_path):

    # We open the file in "w" (Write) mode to save the analysis results permanently.
    with open(output_path, "w", encoding="utf-8") as f:
        
        f.write("==================================================\n")
        f.write("          SENTINEL AUTOMATED ANALYSIS REPORT       \n")
        f.write("==================================================\n")
        # We embed the numerical data coming from our analysis dictionary inside the curly braces {}.
        f.write(f"Total Lines Scanned  : {data['total_lines']}\n")
        f.write(f"Critical Errors Found: {data['log_counts']['ERROR'] + data['log_counts']['CRITICAL']}\n")
        f.write(f"Warnings Logged      : {data['log_counts']['WARNING']}\n")
        f.write("-" * 50 + "\n\n")

        f.write(" TOP SUSPICIOUS NETWORK ADDRESSES (POTENTIAL THREATS):\n")
        # If our suspicious IP addresses dictionary is completely empty:
        if not data["suspicious_ips"]:
            f.write(" - Status Clean: No suspicious IP patterns discovered.\n")
            
        # We loop through the IP addresses and their loop repetitions (counts) in the dictionary using the .items() method.
        for ip, count in data["suspicious_ips"].items():
            # If an IP address sent 3 or more requests sequentially:
            if count >= 3:
                # # We save this suspicious IP and its attack count to the report file using f.write.
                f.write(f" -> IP: {ip} flagged with {count} malicious requests!\n")
                
        f.write("\n" + "-" * 50 + "\n")

        # We write the results of the error detectors (detectors.py) into the report.
        f.write(f" ERROR SPIKES ({detectors.SPIKE_LIMIT} OR MORE ERRORS IN THE SAME MINUTE):\n")
        # If no minute reached the error limit:
        if not data["error_spikes"]:
            f.write(" - Status Stable: No error spikes found.\n")
        # We loop through every spike and write its minute and error count.
        for minute, count in data["error_spikes"]:
            f.write(f" -> {minute} : {count} errors in one minute!\n")
        f.write("\n")

        f.write(" ISOLATED CRITICAL CRIDER GONE LOGS:\n")
        # If our collected crisis lines list is completely empty (Meaning if there are no 'ERROR' or 'CRITICAL' logs in the system):
        if not data["crisis_lines"]:
            f.write(" - Status Stable: No critical errors found in logs.\n")
        # We loop through all the critical error lines accumulated in our list.
        for crisis_line in data["crisis_lines"]:
            # We append each critical error to the very bottom of our report file line by line.
            f.write(crisis_line)

    print(f" Scan finished successfully. Scanned {data['total_lines']} lines.")
    print(f" Detailed crisis report saved to '{output_path}'.")
