import yt_dlp
url_music = 'https://www.youtube.com/LFAKIR_GN'
with yt_dlp.YoutubeDL({"format": "best"}) as ydl:
    ydl.download([url_music])