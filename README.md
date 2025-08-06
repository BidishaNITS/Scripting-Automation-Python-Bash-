# Log Security Analyzer

A beginner-friendly Python project that scans Apache-style access logs and extracts:

- Top 10 IP addresses
- Top 10 User-Agent strings
- All 404 Not Found requests (commonly used in recon or bot scans)

This project simulates lightweight SIEM functionality and showcases DevSecOps practices using GitHub Actions for automation.

---

## Project Files

| File                             | Description                                     |
|----------------------------------|-------------------------------------------------|
| `log_parser.py`                 | Python script to parse log data                |
| `sample_access.log`            | Sample Apache log file                         |
| `report.txt`                   | Output file generated after analysis           |
| `.gitignore`                   | Prevents pushing unwanted files                |
| `.github/workflows/log-parser.yml` | GitHub Action to run script on push        |

---

## How to Run (Locally)

```bash
python log_parser.py