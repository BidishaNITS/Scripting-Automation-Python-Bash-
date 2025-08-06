# Import necessary Python modules
from collections import Counter  # Helps count how often things appear (like IPs, UAs)
import re  # Regular expressions to extract patterns from log lines

# Initialize counters and a list to store data
ip_counter = Counter()       # To count how many times each IP appears
ua_counter = Counter()       # To count how many times each user-agent appears
not_found = []               # To store all lines with status code 404

# Open the Apache/Nginx access log file for reading
with open("sample_access.log", "r") as f:
    for line in f:  # Go through each line in the log file
        # Use regex to extract:
        # 1. IP address
        # 2. HTTP status code
        # 3. User-Agent string
        match = re.search(r'(\d+\.\d+\.\d+\.\d+).+" (\d{3}) \d+ ".+" "(.+)"', line)
        
        if match:  # If the regex pattern matched the line
            ip, status, ua = match.groups()  # Get the 3 captured values from the match

            ip_counter[ip] += 1   # Increment the count for that IP
            ua_counter[ua] += 1   # Increment the count for that User-Agent
            
            if status == "404":   # If the HTTP status is "404 Not Found"
                not_found.append(line.strip())  # Save the whole line (after removing trailing newline)

# Write results to a report file
with open("report.txt", "w") as out:
    # Write top 10 IPs
    out.write("🔝 Top 10 IPs:\n")
    for ip, count in ip_counter.most_common(10):  # Get top 10 IPs by frequency
        out.write(f"{ip} — {count} hits\n")

    # Write top 10 User Agents
    out.write("\n Top 10 User Agents:\n")
    for ua, count in ua_counter.most_common(10):  # Get top 10 UAs
        out.write(f"{ua} — {count} times\n")

    # Write all 404 Not Found log entries
    out.write("\n 404 Not Found Requests:\n")
    for line in not_found:
        out.write(f"{line}\n")