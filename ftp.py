# -*- coding: utf-8 -*-

import os, sys, re
import ftputil, ftplib
#from userRequire import userRequire

__version__ = 'Ver 0.1, Nov.04, 2014'

WELCOME_MESSAGE = 'You are connected to FTP server!'
CONNECT_ERROR   = 'Connecting Failed!' 


# E MIT-CTE CTE-MIT tested.
# C MIT-CTE CTE-MIT to be tested.

dir_group = {'AB-MIT-3-CTE' : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/MIT-CTE/35000~39999/',
	     'AB-MIT-0-CTE' : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/MIT-CTE/05000~05999/',
	     'AB-CTE-3-MIT' : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/CTE-MIT/35000~35999/',
	     'AB-CTE-0-MIT' : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/CTE-MIT/05000~05999/',
	     'AA-MIT-3-CTE' : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/MIT-CTE/35000-35999/',
	     'AA-MIT-0-CTE' : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/MIT-CTE/05001-09999/',
	     'AA-CTE-3-MIT' : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/CTE-MIT/35000-35999/',
	     'AA-CTE-0-MIT' : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/CTE-MIT/05001-06999/'
	    }


project_pattern = {'pro_ND34' :{'AB-MIT-3-CTE':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(MIT)',
			    		        're4':'(-| )?',
			    		        're5':'(3[5|6]\\d+)'
			                       },
			        'AB-CTE-3-MIT':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(CTE)',
			    		        're4':'(-| )?',
			    		        're5':'(3[5|6]\\d+)'
			                       },
			        'AB-MIT-0-CTE':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(MIT)',
			    		        're4':'(-| )?',
			    		        're5':'(05\\d+)'
			                       },
			        'AB-CTE-0-MIT':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(CTE)',
			    		        're4':'(-| )?',
			    		        're5':'(05\\d+)'
			                       }
	                       },
		 'pro_HYH34'  :{'AA-MIT-3-CTE':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(MIT)',
			    		        're4':'(-| )?',
			    		        're5':'(3[5|6]\\d+)'
					       },
		 	        'AA-CTE-3-MIT':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(CTE)',
			    		        're4':'(-| )?',
			    		        're5':'(3[5|6]\\d+)'
			                       },
			        'AA-MIT-0-CTE':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(MIT)',
			    		        're4':'(-| )?',
			    		        're5':'(05\\d+)'
			                       },
			        'AA-CTE-0-MIT':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(CTE)',
			    		        're4':'(-| )?',
			    		        're5':'(05\\d+)'
			                       }
	                       }
                  }

def basementWalk(basement_path):
	base_list_dirs = [] 
	ftp.chdir(basement_path) 
	base_list_dirs = ftp.listdir(ftp.curdir)
	return base_list_dirs

def patternGenerator(user_input):
	label          = ''
	channel_number = ''
	for project in project_pattern:
		for channel in project_pattern[project]:
			pattern = re.compile(project_pattern[project][channel]['re1']+
					     project_pattern[project][channel]['re2']+
					     project_pattern[project][channel]['re3']+
					     project_pattern[project][channel]['re4']+
					     project_pattern[project][channel]['re5'],re.IGNORECASE|re.DOTALL)
			if pattern.search(user_input):
				label = channel
				channel_number = pattern.search(user_input).group(5)

	return (label, channel_number) 

def userRequire():
	sub_path   = 'null'
	final_path = 'null'
	user_input = raw_input('May I have your channel number please?--> ')
	dir_group_label, input_channel_number = patternGenerator(user_input)
	basement_path = dir_group[dir_group_label]

	for path in basementWalk(basement_path):
		if input_channel_number in path[0:17]:
			sub_path = path
			break
	final_path = ftp.path.join(basement_path, sub_path)
	#print '%r' % final_path
	return final_path


def fileDownload(final_dirs, root_dir):
	'''
	change current dir to destinaton dir.
	and download files in the destination dir.
	'''
	download_host = ftplib.FTP(server)
	download_host.login(user, password)

	# make a dir use final_dirs in system download dir
	store_dir = storeDir()
	store_root_dir = os.path.join(store_dir, root_dir)
	os.makedirs(store_root_dir)

	for single_dir in final_dirs:
		# make a dir use single_dir in final_dirs
		download_host.cwd(single_dir)
		ftp.chdir(single_dir)
		files = ftp.listdir(ftp.curdir)
		for f in files:
			if ftp.path.isfile(f):
				store_path_file = os.path.join(store_root_dir, f)
				download_host.retrbinary('RETR '+f, open(store_path_file, 'wb').write)
				
	download_host.quit()

def walkDir(channel_path):
	'''
	channel_directory is the absolute path of what user wants to get. 
	this function walks through the complete destination directory
	and see what's in there(get files and sub-direcotries).
	'''
	for x in ftp.walk(channel_path):
		yield x

def userConfig():
	'''
	get server, user, password in a config.txt file.
	'''
	user_config = open('user_config.db','r')
	for line in user_config.readlines():
		exec(line)
	return server, user, password

def storeDir():
	'''
	get current working directory path.
	generate download directory.
	return abs. path of download directory.
	'''
	current_work_path = os.getcwd()
	base_dir_len = len(os.path.basename(current_work_path))
	download_path = os.path.join(current_work_path[:-base_dir_len], 'download')

	return download_path



def main():
	final_dirs = []
	materials = walkDir(userRequire())   # subsitute variable 'workDirecotry' to func(baseDire) later. 
	for d in materials:
		final_dirs.append(d[0])
	root_dir = os.path.basename(final_dirs[0])

	fileDownload(final_dirs, root_dir)
	



if __name__ == '__main__':
	server, user, password = userConfig()
	go_ahead = True
	ftp = ftputil.FTPHost(server, user, password)
	print '\n', WELCOME_MESSAGE 
	while go_ahead:
		main()
		user_command  = raw_input("Download complete! Press 'ENTER' to quit, or 'ANY KEY+ENTER' to continue: ")
		if user_command:
			go_ahead = True
		else:
			go_ahead = False

