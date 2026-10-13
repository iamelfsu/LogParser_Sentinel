# We include the built-in random library to generate random data distribution and selections.
import random
# We use these modules to create a chronological flow in log records and calculate timestamps backward.
from datetime import datetime, timedelta

# We define the main function that takes the file name and line count parameters from outside, generating 10,000 lines by default.
def generate_log(file_name="server.log", line_count=10000):
    print(f" Generating {line_count} lines of log file...")

    # We create a random pool consisting of IP addresses frequently used in local networks.
    ip_pool = ["192.168.1.15", "10.0.0.4", "172.16.254.1", "192.168.1.50"]
    # We determine a completely foreign and threatening random static IP.
    attacker_ip = "185.22.45.10"
    # We put page directories representing user routes and endpoints in a typical web application into a list.
    endpoints = ["/home", "/products", "/cart", "/checkout", "/profile"]

    # We list the system event levels (log categories) that the server can throw.
    log_levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]
    # We assigned weights (probability percentage) to events to mimic server routines in real life.
    weights = [85, 12, 2.5, 0.5]
    # Based on the system time, we create our time reference point that allows logs to flow starting exactly 1 day (24 hours) ago.
    start_time = datetime.now() - timedelta(days=1)

    # We wrote it like this so that the file is automatically closed by the operating system when the process is finished.
    with open(file_name, "w", encoding="utf-8") as f:
        # We start our main automation loop that will iterate sequentially throughout the line count limit we specified.
        for i in range(line_count):
            # In each loop step, we tried to create a chronological line by advancing the time randomly between 0.1 and 2 seconds.
            timestamp = start_time + timedelta(seconds=i * random.uniform(0.1, 2))
            # We convert the time data into a standard text format (Year-Month-Day Hour:Minute:Second) that users can easily read on the screen.
            timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            # Using the probability weights we determined before, we try to select a random log level specific to that line from the list.
            level = random.choices(log_levels, weights=weights)[0]

            # If 'INFO' was selected by chance for that line, we created a random page navigation template with a clean IP.
            if level == "INFO":
                line = f"[{timestamp_str}] INFO: User viewed {random.choice(endpoints)} page. IP: {random.choice(ip_pool)}\n"
            # If the status is 'WARNING'; we configure a resource alert line hitting the server load with random numbers between 75% and 89%.
            elif level == "WARNING":
                line = f"[{timestamp_str}] WARNING: Server memory usage reached {random.randint(75, 89)}% capacity.\n"
            # If the status is 'ERROR', we tried to create the 500 server timeout error.
            elif level == "ERROR":
                line = f"[{timestamp_str}] ERROR: Error occurred while loading {random.choice(endpoints)}. Status Code: 500 Timeout\n"
            # If it is in the System crisis 'CRITICAL' status, we tried to create a cyber threat situation.
            elif level == "CRITICAL":
                # If the loop counter happens to be exactly between 50,000 and 50,015 lines, this code leaves a sequential attack trace on the system.
                if 50000 < i < 50015:
                    line = f"[{timestamp_str}] CRITICAL: Unauthorized admin panel access attempt! IP: {attacker_ip}\n"
                else:
                    # In all other critical situations, we prepared an ordinary database disconnection error case.
                    line = f"[{timestamp_str}] CRITICAL: Database connection lost! IP: {random.choice(ip_pool)}\n"

            # We print the log line to the physical file.
            f.write(line)
        # For now, we wrote a confirmation message stating that the file was successfully saved to disk when the loop finished.
        print(f"'{file_name}' file has been created. Ready for testing.\n")


# When this script we wrote is run directly from the terminal (with 'python kod.py' for example), we ensured that the function is automatically triggered here.
if __name__ == "__main__":
    generate_log()
