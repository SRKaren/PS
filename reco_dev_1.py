from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
from dejavu.testing import get_length_audio
import warnings
import json
import os, fnmatch
warnings.filterwarnings("ignore")

# load config from a JSON file (or anything outputting a python dictionary)
# with open("dejavu.cnf.SAMPLE") as f:
#configrura la base de datos
config = {
	"database": {
	"host": "127.0.0.1",
	"user": "root",
	"passwd": "ksilva", 
	"db": "dejavu2"
	}
}

# create a Dejavu instance
djv = Dejavu(config)

# Fingerprint all the mp3's in the directory we give it/configura el directorio donde estaran alojadas las firmas
# la firma de pistas se eejcutara con firmarDejavu.py de forma separada

# reconocer archivos de una carpeta para hacer el reconocimiento de pistas de un directorio
def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

# gather files to fingerprint /configura el directorio donde estaran alojadas las pistas a comparar
# UNLABELED_AUDIO_DIR = "./lockon/"
UNLABELED_AUDIO_DIR = "/home/nego/Escritorio/mp3/"
PATTERN = "*.mp3"
audio_paths = find_files(UNLABELED_AUDIO_DIR, PATTERN)

# recognize them one at a time
original_file_to_song = {}
for path in audio_paths:
    print "Attempting to recognize %s..." % path
    song = djv.recognize(FileRecognizer, path)
    original_file_to_song[path] = song

#print "Audio file at: %s was recognized as %s" % (path, song)
# see the songs you've recognized
for path, song in original_file_to_song.iteritems():
    print "Audio file at: %s was recognized as %s \n" % (path, song)

#resultado para reporte
cadenaReporte='Pista objetivo, Firma Identificada, Id de pista, Confianza, Inicio de firma, Alineacion \n'

# path es la llave del diccionario en original_file... cuyo valor corresponde al nombre de la cancion escaneada, y song es el valor de la llave del mismo diccionario cuyo valor corresponde al resultado del reconocimiento 
for objetivo,result in original_file_to_song.iteritems():
	
	# pista objetivo
	songObj='pista objetivo %s' % objetivo
	
	#firma identificada
	songIdent='cancion reconocida %s' % result['song_name']
	
	#caneda de resultado de la comparacion
	cadena=''
	
	#bandera de comprobacion de coincidencia de firma
	comprobacion=False
	for key in result:
		if key=='song_id':
			# print 'id cancion %s' % result[key]
			cadena+=str(result[key])+','
		elif key=='confidence':
			confidenceR=result[key]
			# los resultados cuyo nivel de confianza sea mayor al valor dado son validos para revision
			# if result[key]>10:
			# 	comprobacion=True
			# else:
			# 	comprobacion=False
			# print 'confianza de camparacion %s'%result[key]
			cadena+=str(result[key])+','
		elif key=='offset_seconds':
			offset_secondsR=result[key]
			# print 'ubicacion de la firma en la pista %s' % result[key]
			# if result[key]<0.0:
			# 	# si los offset_seconds tienen un valo negativo se ignora la pista
			# 	comprobacion=False
			# else:
			# 	comprobacion=True
			cadena+=str(result[key])+','
		elif key=='offset':
			offsetR=result[key]
			# if result[key]<100:
			# 	comprobacion=True
			# else:
			# 	comprobacion=False
			# print 'alineacion hash %s' % result[key]
			cadena+=str(result[key])+','
    	# print song[key]
    	if confidenceR >0:
	    	if offset_secondsR>=0.0:
	    		if offsetR >=0.0:
	    			comprobacion=True
	    		else:
	    			comprobacion=False
	    	else:
	    		comprobacion=False
		# imprimir resultado
    	if comprobacion==True:
    		print '%s %s resultado: %s \n' % (songObj,songIdent,cadena)
    		cadenaReporte+='%s %s %s \n' % (songObj,songIdent,cadena)



f = open('./logs/reportes/reporte.csv','wb')
f.write(cadenaReporte)
f.close()

# ciclo generar csv texto
# for(var i=0;i < resultados.length; i++){
#     	Ti.API.info('encuesta '+(i)+': '+JSON.stringify(resultados[i]));
#     	Ti.API.info('inner2 primer loop: '+(resultados[i].resultados).length);
#         for(var j = 0; j < (resultados[i].resultados).length; j++){
#             rowTxt += '"' + resultados[i].resultados[j] + '"';
  			
#             if(j < ((resultados[i].resultados).length)-1)
#             {
#                 rowTxt += ',';
#             }
#         }
#       rowTxt += '\n';
#     }
#     Ti.API.info('gr: '+rowTxt);
