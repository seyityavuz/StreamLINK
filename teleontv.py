import subprocess
import time
import os

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

def main():
    url = "https://kick.com/teleontv"
    quality = "best"

    while True:
        m3u8 = get_m3u8(url, quality)
        if m3u8:
            print(f"[{time.strftime('%H:%M:%S')}] Güncel m3u8: {m3u8}")
            # m3u8 linkini dosyaya yaz
            with open("current_url.txt", "w", encoding="utf-8") as f:
                f.write(m3u8 + "\n")

            # Git komutları ile GitHub’a push et
            os.system("git add current_url.txt")
            os.system(f'git commit -m "Update m3u8 {time.strftime("%Y-%m-%d %H:%M:%S")}"')
            os.system("git push origin main")
        else:
            print("Link alınamadı.")
        time.sleep(60)  # 60 saniyede bir yenile

if __name__ == "__main__":
    main()
