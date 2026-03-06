   
EOPY

echo "5) Writing RevenueMetrics.py..."
cat > "$ROOT_DIR/RevenueMetrics.py" << 'EOPY'
from RevenueDB import get_conn

def get_metrics():
    conn = get_conn()
    try:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*), COALESCE(SUM(amount), 0) FROM revenue_events")
        count, total = cur.fetchone()
        return {
            "revenue_events_total": count,
            "revenue_amount_total": total,
        }
    finally:
        conn.close()
EOPY





EOPY
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

echo "7) Writing RevenueServer.py..."
cat > "$ROOT_DIR/RevenueServer.py" << 'EOPY'
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from RevenueIngest import ingest_revenue
from RevenueMetrics import get_metrics
from RevenueDB import init_db
from threading import Thread
from RevenueRetry import retry_loop

HOST = "0.0.0.0"
PORT = 8000



lass RevenueHandler(BaseHTTPRequestHandler):
    def _json_response(self, code, payload):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_POST(self):
        if self.path == "/revenue":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body.decode())
                ingest_revenue(
                    species=data.get("species"),
                    job_id=data.get("job_id"),
                    amount=data.get("amount"),
                    currency=data.get("currency", "USD"),
                )
                self._json_response(200, {"status": "ok"})
            except Exception as e:
                self._json_response(400, {"status": "error", "error": str(e)})
        else:
            self._json_response(404, {"status": "not_found"})

    def do_GET(self):
        if self.path == "/metrics":
            metrics = get_metrics()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            lines = [
                f"revenue_events_total {metrics['revenue_events_total']}",
                f"revenue_amount_total {metrics['revenue_amount_total']}",
            ]
            self.wfile.write(("\n".join(lines) + "\n").encode())
        else:
            self._json_response(404, {"status": "not_found"})

def start_retry_loop():
    t = Thread(target=retry_loop, daemon=True)
    t.start()

if __name__ == "__main__":
    init_db()
    start_retry_loop()
    server = HTTPServer((HOST, PORT), RevenueHandler)
EOPY
    print(f"[RevenueServer] Listening on {HOST}:{PORT}")
    server.serve_forever()
