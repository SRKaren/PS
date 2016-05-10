from dejavu import Dejavu
from dejavu.testing import*
from dejavu.recognize import FileRecognizer
import warnings
import json
import os, fnmatch
import argparse
import sys
warnings.filterwarnings("ignore")

# load config from a JSON file (or anything outputting a python dictionary)
#with open("dejavu.cnf.SAMPLE") as f:

#Directorio de firmas
audiopath= "/home/nego/Descargas/firma"
extension= ".mp3"
audio_paths = get_files_recursive(audiopath, extension)

#Obtener longitud de pistas
for path in audio_paths:
    print "Path %s" % path
    n = get_length_audio(path, extension)
    print "Length %s "%(n)
    config={
    "database": {
    "host": "127.0.0.1",
    "user": "root",
    "passwd": "ksilva",
    "db": "dejavu3"
    },
    "fingerprint_limit": [n]
    }
    # create a Dejavu instance
    djv = Dejavu(config)
    djv.fingerprint_file(path)

#djv.fingerprint_directory(audiopath, [extension])
#Comandos

#print len(sys.argv)
#print str(sys.arv)
