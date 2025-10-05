import subprocess
import time
from datetime import datetime
from pathlib import Path

URL = "https://kick.com/teleontv"
QUALITY = "best"
OUT_DIR = Path("linkler")

def get_m3u8(url, quality="best"):
    try:
        result = subprocess.run(
            ["streamlink", "--stream-url", url, quality],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Hata:", e.stderr)
        return None

if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    m3u8 = get_m3u8(URL, QUALITY)
    if m3u8:
        ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
        file_ts = OUT_DIR / f"teleontv-{ts}.txt"
        file_ts.write_text(m3u8 + "\n", encoding="utf-8")
        latest = OUT_DIR / "latest.txt"
        latest.write_text(m3u8 + "\n", encoding="utf-8")
        print("Dosyalar güncellendi.")
    else:
        print("Link alınamadı.")
