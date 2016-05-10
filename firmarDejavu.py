from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
from dejavu.testing import get_length_audio
import warnings
import json
import os, fnmatch,sys
warnings.filterwarnings("ignore")

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

# def generaFirmas(directory,extension,nameDB):

# directorio de busqueda
# UNLABELED_AUDIO_DIR = "./examples/firmas-ChryslerAds/"
UNLABELED_AUDIO_DIR = "./firmas/"
# extension base de los archivos objetivo puede ser *.mp3  o *.wav
PATTERN = "*.MP3"
#extension para 
# EXTENSION='mp3'
audio_paths = find_files(UNLABELED_AUDIO_DIR, PATTERN)

original_file = []
for path in audio_paths:
    print "for fingerprinting %s..." % path
    original_file.append(path)
print original_file

for x in original_file:
	limittime=get_length_audio(x,'.mp3')
	print limittime
	config = {
	"database": {
	"host": "127.0.0.1",
	"user": "root",
	"passwd": "ksilva", 
	"db": "dejavu"
	},
	"database_type" : "mysql",
	"fingerprint_limit":limittime
	}
	djv = Dejavu(config)
	print 'x'+x
	djv.fingerprint_file(x)

# 
# if __name__=__main__:
# 	if len(sys.argv)<4:



# if __name__ == '__main__': 
#     if len(sys.argv) != 3: 
#         print "La cantidad de argumentos ingresada no es correcta" 
#     file = sys.argv[1] 
#     action = sys.argv[2] 
#     if action == '-c': 
#         print check(file) 
#     elif action == '-h': 
#         hide(file) 
#         print "El archivo se encuentra oculto" 
#     elif action == '-s': 
#         show(file) 
#         print "El archivo ya no se encuentra oculto" 
#     else: 
#         print "El argumento ingresado no es correcto" 


