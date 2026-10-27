# Lab 09 Record

## Brief
Rural drinking-water pumps fail when field technicians miss abnormal voltage spikes and sustained overcurrent conditions. This project helps Panchayat Water Technicians monitor daily pump telemetry, reject bad records, and generate a maintenance summary without silently losing data.

## User
Panchayat Water Technicians and village maintenance staff who review daily pump health logs and need a reliable summary of field equipment condition.

## Function Signatures
```python
import re, os

RECORD = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})\|(?P<pump_id>PUMP-\d{2})\|(?P<voltage>\d+)\|(?P<current>\d+(?:\.\d+)?)\|(?P<status>[A-Z]+)$"
)

def parse_record(line: str) -> dict:
    """One raw line -> a dict of fields. Raises ValueError if malformed."""


def load(path: str) -> tuple[list[dict], list[tuple[int, str, str]]]:
    """Read a file -> (records, problems)."""


def summarise(records: list[dict]) -> dict:
    """records -> a dict of the numbers needed for the final report."""
```

## Decision on the Third Imperfect Line
The third imperfect line is the out-of-range voltage entry:

`2026-10-05|PUMP-01|440|13.8|OK`

This record is syntactically valid but physically impossible for a safe operating range, so it is rejected as an invalid telemetry value. The line with leading spaces is accepted after stripping, while the missing-field line is rejected as malformed.

## Stranger Test Result
A stranger can open the README and run the project without needing extra clarification. The program reads `data/sample.txt`, processes the valid entries, records malformed or invalid ones in the problems section, and writes a dated report in `reports/`. If the input file is missing, the program raises a clear `FileNotFoundError` with the missing path name instead of crashing without explanation.

## Final Output
The project writes a dated report in the `reports/` directory containing:
- source file name
- summary of accepted and flagged records
- operational statistics
- list of all rejected lines with reasons

## Final Project Statement
This project builds a resilient data layer for village water-pump telemetry. It reads daily pump logs, validates voltage and current values, rejects malformed entries without silently losing records, and generates a maintenance report for field technicians who need a reliable view of pump condition.
