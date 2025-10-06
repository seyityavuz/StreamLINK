import subprocess
import time

URL = "https://kick.com/teleontv"
OUTPUT_PATH = "teleontvlinki.m3u"  # Sadece dosya, klasör yok

def update_m3u():
    result = subprocess.run(
        ["streamlink", "--stream-url", URL, "best"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        stream_url = result.stdout.strip()
        m3u_content = f"#EXTM3U\n#EXTINF:-1,teleontv\n{stream_url}\n"
        with open(OUTPUT_PATH, "w") as f:
            f.write(m3u_content)
        print("Güncellendi:", stream_url)
    else:
        print("Streamlink hatası:", result.stderr.strip())

# Sonsuz döngü
while True:
    update_m3u()
    time.sleep(60)
