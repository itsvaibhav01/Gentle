# Gentle -  a movie subtitle alignment tool using deep learning application gentle
---
<b> http://lowerquality.com/gentle/ </b>

### Fast run 
---
There are 3 files to process under align.py file <br>
1. Need to give movie name after -m arg along with the extenstion like **-m movie.mkv**
2. Need to give the subtitle file with -s arg like **-s movie_subtitle.srt** 
3. It is optional to give name of final adjusted subtitle file a name, by default it gives **new subtitles.srt**. If needed we can name it with **-o file_name_here.srt**
---
<i>A simple running example is like this:</i>

~~~bash
python3 align.py -m example_name.mkv -s subtitle.srt -o output.srt
~~~
---

### Installation
1. Get the dockercontainer of Gentle and keep it running (instructions inside gentle folder)
2. Install all resources by installing resources.

---

### License & Copyright 

Licensed under the [MIT License](LICENSE).
