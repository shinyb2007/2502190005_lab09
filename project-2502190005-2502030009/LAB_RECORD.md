# Lab 09 Record

## Brief
Rural drinking-water pumps fail when field technicians miss abnormal voltage spikes and sustained overcurrent. This project helps Panchayat Water Technicians quickly ingest daily telemetry, reject bad records, and produce a maintenance summary without silently losing data.

## User
Panchayat Water Technicians working in village maintenance teams who review pump health from daily paper/text logs.

## Function Signatures
```python
import re, os

RECORD = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2})\|(?P<pump_id>PUMP-\d{2})\|(?P<voltage>\d+)\|(?P<current>\d+(?:\.\d+)?)\|(?P<status>[A-Z]+)$")

def parse_record(line: str) -> dict:
    """One raw line -> a dict of fields. Raises ValueError if malformed."""


def load(path: str) -> tuple[list[dict], list[tuple[int, str, str]]]:
    """Read a file -> (records, problems)."""


def summarise(records: list[dict]) -> dict:
    """records -> a dict of the numbers the report needs."""
```

## Decision on the Third Imperfect Line
The third imperfect line is the out-of-range voltage record:
`2026-10-05|PUMP-01|440|13.8|OK`
This is well-formed syntax but physically impossible, so it is rejected as a bad telemetry value. The stray spaces line is cleaned with `strip()` and accepted, while the missing-field line is rejected as malformed.

## Stranger Test Result
A stranger can open the README and run the project from there alone. The program reads `data/sample.txt`, processes valid records, and writes a report in `reports/`. If a bad line is added to the sample file, it is reported in the problems section instead of crashing or being silently accepted. If the input file is missing, the program raises a clear `FileNotFoundError` message naming the missing path.

## Final Output
The project writes a dated report in the `reports/` directory with the source file, operational summary, and skipped-line audit.
