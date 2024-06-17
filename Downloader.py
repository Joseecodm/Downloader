from pytube import YouTube

try:
    yt = input('Ingrese el link del video o canción: ')
    print('\n')
    yt = YouTube(yt)
    print("Titulo del video: ", yt.title)
    print("Autor del video: ", yt.author)
    print('\n')
    lengthVideo = int(yt.length)
    min, sec = divmod(lengthVideo, 60)
    print("Duración del video: ", "{}:{}".format(min, sec))
    yt.streams.filter(progressive=True, file_extension='.mp4').order_by('resolution').desc().first().download
    print("El video: ", yt.title, " ha sido descargado correctamente")
    
except:
    print("Hubo un error, intentelo de nuevo")
    exit()    
    