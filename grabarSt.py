from crontab import CronTab
import os
import time

url= raw_input("Introduce la url del stream a grabar: ")
horai= int(input("Ingresa la hora de inicio de grabacion: "))
horat=int(input("Ingresa la hora de termino de grabacion: "))

h=time.strftime("%H%M")
date=time.strftime("%y-%m-%d")
output_filename= '%s-%s' %(date,h)

duration=60

output_dir='~/dejavu/mp3/%s' %(url)

#comando= '*/1 %s-%s * * * streamripper %s -d %s -l %s -a %s -u FreeAmp/2.x -o always' % (horai,horat,url,output_dir,duration, output_filename)

#print horai

cmd= 'streamripper %s -d %s -l %s -a %s -u FreeAmp/2.x -o always' % (url,output_dir,duration, output_filename)


tab = CronTab(user='nego')
cron_job =tab.new(cmd)
cron_job.minute.every(1)
cron_job.hour.during(horai, horat)
tab.write()
print tab.render()
