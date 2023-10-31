# Download-Videos-with-yt_dlp

Is a Python script to download YouTube videos using the yt_dlp library (a fork of youtube-dl). Next, I explain how it works:

    import yt_dlp

In this line, you import the yt_dlp library, which allows you to download videos from YouTube and other similar sites.

URL entry:

    url = input()

This line allows the user to enter the URL of the YouTube video they want to download. User input is saved in the url variable.

Download options settings:

    download_directory = 'Path of download'
    ydl_opts = {
     'outtmpl' : f'{download_directory}/%(title)s.%(ext)s',
     'format': 'best'
    }

In these lines, you define the download options. 'outtmpl' specifies the file naming pattern for downloaded files. '%(title)s.%(ext)s' means that the file name will be generated with the video title and its extension. 'format' is set to 'best', which means the best quality available will be downloaded.

Video download:

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
         ydl.download([url])

Here, you create an instance of YoutubeDL with the download options set to ydl_opts. Then, you use the download([url]) method to download the video whose URL the user entered.

Completion message:

     print("download complete")

After the video download is complete, you print "download complete" to the console to indicate that the download is complete.

It is important to note that this script requires the yt_dlp library to be installed in your Python environment to work correctly. Also, make sure to provide a valid download path in the download_directory variable. Also, there is a small error in the original code: '%(tittle)s' needs to be corrected to '%(title)s' to get the correct video title.
