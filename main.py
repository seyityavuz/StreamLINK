import subprocess
import sys
import time

def get_m3u8(url, quality="best"):
    try:
        # streamlink --stream-url <url> <quality>
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
    if len(sys.argv) < 2:
        print("Kullanım: python main.py <yayın-url> [kalite]")
        sys.exit(1)

    url = sys.argv[1]
    quality = sys.argv[2] if len(sys.argv) > 2 else "best"

    while True:
        m3u8 = get_m3u8(url, quality)
        if m3u8:
            print(f"[{time.strftime('%H:%M:%S')}] Güncel m3u8: {m3u8}")
        else:
            print("Link alınamadı.")
        time.sleep(60)  # 60 saniyede bir yenile

if __name__ == "__main__":
    main()
