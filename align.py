from process import inbox , clip , string_to_txt, json_to_csv, outbox, check, cleaning
import os 
import argparse

parser = argparse.ArgumentParser(description='Align your subtitles in a movie by use of Deep learning library Align.  Outputs srt')

parser.add_argument('-m', type=str, help='movie file name' , required=True)
parser.add_argument('-s', type=str, help='subtitles file name' , required=True)
parser.add_argument('-o', type=str, help='output srt file',  default = 'new subtitles.srt')


if __name__ == "__main__": 

	args = parser.parse_args()
	srt = args.s
	movie = args.m
	cut = "cut.mkv"
	audio = "audio.mp3"
	out = args.o

	text , data = inbox(srt)
	last = data[-1][0]

	clip(last, movie, cut, audio)

	string_to_txt(text)

	os.system("curl -X POST -F 'audio=@{}' -F 'transcript=<{}' 'http://localhost:32768/transcriptions?async=false' -o {}".format(audio, "out.txt", "out.json"))

	json_to_csv("out.json")

	delay = check(out = "out.csv", data = data)

	outbox(srt, new = out, delay = delay)

	cleaning()

