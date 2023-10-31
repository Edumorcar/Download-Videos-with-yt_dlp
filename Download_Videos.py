import yt_dlp
url = input()
download_directory = ' Path of download'

ydl_opts = {
      'outtmpl' : f'{download_directory}/%(tittle)s.%(ext)s',
      'format':'best'      

}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

print   ("download complete")