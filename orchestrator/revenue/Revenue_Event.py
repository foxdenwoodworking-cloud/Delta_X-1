from RevenueQueue import enqueue_revenue_event

def ingest_revenue(species, job_id, amount, currency="USD"):
    event = {
        "species": species,
        "job_id": job_id,
        "amount": amount,
        "currency": currency,
    }
    enqueue_revenue_event(event)
EOPY
