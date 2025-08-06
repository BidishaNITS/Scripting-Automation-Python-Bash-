from collections import Counter
import re

ip_counter = Counter()
ua_counter = Counter()
not_found = []

with open("sample_access.log", "r") as f:
    for line in f:
        match = re.search(r'(\d+\.\d+\.\d+\.\d+).+" (\d{3}) \d+ ".+" "(.+)"', line)
        if match:
            ip, status, ua = match.groups()
            ip_counter[ip] += 1
            ua_counter[ua] += 1
            if status == "404":
                not_found.append(line.strip())

with open("report.txt", "w") as out:
    out.write("🔝 Top 10 IPs:\n")
    for ip, count in ip_counter.most_common(10):
        out.write(f"{ip} — {count} hits\n")

    out.write("\n Top 10 User Agents:\n")
    for ua, count in ua_counter.most_common(10):
        out.write(f"{ua} — {count} times\n")

    out.write("\n 404 Not Found Requests:\n")
    for line in not_found:
        out.write(f"{line}\n")