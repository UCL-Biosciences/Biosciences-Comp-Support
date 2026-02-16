
import requests
import datetime
import os

tenant = os.environ["GRAPH_TENANT_ID"]
client = os.environ["GRAPH_CLIENT_ID"]
secret = os.environ["GRAPH_CLIENT_SECRET"]
calendar_id = os.environ["CALENDAR_ID"]

# 1. Get OAuth token
token_url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
data = {
    "client_id": client,
    "client_secret": secret,
    "scope": "https://graph.microsoft.com/.default",
    "grant_type": "client_credentials",
}
token_response = requests.post(token_url, data=data).json()
print(token_response)  # DEBUG

token = token_response["access_token"]
headers = {"Authorization": f"Bearer {token}"}

# 2. Get events for next 30 days
endpoint = (
    f"https://graph.microsoft.com/v1.0/users/{calendar_id}/events"
    "?$filter=categories/any(c:c eq 'Drop-In')"
    "&$select=subject,start,end,location,categories"
)

events = requests.get(endpoint, headers=headers).json().get("value", [])

# 3. Generate Markdown
lines = ["# Drop‑in Times\n", "Updated automatically from my Outlook calendar.\n"]

for e in events:
    subject = e["subject"]
    start = e["start"]["dateTime"]
    end = e["end"]["dateTime"]
    location = e["location"]["displayName"] or "TBA"

    lines.append(f"### **{subject}**")
    lines.append(f"- 🗓️ {start} → {end}")
    lines.append(f"- 📍 {location}\n")

with open("DROPINS.md", "w") as f:
    f.write("\n".join(lines))
