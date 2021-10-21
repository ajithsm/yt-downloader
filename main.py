from pytube import YouTube
video_list = [https://www.youtube.com/watch?v=ddaObxkRQH0]

for i in video_list:
    try:
        yt = YouTube(i)
        print("Downloading the link :" +i)
        print("Downloading the video :" +yt.streams[0].title)
    except:
        print("Connection error")
    stream = yt.streams.filter(res="144p").first()
    stream.download("Downloads/")
print("Task Completed")
