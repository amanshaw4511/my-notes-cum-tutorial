
# docx to anything

    libreoffice --headless --convert-to out.pdf input.docx



# video and audio 
    ## audio
    ffmpeg -i input.mp3 output.ogg

    ## video
    ffmpeg -i input.webm output.mp4


# html pdf txt
    
    pandoc -f markdown -t html hello.md -o hello.html

     -f   : from format
     -t   : to format
     -o   : output file




