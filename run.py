"""
MediGrowth AI - 1-Click Launch Script
Launches the Flask application and opens the local browser dashboard.
"""

import sys
import webbrowser
import threading
import time
from app import app

def open_browser():
    """Wait for server initialization then open browser."""
    time.sleep(1.2)
    url = "http://127.0.0.1:5000"
    print(f"\n[MediGrowth AI] Opening local dashboard at {url} ...\n")
    webbrowser.open(url)

if __name__ == "__main__":
    print("=" * 75)
    print("  🚀 MEDIGROWTH AI - AUSTRALIAN HEALTHCARE INTELLIGENCE & OUTBOUND ENGINE")
    print("  Practical Assessment Project: AI Growth & Automation Associate")
    print("=" * 75)
    print("\n[+] Starting background browser launcher...")
    threading.Thread(target=open_browser, daemon=True).start()
    print("[+] Starting Web Application Server on http://127.0.0.1:5000 (Ctrl+C to stop)...")
    app.run(host="127.0.0.1", port=5000, debug=False)
