

""" This program creates a directory to store the archived data of a retired application.
It prompts for the application name and a 4 digit ID then creates the directory using those details in the correct format"""

import os
import sys 
import re
import datetime

# print('Correct Format' if re.match(r'[A-Z][a-z]{2}[0-9]{3}', u_id) else 'Wrong Format')
# if re.match(r'[A-Z][a-z]{2}[0-9]{3}', path) 


def create_dir():

	arch_app=input("ENTER the name of the APP to be ARCHIVED using underscores for spaces \n Eg. app_to_archive : ")
	# print(arch_app)

	if arch_app == "":

		print ("You must enter an APPLICATION NAME, try again ")
		create_dir()

	else:		

		arch_id=input("Enter the 4 digit ID of the application to be archived : ")
		# print(arch_id)	

		# path=sys.argv[1]
		# print(path)
		access_rights = 0o700
		# path='2020-'+arch_app+'_'+arch_app+'-'+arch_id+''
		now = datetime.datetime.now()
		cyear=str(now.year)

		#for i in range(16):
		
		path=''+cyear+'-'+arch_app+'-'+arch_id+''
		path1=''+cyear+'-'+arch_app+'-'+arch_id+'/Chain_of_Custody/source_checksums'
		path2=''+cyear+'-'+arch_app+'-'+arch_id+'/Chain_of_Custody/dest_checksums'
		path3=''+cyear+'-'+arch_app+'-'+arch_id+'/Chain_of_Custody/ease_checksums'
		path4=''+cyear+'-'+arch_app+'-'+arch_id+'/Data'
		path5=''+cyear+'-'+arch_app+'-'+arch_id+'/year_1'
		path6=''+cyear+'-'+arch_app+'-'+arch_id+'/year_2'
		path7=''+cyear+'-'+arch_app+'-'+arch_id+'/year_3'
		path8=''+cyear+'-'+arch_app+'-'+arch_id+'/year_4'
		path9=''+cyear+'-'+arch_app+'-'+arch_id+'/year_5'
		path10=''+cyear+'-'+arch_app+'-'+arch_id+'/year_6'
		path11=''+cyear+'-'+arch_app+'-'+arch_id+'/year_7'
		path12=''+cyear+'-'+arch_app+'-'+arch_id+'/year_8'
		path13=''+cyear+'-'+arch_app+'-'+arch_id+'/year_9'
		path14=''+cyear+'-'+arch_app+'-'+arch_id+'/year_10'
		path15=''+cyear+'-'+arch_app+'-'+arch_id+'/Documentation'
		path16=''+cyear+'-'+arch_app+'-'+arch_id+'/EASE_Cores'


		# if arch_app != "":

		if re.match(r'([1-3][0-9]{3}-.*-[0-9])', path):

			try:
				os.makedirs(path, access_rights, exist_ok=True)
				os.makedirs(path1, access_rights, exist_ok=True)
				os.makedirs(path2, access_rights, exist_ok=True)
				os.makedirs(path3, access_rights, exist_ok=True)
				os.makedirs(path4, access_rights, exist_ok=True)
				os.makedirs(path5, access_rights, exist_ok=True)
				os.makedirs(path6, access_rights, exist_ok=True)
				os.makedirs(path7, access_rights, exist_ok=True)
				os.makedirs(path8, access_rights, exist_ok=True)
				os.makedirs(path9, access_rights, exist_ok=True)
				os.makedirs(path10, access_rights, exist_ok=True)
				os.makedirs(path11, access_rights, exist_ok=True)
				os.makedirs(path12, access_rights, exist_ok=True)
				os.makedirs(path13, access_rights, exist_ok=True)
				os.makedirs(path14, access_rights, exist_ok=True)
				os.makedirs(path15, access_rights, exist_ok=True)
				os.makedirs(path16, access_rights, exist_ok=True)
			except OSError:
				print ("Creation of the directory %s failed" % path)

		else:
		    # print ("Creation of the directory %s failed" % path)
			print ("Incorrect format; %s, try again " % path)
			create_dir()

""" def rem_dir()

try:
    os.rmdir(path)
except OSError:
    print ("Deletion of the directory %s failed" % path)
else:
    print ("Successfully deleted the directory %s" % path)	    

"""    

if __name__ == '__main__':   
	create_dir()

# if not os.path.exists(path, exist_ok=True):


