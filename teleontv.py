import subprocess
from datetime import datetime, timezone
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

if name == "main":
    if OUTDIR.exists() and not OUTDIR.is_dir():
        OUT_DIR.unlink()
    OUTDIR.mkdir(parents=True, existok=True)

    m3u8 = get_m3u8(URL, QUALITY)
    if m3u8:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

        # Zaman damgalı dosya
        filets = OUTDIR / f"teleontv-{ts}.txt"
        filets.writetext(m3u8 + "\n", encoding="utf-8")
        print("Yeni dosya:", file_ts)

        # Son güncel link
        latest = OUT_DIR / "latest.txt"
        latest.write_text(m3u8 + "\n", encoding="utf-8")
        print("latest.txt güncellendi.")
    else:
        print("Link alınamadı.")
