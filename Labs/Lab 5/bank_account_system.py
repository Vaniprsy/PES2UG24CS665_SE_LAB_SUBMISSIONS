
"""Bank account management module."""

import hashlib
import hmac
import secrets

account_data = {}


def create_account(acc_id, name, initial_deposit=0, transactions=None):
    """Create an account and optionally record its creation."""
    if acc_id in account_data:
        return False

    account_data[acc_id] = {"name": name, "balance": initial_deposit}

    if transactions is not None:
        transactions.append(
            f"Created {acc_id} with initial balance {initial_deposit}"
        )
    return True


def deposit(acc_id, amount):
    """Deposit a positive amount into an existing account."""
    if acc_id not in account_data or amount <= 0:
        return False

    account_data[acc_id]["balance"] += amount
    return True


def withdraw(acc_id, amount):
    """Withdraw money from an account if sufficient funds are available."""
    service_fee = 2.50
    if acc_id not in account_data or amount <= 0:
        return False

    total = amount + service_fee
    if account_data[acc_id]["balance"] < total:
        return False

    account_data[acc_id]["balance"] -= total
    return True


def compute_bonus(acc_id, rate=0.05):
    """Calculate a bonus using a rate between zero and one."""
    if acc_id not in account_data or not 0 <= rate <= 1:
        raise ValueError("Account must exist and rate must be between 0 and 1")

    balance = account_data[acc_id]["balance"]
    return balance * rate


def get_hash(pin, salt=None):
    """Hash a PIN with PBKDF2-HMAC-SHA256 and a random salt."""
    if salt is None:
        salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", pin.encode("utf-8"), salt, 200_000
    )
    return f"{salt.hex()}:{digest.hex()}"


def verify_pin(pin, stored_hash):
    """Verify a PIN against a salt-and-hash string."""
    try:
        salt_hex, digest_hex = stored_hash.split(":")
        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(digest_hex)
    except (ValueError, TypeError):
        return False

    actual = hashlib.pbkdf2_hmac(
        "sha256", pin.encode("utf-8"), salt, 200_000
    )
    return hmac.compare_digest(actual, expected)


def generate_temp_pin():
    """Generate a cryptographically secure four-digit temporary PIN."""
    return f"{secrets.randbelow(9000) + 1000}"


def backup_data(filename="backup.txt"):
    """Write account data to a UTF-8 text backup."""
    with open(filename, "w", encoding="utf-8") as backup_file:
        backup_file.write(str(account_data))
    print(f"Backup complete: {filename}")


def main():
    """Run a demonstration of the bank account operations."""
    create_account("A01", "Alice", 1000)
    deposit("A01", 500)
    withdraw("A01", 200)
    print("Bonus:", compute_bonus("A01"))
    pin_hash = get_hash("1234")
    print("PIN Hash:", pin_hash)
    print("PIN verified:", verify_pin("1234", pin_hash))
    print("Temp PIN:", generate_temp_pin())
    backup_data()

    # Never print or hardcode real administrator credentials here.


if __name__ == "__main__":
    main()
