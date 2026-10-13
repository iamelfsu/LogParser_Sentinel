- Opens the output file with `with open(output_path, "w", encoding="utf-8")`, so the
  report is created from scratch on every run and the file is closed automatically
  (Week 2, slide 23 – write mode; Week 2, slide 21 – the `with` statement).
- Writes a header and the summary numbers with f-strings: total lines scanned,
  critical errors (`ERROR` + `CRITICAL` counts added together) and warnings
  (Week 3, slide 37 – f-strings; Week 3, slide 13 – reading values from a dictionary).
- Suspicious IP section: loops over `data["suspicious_ips"].items()` and writes every
  IP that appears 3 or more times; if the dictionary is empty it writes a "Status Clean"
  line instead (Week 3, slide 16 – looping over key–value pairs with `.items()`;
  Week 1 – `if` conditions and comparisons).
- Error-spike section: loops over the `(minute, count)` tuples in `data["error_spikes"]`
  and writes one line per spike; the heading uses `detectors.SPIKE_LIMIT`, so the text
  follows the constant automatically (Week 3, slide 19 – tuples; slide 12 – constants).
- Critical-log section: writes every saved `"[Line n] ..."` entry from
  `data["crisis_lines"]`, or a "Status Stable" line when the list is empty
  (Week 2, slide 24 – looping over a list and writing results to a file).
- Prints a short confirmation to the terminal with the number of scanned lines and
  the report path.