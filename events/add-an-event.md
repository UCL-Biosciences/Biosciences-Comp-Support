# Add an event
1. Copy `events/template.yaml` to `events/YYYY-MM-DD-short-title.yaml`.
2. Fill in the required fields.
4. Open a pull request. Maintainers will merge and the table in the README will update automatically.

## Naming rules
- File name must start with the event date: `YYYY-MM-DD`.
- Use lowercase and hyphens only.

## Field notes
- `start` and `end` use 24-hour time, e.g. `2025-11-15 12:30`.
- `timezone` must be an IANA zone like `Europe/London`.
- `summary` supports basic Markdown.
