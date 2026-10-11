from app.db import get_cursor
from app import billing

with get_cursor(dict_rows=False) as cur:
    cur.execute("SELECT id, credit_balance FROM api_customers")
    customers = cur.fetchall()

for cid, bal in customers:
    new = billing.grant_credits(cid, 50, reason="manual_test")
    print(f"{cid}: {bal} -> {new}")