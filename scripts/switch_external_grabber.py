#!/usr/bin/python -OO

#
# remote.xml in the config folder defines a custom action to run this script on "green"  button
#

import os
import time 



configfile = "/home/pi/config/hyperion.config.json"
tmpfile = "/tmp/config"


c = open( configfile, "r" )
t = open( tmpfile, "w" )

writelines=True
v4lblock=False

for line in c:
	if "ambipi_grabber_start" in line:
		writelines=False
		if "framegrabber" in line:
			v4lblock=True


	if(writelines):
		t.write(line)


        if "ambipi_grabber_stop" in line:
                writelines=True
		if(v4lblock):
			print "generating v4lblock"
			t.write('\
			//ambipi_grabber_start v4l\n\
			"grabber-v4l2" :\n\
        		{\n\
                		"device" : "/dev/video0",\n\
                		"input" : 0,\n\
                		"width" : 300,\n\
                		"height" : 200,\n\
                		"frameDecimation" : 2,\n\
               			 "sizeDecimation" : 8,\n\
		                "priority" : 1100,\n\
             		   	"mode" : "2D",\n\
                		"cropLeft" : 1,\n\
     			        "cropRight" : 1,\n\
                		"cropTop" : 1,\n\
                		"cropBottom" : 1,\n\
                		"redSignalThreshold" : 0.1,\n\
                		"greenSignalThreshold" : 0.1,\n\
                		"blueSignalThreshold" : 0.1\n\
        		},\n\
			//ambipi_grabber_stop\n\
			')
		else:
			print "generating framegrabber block"
                        t.write('\n\
                        //ambipi_grabber_start framegrabber\n\
        		"framegrabber" :\n\
        		{\n\
                		"width" : 64,\n\
                		"height" : 64,\n\
                		"frequency_Hz" : 10.0\n\
        		},\n\
                        //ambipi_grabber_stop\n\
                        ')
			



c.close()
t.close;

os.unlink(configfile)
os.rename(tmpfile,configfile);

os.system("sudo service hyperion stop")
os.system("sudo service hyperion start") 
	
