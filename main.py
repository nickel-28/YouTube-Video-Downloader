from pytube import YouTube

 # Here I will copy the link of the video I wanna download
link = "https://www.youtube.com/watch?v=BddP6PYo2gs"
youtube_1 = YouTube(link)

videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("enter : "))
videos[strm].download()
print('Successfully')