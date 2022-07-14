from pytube import Playlist
playlist = Playlist('Set PlayList URL Here')
# DOWNLOAD_DIR = 'D:\Downloads'
print(f'Downloading: {playlist.title}')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

for video in playlist.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download()
    # video.streams.first().download()
