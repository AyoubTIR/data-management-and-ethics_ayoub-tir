"""CTP 2 - Exercise 1 STARTER: profile customers.csv with pandas.
Run from the 02_CTP2 folder:  python profile_customers_starter.py
Goal: measure at least 8 rules (2 per dimension) and copy the numbers into quality_scorecard_template.csv
"""
import pandas as pd

df = pd.read_csv("../shopfast-kit/data/customers.csv", dtype=str)   # dtype=str: keep the raw text (e.g. 01300)
n = len(df)
print("Rows:", n)
print(df.head())

# --- Completeness: how many empty values per column? ---
print("\nEmpty values per column:\n", df.isna().sum())

# --- Uniqueness: is customer_id unique? ---
print("\nDuplicated customer_id rows:", df["customer_id"].duplicated(keep=False).sum())

# TODO 1 (Uniqueness): normalise email (strip + lower case) and count people registered twice

email_norm = df["email"].str.strip().str.lower()

counts = email_norm.dropna().value_counts()


people_registered_twice = (counts > 1).sum()
print(f"People registered twice : {people_registered_twice}")


# TODO 2 (Validity): count emails that do not match the regex  ^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$   (hint: .str.match)

pattern = r"^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$"
emails = email_norm.dropna()
invalid = ~emails.str.match(pattern)
print("\nInvalid emails:", invalid.sum())
print(emails[invalid].head(10))

# TODO 3 (Consistency): list the distinct values of country with value_counts() - how many spellings for 4 countries?

print("Country values:\n", df["country"].value_counts(dropna=False))
print("Distinct spellings:", df["country"].nunique())

valid_country_code_formats = ["FR", "DE", "ES", "BE"]

bad_country = df["country"].notna() & ~df["country"].isin(valid_country_code_formats)
print("Non-standard country values:", bad_country.sum())

# TODO 4 (Consistency): count signup_date values that are NOT in the format YYYY-MM-DD

bad_signup = ~df["signup_date"].str.match(r"^\d{4}-\d{2}-\d{2}$")
print("signup_date not ISO:", bad_signup.sum())
print(df.loc[bad_signup, "signup_date"].head(10))

# TODO 5 (Validity): loyalty_tier values outside bronze / silver / gold / platinum

print("loyalty_tier values:\n", df["loyalty_tier"].value_counts(dropna=False))

allowed_tiers = ["bronze", "silver", "gold", "platinum"]

bad_tier = ~df["loyalty_tier"].isin(allowed_tiers)
print("Invalid loyalty_tier (raw):", bad_tier.sum())

bad_tier_norm = ~df["loyalty_tier"].str.strip().str.lower().isin(allowed_tiers)
print("Invalid loyalty_tier (after strip+lower):", bad_tier_norm.sum())

# TODO 6 (Accuracy): birth dates in the future or before 1906 (convert the ISO ones with pd.to_datetime)

birth = pd.to_datetime(df["birth_date"], format="%Y-%m-%d", errors="coerce")
print("\nISO birth dates checked:", birth.notna().sum())

bad_birth = (birth > pd.Timestamp.today()) | (birth < pd.Timestamp("1906-01-01"))
print("Implausible birth dates:", bad_birth.sum())
print(df.loc[bad_birth, "birth_date"])


# TODO 7 (Validity): French postal codes that do not have 5 digits

country_norm = df["country"].str.strip().str.lower()

is_fr = country_norm.isin(["fr", "france", "fra"])
bad_pc = is_fr & ~df["postal_code"].str.strip().str.match(r"^\d{5}$")

print("French customers:", is_fr.sum())
print("French postal codes without 5 digits:", bad_pc.sum())
print(df.loc[bad_pc, "postal_code"].head(10))

# Bonus: compute score_pct = 100 * (1 - failing_rows / n) for each rule
