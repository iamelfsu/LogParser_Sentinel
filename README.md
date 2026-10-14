
# What Does LogParser-Sentinel Do?

- When a website or application runs, a massive log file explaining what is happening in the background is continuously generated inside the server. If these log files are not carefully parsed, discovering critical system vulnerabilities and hidden operational errors becomes nearly impossible. Searching for critical errors and security threats manually within thousands or millions of lines of raw text is highly inefficient and impractical.

- This is exactly where our **LogParser-Sentinel** project comes into play. Designed as a lightweight, memory-efficient automation script, it dives into massive chunks of text data and automatically extracts the most dangerous situations (such as lines tagged with `ERROR` and `CRITICAL`) along with their exact, 1-based line numbers. 

- Moreover, beyond simply looking for string keywords, the program performs intelligent cyber attack detection in the background by dynamically tracking IP address frequencies. If a specific network address sends too many consecutive or unusual requests to the server, Sentinel immediately flags it as a malicious botnet or brute force attempt, generating an automated structural alert inside the final crisis report.

- In addition to structural threat tracking, the engine calculates statistical server density metrics in real time. It monitors hardware capacity anomalies and isolates high-frequency operational error bursts aggregated within strict chronological time slices to deliver a comprehensive security and performance audit without requiring manual human oversight.

---

## 📁 Repository Directory Map & Script Architecture

### 📥 The Root Directory Files
*   **`sentinel.py`**: This is the primary system application and main CLI automation entry point. It captures input flags natively, establishes a memory-optimized file pipeline to read production records, filters threat anomalies via advanced data collections, and automatically generates the structured `crisis_report.txt`.
*   **`log_generator.py`**: This serves as our helper test simulation laboratory. It utilizes weighted loops and time deltas to construct a realistic 10,000-line server dataset populated with artificial cyber attack patterns, allowing instant local verification of our core analysis logic.
*   **`detectors.py`**: This acts as our internal algorithmic monitoring engine. It executes statistical analytics over the row stream, calculating high-frequency error spikes per minute using dictionary wrappers and tracking severe system memory pressure thresholds via robust try-except error containment boundaries.
*   **`.gitignore`**: A Git configuration layer that programmatically marks runtime file dumps (`server.log` and `crisis_report.txt`) as untracked. This ensures that massive dynamic outputs never clutter or bloat our public upstream repository. 
*   **`README.md`**: This current documentation guide, providing a technical breakdown of the system and mapping our real-world automated business impacts directly to our weekly lecture topics.

### 👥 The `contributions/` Folder (Group Mandate Compliance)
As required by the official portfolio guidelines, this dedicated folder contains individual Markdown (`.md`) documentation logs tracking the team's distributed tasks:
*   **`ELİF_SU_İLERİ_2305041041_iamelfsu.md`**: Developed detectors.py, integrated detectors to sentinel and finalized the project.

*   **`HİLAL_ONAY_2609011056_nyx78.md`**: Worked on developing the CLI (Command Line Interface) and developed log_generator.py.

*   **`SEDANUR_BAYRAM_2509051037_sedabayram.md`**: Writes the full report (summary, suspicious IPs, error spikes, critical lines) using with open(..., "w"), f-strings and loops over dictionaries, tuples and lists, then prints a confirmation.
*   **`YAVUZ_SELİM_DİLMEN_2509051036_yavuzdilmen.md`**: Worked on sentinel by validating the file with os/sys, reads it line by line into an analysis_data dictionary, saves numbered ERROR/CRITICAL lines, and counts suspicious IPs safely with try-except and .get().

---

## ⚙️ Step-by-Step Execution Workflow (How to Test & Run)

To evaluate the core automation metrics of Sentinel, follow these two sequential terminal execution steps in your command-line environment (VS Code Terminal / Bash):

### Step 1: Initialize the Local Data Factory (Log Generation)
Before auditing threats, the environment needs realistic server files. Execute the simulator module to dynamically generate a test infrastructure:
```bash
python log_generator.py
```
*   **System Action:** This triggers our weighted memory loops. It immediately flushes any stale data and streams exactly 10,000 unique cronological records populated with hidden system errors into a local `server.log` file.

### Step 2: Fire the Primary Monitoring Engine (CLI Triage Audit)
Once the data factory populates the directory, execute our primary Command-Line Interface (CLI) engine to filter anomalies and map threat statistics:
```bash
python sentinel.py --log server.log
```
*   **System Action:** Our `argparse` mechanism intercepts the `--log` flag natively from the terminal boundary. The pipeline processes the file row by row, updates our internal dictionary counters, and programmatically exports the complete security triage summary into a permanent `crisis_report.txt` file.

### Optional: Define a Custom Output Path
If you want to dictate a custom path or name for the generated text report instead of using the default filename, you can append the optional `--output` flag:
```bash
python sentinel.py --log server.log --output professor_review.txt
```
---


