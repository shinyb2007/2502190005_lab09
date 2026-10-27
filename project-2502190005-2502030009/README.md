# Village Borewell Pump Telemetry Data Layer

## Problem & User
Rural drinking-water pumps fail when field technicians miss abnormal voltage spikes and sustained overcurrent. This project helps Panchayat Water Technicians quickly ingest daily telemetry, reject malformed records, and produce an audit report for maintenance decisions.

## Input Format
Records in `data/sample.txt` use pipe-delimited format:
`YYYY-MM-DD|PUMP_ID|VOLTAGE|CURRENT|STATUS`

Example:
`2026-10-01|PUMP-01|220|14.2|OK`

Physical validation rules:
- Voltage safe envelope: 160V - 280V
- Current safe envelope: 0.0A - 40.0A

## Project Structure
```text
project-2502190005-2502030009/
├── README.md
├── datalayer.py
├── main.py
├── data/
│   └── sample.txt
├── reports/
│   └── report_YYYY-MM-DD_HHMM.txt
└── 2502190005_lab09.py
```

## How to Run
From inside the project folder:

```bash
python main.py
```

## Output
The program reads `data/sample.txt`, validates each row, ignores malformed entries in the summary, and writes a timestamped audit report to `reports/report_YYYY-MM-DD_HHMM.txt`.

## Notes
This repository is intentionally designed so that a stranger can clone it and run the program without any hidden setup or commented-out generation scripts.
