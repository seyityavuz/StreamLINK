import subprocess
import time
import os

# Ayarlar
url = "https://kick.com/teleontv"
output_folder = "linkler"
output_file = "teleontvlinki.m3u"
output_path = os.path.join(output_folder, output_file)
refresh_interval = 60  # saniye

# Klasör kontrolü
if os.path.exists(output_folder):
    if not os.path.isdir(output_folder):
        os.remove(output_folder)  # Dosya varsa sil
        os.makedirs(output_folder)
else:
    os.makedirs(output_folder)

def get_stream_url():
    try:
        result = subprocess.run(
            ["streamlink", "--stream-url", url, "best"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print("Streamlink hatası:", result.stderr)
            return None
    except Exception as e:
        print("Hata:", e)
        return None

def write_m3u(stream_url):
    m3u_content = f"#EXTM3U\n#EXTINF:-1,teleontv\n{stream_url}\n"
    with open(output_path, "w") as f:
        f.write(m3u_content)
    print("Güncellendi:", stream_url)

# Ana döngü
while True:
    stream_url = get_stream_url()
    if stream_url:
        write_m3u(stream_url)
    else:
        print("Yayın alınamadı.")
    time.sleep(refresh_interval)
