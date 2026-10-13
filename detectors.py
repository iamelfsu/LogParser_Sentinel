# This file holds our error detectors. sentinel.py imports it and calls its two functions.

# We decide that 5 or more errors in the same minute count as an error spike.
SPIKE_LIMIT = 5
# We decide that a memory usage of 85% or more counts as memory pressure.
MEMORY_LIMIT = 85


def find_error_spikes(log_file_path):
    # We create an empty dictionary that will hold how many errors happened in each minute.
    errors_per_minute = {}

    # Here, when the process is finished or if the code throws an error, it automatically closes the file safely.
    with open(log_file_path, "r", encoding="utf-8") as file:
        # We read the file line by line with a 'for' loop, the same way sentinel.py does.
        for line in file:
            # Every line starts with the time, like "[2026-10-12 06:46:39] ERROR: ...".
            # We take the level that comes after the time; "[2026-10-12 06:46:39] " is 22 characters long.
            level = line[22:].split(":")[0]
            # If the line is in our format and its level is 'ERROR' or 'CRITICAL'...
            if line.startswith("[") and level in ("ERROR", "CRITICAL"):
                # We cut the minute out of the time with line[1:17], for example "2026-10-12 06:46".
                minute = line[1:17]
                # We count the error for that minute, starting from 0 with the .get() method if the minute is new.
                errors_per_minute[minute] = errors_per_minute.get(minute, 0) + 1

    # We open an empty list to collect the minutes that had too many errors.
    spikes = []
    # We loop through the minutes in time order with sorted() and the .items() method.
    for minute, count in sorted(errors_per_minute.items()):
        # If a minute reached our limit, we save the minute and its error count together.
        if count >= SPIKE_LIMIT:
            spikes.append((minute, count))

    # We return the list of spikes to where the function was called.
    return spikes


def find_memory_pressure(log_file_path):
    # We start our two counters: how many times memory went over the limit, and the highest value we saw.
    times_over_limit = 0
    highest = 0

    # Here, when the process is finished or if the code throws an error, it automatically closes the file safely.
    with open(log_file_path, "r", encoding="utf-8") as file:
        # We read the file line by line with a 'for' loop.
        for line in file:
            # The lines we want look like: "... WARNING: Server memory usage reached 87% capacity."
            # We check both parts, so there is always something to split on.
            if "memory usage reached " in line and "%" in line:
                # We established a try-except block to prevent the code from crashing if the number is broken.
                try:
                    # We take the text between "reached " and "%" and turn it into a number with int().
                    percent = int(line.split("reached ")[1].split("%")[0])
                except ValueError:
                    # If it is not a number, do not crash the program, just skip (with continue) that line.
                    continue
                # If the memory usage reached our limit, we increment the counter by 1.
                if percent >= MEMORY_LIMIT:
                    times_over_limit += 1
                # If this is the highest value so far, we remember it.
                if percent > highest:
                    highest = percent

    # We return both numbers together to where the function was called.
    return times_over_limit, highest
