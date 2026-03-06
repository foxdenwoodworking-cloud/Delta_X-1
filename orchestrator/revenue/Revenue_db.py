from RevenueDB import get_conn

def rollup_species():
    conn = get_conn()
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO revenue_rollups (species, total_amount, currency, as_of)
            SELECT species, SUM(amount), 'USD', datetime('now')
            FROM revenue_events
            GROUP BY species
        """)
        conn.commit()
    finally:
        conn.close()
