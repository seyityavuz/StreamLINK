import subprocess
import time
from datetime import datetime
from pathlib import Path

URL = "https://kick.com/teleontv"
QUALITY = "best"
OUT_DIR = Path("linkler")
WRITE_HISTORY = True   # history.txt'ye ekleme açık

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

def write_files(m3u8):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    # Zaman damgalı dosya
    file_ts = OUT_DIR / f"teleontv-{ts}.txt"
    file_ts.write_text(m3u8 + "\n", encoding="utf-8")
    print("Yeni dosya:", file_ts)

    # Son güncel link
    latest = OUT_DIR / "latest.txt"
    latest.write_text(f"# UTC: {ts}\n{m3u8}\n", encoding="utf-8")
    print("Güncel dosya:", latest)

    # Geçmiş kayıt
    if WRITE_HISTORY:
        history = OUT_DIR / "history.txt"
        with history.open("a", encoding="utf-8") as f:
            f.write(f"{ts} UTC\t{m3u8}\n")

if __name__ == "__main__":
    # Bu döngü GitHub Actions içinde birkaç kez çalışacak şekilde tasarlandı.
    # Lokal kullanımda sonsuz döngüye de alabilirsin.
    iterations = 5  # 5 kez (yaklaşık 5 dakika) çalışır
    for i in range(iterations):
        m3u8 = get_m3u8(URL, QUALITY)
        if m3u8:
            write_files(m3u8)
        else:
            print("Link alınamadı.")
        time.sleep(60)
