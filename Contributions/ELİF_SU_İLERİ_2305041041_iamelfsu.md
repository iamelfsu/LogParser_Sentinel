My Contributions

I developed detectors.py, the file that holds our error detectors, and connected it to sentinel.py so its results appear in the same crisis_report.txt and did the last round of checks before finalizing the code.

The first version only counted errors and warnings. I added two detectors that find problems it could not see:

Error spikes (find_error_spikes): finds the minutes in which 5 or more ERROR or CRITICAL lines happened. It takes the minute from the time at the start of each line and counts the errors of each minute in a dictionary. A burst of errors in one minute usually means the server is breaking down.
Memory pressure (find_memory_pressure): reads the percentage in lines like "Server memory usage reached 87% capacity" and finds how many times memory usage reached 85% or more, and the highest value. Broken lines are skipped with try/except instead of crashing the program.

The limits are stored as two constants at the top of the file (SPIKE_LIMIT and MEMORY_LIMIT), so they are easy to change.

To connect the detectors, I imported detectors.py in sentinel.py, called both functions at the end of analyze_log(), and added two new sections ("ERROR SPIKES" and "MEMORY PRESSURE") to the report in generate_crisis_report(). I did not change any of the existing code. I also added __pycache__/ to .gitignore, since Python creates that folder when one file imports another.

I tested it on our server.log: it found 7 error spikes and reported that memory reached 85% or more 411 times, with a highest value of 89%. I also checked that empty files, missing files and broken memory lines do not crash the program, and that the rest of the report stayed the same as before.

Lastly I fixed any bugs we may had, make sure detetor and sentinel worked correctly and the data output was being sent to the crisis_report and finished the project.