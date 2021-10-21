from pytube import YouTube
video_list = [ "https://www.youtube.com/watch?v=FC2dbAZcewo" ]

for i in video_list:
    try:
        yt = YouTube(i)
        print( "Downloading the link :" +i )
        print( "Downloading the video :" +yt.streams[0].title )
    except:
        print("Connection error")

    stream = yt.streams.filter(fps="60fps",res="720p").first()
    stream.download(output_path="Downloads/")
print("Task Completed")

