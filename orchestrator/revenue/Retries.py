def process_event(event):
    conn = get_conn()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO revenue_events (species, job_id, amount, currency, created_at) VALUES (?, ?, ?, ?, datetime('now'))",
            (event.get("species"), event.get("job_id"), event.get("amount"), event.get("currency", "USD")),
        )
        conn.commit()
    finally:
        conn.close()

def retry_loop():
    while True:
        _, raw = r.brpop(REVENUE_QUEUE)
        payload = json.loads(raw)
        event = payload.get("event", payload)
        retries = payload.get("retries", 0)

        try:
            process_event(event)
        except Exception as e:
            retries += 1
            if retries > MAX_RETRIES:
                move_to_dead_letter(event, reason=str(e))
            else:
                backoff = min(60, 2 ** retries)
                time.sleep(backoff)
                r.lpush(REVENUE_QUEUE, json.dumps({"event": event, "retries": retries}))
EOPY
