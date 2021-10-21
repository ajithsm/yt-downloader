from pytube import YouTube
urlIP=input('Enter URL:')
video_list = [urlIP]
#video_list = [ "https://www.youtube.com/watch?v=XHq3ZBZHznE&list=RDddaObxkRQH0&index=6" ]

for i in video_list:
    try:
        yt = YouTube(i)
        print( "Downloading the link :" +i )
        print( "Downloading the video :" +yt.streams[0].title )
    except:
        print("Connection error")

    stream = yt.streams.filter(res="720p" ).first()
    stream.download(output_path="Downloads/")
print("Task Completed")

