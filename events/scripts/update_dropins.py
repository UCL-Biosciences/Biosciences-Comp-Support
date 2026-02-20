import re
from datetime import datetime
from pathlib import Path
import pandas as pd

EVENTS_FILE = Path("events/dropin.md")
README_FILE = Path("README.md")

START_TAG = "<!-- NEXT_EVENTS_START -->"
END_TAG = "<!-- NEXT_EVENTS_END -->"


def extract_events_table(md_text):
    """
    Extracts the first markdown table from the file and returns a DataFrame.
    """
    lines = md_text.splitlines()
    table_lines = []

    in_table = False
    for line in lines:
        if "|" in line:
            in_table = True
            table_lines.append(line)
        elif in_table:
            break

    df = pd.read_csv(
        pd.io.common.StringIO("\n".join(table_lines)),
        sep="|",
        engine="python",
        skipinitialspace=True
    )

    # The first and last columns from pipes become empty — drop them
    df = df.drop(columns=[col for col in df.columns if col.strip() == ""])

    return df


def main():
    # Load events
    md_text = EVENTS_FILE.read_text()
    df = extract_events_table(md_text)
    
    # Drop empty columns created by leading/trailing pipes
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
    
    # Normalize header names by stripping whitespace
    df.columns = df.columns.str.strip()
    
    # Drop the markdown alignment/separator row (------ etc.)
    if (df.iloc[0].astype(str).str.fullmatch(r"-+").all()):
        df = df.iloc[1:].reset_index(drop=True)
    
    # Also strip whitespace from all cells
    df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))

    print("=== DEBUG: Columns found in events table ===")
    print(df.columns.tolist())
    
    print("=== DEBUG: First few rows ===")
    print(df.head().to_string())


    # Parse dates
    df["parsed_date"] = df["Date"].apply(
        lambda d: datetime.strptime(d.strip(), "%a, %d %b %Y")
    )

    # Filter future events
    now = datetime.utcnow()
    df_future = df[df["parsed_date"] > now].sort_values("parsed_date")

    # Get next 3 events
    next_three = df_future.head(3)

    # Build markdown list
    events_md = "\n".join(
        f"- **{row['Date']}** — {row['Time']} — {row['Location']} — {row['Title']}"
        for _, row in next_three.iterrows()
    )

    # Update README
    readme = README_FILE.read_text()

    new_content = re.sub(
        f"{START_TAG}.*?{END_TAG}",
        f"{START_TAG}\n{events_md}\n{END_TAG}",
        readme,
        flags=re.DOTALL
    )

    README_FILE.write_text(new_content)
    print("README updated with next three events.")


if __name__ == "__main__":
    main()
