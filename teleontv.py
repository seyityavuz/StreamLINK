python
import subprocess
from datetime import datetime, timezone
from pathlib import Path

Ayarlar
URL = "https://kick.com/teleontv"
QUALITY = "best"
OUT_DIR = Path("linkler")
LISTFILE = OUTDIR / "m3u8_listesi.txt"
M3UFILE = OUTDIR / "m3u_dosyasi.txt"

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
    # Klasör kontrolü
    if OUTDIR.exists() and not OUTDIR.is_dir():
        OUT_DIR.unlink()
    OUTDIR.mkdir(parents=True, existok=True)

    # M3U8 linkini al
    m3u8 = get_m3u8(URL, QUALITY)
    if m3u8:
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        entry = f"# {ts} - {URL}\n{m3u8}\n\n"

        # Liste dosyasına ekle
        with LIST_FILE.open("a", encoding="utf-8") as f:
            f.write(entry)
        print("Yeni M3U8 eklendi:", LIST_FILE)

        # Televizo uyumlu M3U dosyasına ekle
        with M3U_FILE.open("a", encoding="utf-8") as f:
            f.write(f"#EXTINF:-1,TeleonTV ({ts})\n{m3u8}\n\n")
        print("Televizo için M3U dosyası güncellendi:", M3U_FILE)
    else:
        print("Link alınamadı.")
