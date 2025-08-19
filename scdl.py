import os
import yt_dlp

SC_DOWNLOAD_DIR = "scdownload"
DOWNLOAD_ARCHIVE = os.path.join(SC_DOWNLOAD_DIR, "downloaded.txt")

def download_sc(url):
    os.makedirs(SC_DOWNLOAD_DIR, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{SC_DOWNLOAD_DIR}/%(playlist_title|uploader)s/%(id)s_%(title)s.%(ext)s',
        'download_archive': DOWNLOAD_ARCHIVE,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            },
            {
                'key': 'EmbedThumbnail',
            },
        ],
        'writethumbnail': True,
        'ignoreerrors': False,
        'sleep_interval': 2,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

            if info.get('_type') == 'playlist':
                print(f"Найден плейлист: {info.get('title', 'Без названия')}")
            else:
                print(f"Найден трек: {info.get('title', 'Без названия')}")

            ydl.download([url])

        print("Готово!")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    url = input("Введите URL SoundCloud (трек или плейлист): ")
    download_sc(url)