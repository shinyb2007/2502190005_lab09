import datetime
import os
import sys

from datalayer import load, summarise


def main():
    data_path = os.path.join("data", "sample.txt")
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    try:
        records, problems = load(data_path)
    except FileNotFoundError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        sys.exit(1)

    summary = summarise(records)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    out_path = os.path.join(reports_dir, f"report_{stamp}.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("=" * 64 + "\n")
        f.write("     VILLAGE WATER-PUMP TELEMETRY & MAINTENANCE REPORT\n")
        f.write("=" * 64 + "\n")
        f.write(f"Generated On : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Source File  : {data_path}\n")
        f.write(f"Status       : {len(records)} Accepted | {len(problems)} Flagged\n")
        f.write("-" * 64 + "\n\n")

        f.write("OPERATIONAL SUMMARY\n")
        f.write("-" * 36 + "\n")
        f.write(f"{'METRIC':<24}{'VALUE':>12}\n")
        f.write("-" * 36 + "\n")
        f.write(f"{'Valid Records Read':<24}{summary['total']:>12}\n")
        f.write(f"{'Mean Voltage (V)':<24}{summary['avg_v']:>12.1f}\n")
        f.write(f"{'Mean Current (A)':<24}{summary['avg_i']:>12.2f}\n")
        f.write("-" * 36 + "\n\n")

        f.write("DATA AUDIT · SKIPPED ENTRIES & REASONS\n")
        f.write("-" * 64 + "\n")
        if problems:
            f.write(f"{'LINE':<6}{'REASON':<36}{'RAW INPUT'}\n")
            f.write("-" * 64 + "\n")
            for line_no, reason, raw in problems:
                f.write(f"{line_no:<6}{reason[:34]:<36}{raw}\n")
        else:
            f.write("None. All records conformed to schema.\n")
        f.write("=" * 64 + "\n")

    print(f"[OK] Accepted: {len(records)} | Flagged: {len(problems)}")
    print(f"[REPORT] Saved -> {out_path}")


if __name__ == "__main__":
    main()
