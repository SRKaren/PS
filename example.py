import warnings
import json
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == '__main__':

	# create a Dejavu instance
	djv = Dejavu(config)

	# Fingerprint all the mp3's in the directory we give it
	#djv.fingerprint_directory("./firmas", [".mp3"])

	# Recognize audio from a file.
	song = djv.recognize(FileRecognizer, "/home/nego/Escritorio/mp3/2016-mie-abr-27-1807.mp3")
	print "From file we recognized: %s\n" % song

	# Or recognize audio from your microphone for `secs` seconds

