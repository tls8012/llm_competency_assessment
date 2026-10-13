ledger = []
cache = {}

def authorize(tenant, request_id, amount_cents, simulate_timeout=False):
    key = (tenant, request_id)
    if key in cache:
        return cache[key]
    if type(amount_cents) is not int or amount_cents <= 0:
        raise ValueError("amount")
    row = {"tenant": tenant, "request_id": request_id,
           "amount_cents": amount_cents, "auth_id": len(ledger) + 1}
    ledger.append(row)
    if simulate_timeout:
        raise TimeoutError("response path failed after commit")
    cache[key] = row
    return row
