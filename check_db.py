from app.db import get_cursor

with get_cursor(dict_rows=False) as c:
    c.execute("UPDATE users SET email_verified = TRUE WHERE email = %s",
              ("psaikrishnan7@gmail.com",))
print("verified")