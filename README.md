# Gentle -  a movie subtitle allignment tool using deep learning library gentle
---
<b> http://lowerquality.com/gentle/ </b>

### Fast run 
---
There are 3 files to process under align.py file <br>
1. Need to give movie name after -m arg along with the extenstion like **-m movie.mkv**
2. Need to give the subtitle file with -s arg like **-s movie_subtitle.srt** 
3. It is optional to give name of final adjusted subtitle file a name, by default it gives **new subtitles.srt**. If needed we can name it with **-o file_name_here.srt**
---

~~~bash
python align.py -m example_name.mkv -s subtitle.srt -o output.srt
~~~
