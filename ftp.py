# -*- coding: utf-8 -*-

import os, sys, re
import ftputil, ftplib

__version__ = 'Rev 0.2, Nov.5th, 2014'
WELCOME_MESSAGE = 'You are connected to FTP server!'
CONNECT_ERROR   = 'Connecting Failed!' 
Debug = '#Debug Tag#'


# E MIT-CTE CTE-MIT tested.
# C MIT-CTE CTE-MIT to be tested.

dir_group = {'AB-MIT-3-CTE'  : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/MIT-CTE/35000~39999/',
	     'AB-MIT-0-CTE'  : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/MIT-CTE/05000~05999/',
	     'AB-CTE-3-MIT'  : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/CTE-MIT/35000~35999/',
	     'AB-CTE-0-MIT'  : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/CTE-MIT/05000~05999/',
	     'AB-SDB-40-ANE' : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/SDB-ANE/400000-409999/',
	     'AB-SDB-43-ANE' : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/SDB-ANE/430000-439999/',
	     'AB-SDB-44-ANE' : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/SDB-ANE/440000-449999/',
	     'AB-SDB-495-ANE': '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/SDB-ANE/495000-499999/',
	     'AB-SDB-51-ANE' : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/SDB-ANE/510000-519999/',
	     'AB-SDB-6-ANE'  : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/SDB-ANE/600000-699999/',
	     'AB-SDB-7-ANE'  : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/SDB-ANE/700000-799999/',
	     'AB-SDB-99-ANE' : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/SDB-ANE/990000-999999/',
	     'AB-SDB-0-AEQ'  : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/SDB-AEQ/000001-099999/',
	     'AB-SDB-36-IICS': '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/SDB-AEQ/360000-369999/IICS/',
	     'AB-SDB-36-IITF': '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/SDB-AEQ/360000-369999/IITF/',
	     'AB-SDB-30-IICS': '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/SDB-AEQ/300000-399999/IICS/',
	     'AB-SDB-30-IITF': '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/SDB-AEQ/300000-399999/IITF/',
	     'AB-SDB-99-AEQ' : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/SDB-AEQ/990000~999999/',
	     'AB-AEQ-0-SDB'  : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/AEQ-SDB/000001-099999/',
	     'AB-AEQ-30-IICS': '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/AEQ-SDB/300000-399999/IICS/',
	     'AB-AEQ-30-IITF': '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/AEQ-SDB/300000-399999/IITF/',
	     'AB-AEQ-36-IICS': '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/AEQ-SDB/360000-369999/IICS/',
	     'AB-AEQ-36-IITF': '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/AEQ-SDB/360000-369999/IITF/',
	     'AB-AEQ-99-SDB' : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/AEQ-SDB/990000-999999/',
	     'AB-ANE-0-SDB'  : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/ANE-SDB/000001-099999/',
	     'AB-ANE-40-SDB' : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/ANE-SDB/400000-419999/',
	     'AB-ANE-43-SDB' : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/ANE-SDB/430000-439999/',
	     'AB-ANE-44-SDB' : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/ANE-SDB/440000-449999/',
	     'AB-ANE-456-SDB': '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/ANE-SDB/456000-456999/',
	     'AB-ANE-490-SDB': '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/ANE-SDB/490000-494999/',
	     'AB-ANE-495-SDB': '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/ANE-SDB/495000-499999/',
	     'AB-ANE-6-SDB'  : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/ANE-SDB/600000-699999/',
	     'AB-ANE-7-SDB'  : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/ANE-SDB/700000-799999/',
	     'AB-ANE-9-SDB'  : '/01.项目文件/00.CPR1000项目/04.CPR1000 PROJECT E/00_收发文件/ANE-SDB/990000-999999/',
	     'AA-AEQ-0-SDB'  : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/AEQ-SDB/000001-099999/',
	     'AA-AEQ-30-IICS': '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/AEQ-SDB/300000-399999/IICS/',
	     'AA-AEQ-30-IITF': '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/AEQ-SDB/300000-399999/IITF/',
	     'AA-AEQ-36-IICS': '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/AEQ-SDB/360000-369999/IICS/',
	     'AA-AEQ-36-IITF': '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/AEQ-SDB/360000-369999/IITF/',
	     'AA-AEQ-6-SDB'  : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/AEQ-SDB/600000-699999/',
	     'AA-AEQ-99-SDB' : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/AEQ-SDB/990000-999999/',
	     'AA-ANE-0-SDB'  : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/ANE-SDB/000001-099999/',
	     'AA-ANE-40-SDB' : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/ANE-SDB/400000-419999/',
	     'AA-ANE-43-SDB' : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/ANE-SDB/430000-439999/',
	     'AA-ANE-44-SDB' : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/ANE-SDB/440000-449999/',
	     'AA-ANE-456-SDB': '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/ANE-SDB/456000-456999/',
	     'AA-ANE-490-SDB': '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/ANE-SDB/490000-490999/',
	     'AA-ANE-495-SDB': '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/ANE-SDB/495000-495999/',
	     'AA-ANE-6-SDB'  : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/ANE-SDB/600000-699999/',
	     'AA-ANE-7-SDB'  : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/ANE-SDB/700000-899999/',
	     'AA-ANE-9-SDB'  : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/ANE-SDB/990000-999999/',
	     'AA-SDB-0-AEQ'  : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/SDB-AEQ/000001-099999/',
	     'AA-SDB-30-IICS': '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/SDB-AEQ/300000-399999/IICS/',
	     'AA-SDB-30-IITF': '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/SDB-AEQ/300000-399999/IITF/',
	     'AA-SDB-36-IICS': '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/SDB-AEQ/360000-369999/IICS/',
	     'AA-SDB-36-IITF': '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/SDB-AEQ/360000-369999/IITF/',
	     'AA-SDB-99-AEQ' : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/SDB-AEQ/990000-999999/',
	     'AA-SDB-99-ANE' : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/SDB-ANE/990000-999999/',
	     'AA-MIT-3-CTE'  : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/MIT-CTE/35000-35999/',
	     'AA-MIT-0-CTE'  : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/MIT-CTE/05001-09999/',
	     'AA-CTE-3-MIT'  : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/CTE-MIT/35000-35999/',
	     'AA-CTE-0-MIT'  : '/01.项目文件/00.CPR1000项目/02.CPR1000 PROJECT C/00_收发文件/CTE-MIT/05001-06999/'
	    }


project_pattern = {'pro_ND34' :{'AB-MIT-3-CTE':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(MIT)',
			    		        're4':'(-| )?',
			    		        're5':'(3[5|6]\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AB-CTE-3-MIT':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(CTE)',
			    		        're4':'(-| )?',
			    		        're5':'(3[5|6]\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AB-MIT-0-CTE':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(MIT)',
			    		        're4':'(-| )?',
			    		        're5':'(05\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AB-CTE-0-MIT':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(CTE)',
			    		        're4':'(-| )?',
			    		        're5':'(05\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AB-SDB-40-ANE':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(40\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AB-SDB-43-ANE':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(43\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AB-SDB-44-ANE':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(44\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AB-SDB-495-ANE':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(49[5-9]\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AB-SDB-51-ANE':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(51\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AB-SDB-6-ANE':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(6\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AB-SDB-7-ANE':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(7\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AB-SDB-99-ANE':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(99\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-SDB-0-AEQ':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(0\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-SDB-36-IICS':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(36\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-SDB-36-IITF':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(36\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-SDB-30-IICS':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(30\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-SDB-30-IITF':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(30\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-SDB-99-AEQ':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(99\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-AEQ-0-SDB':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(AEQ)',
			    		        're4':'(-| )?',
			    		        're5':'(0\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-AEQ-30-IICS':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(AEQ)',
			    		        're4':'(-| )?',
			    		        're5':'(30\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-AEQ-30-IITF':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(AEQ)',
			    		        're4':'(-| )?',
			    		        're5':'(30\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-AEQ-36-IICS':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(AEQ)',
			    		        're4':'(-| )?',
			    		        're5':'(36\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-AEQ-36-IITF':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(AEQ)',
			    		        're4':'(-| )?',
			    		        're5':'(36\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-AEQ-99-SDB':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(AEQ)',
			    		        're4':'(-| )?',
			    		        're5':'(99\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-ANE-0-SDB':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(0\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-ANE-40-SDB':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(4[0|1]\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-ANE-43-SDB':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(43\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-ANE-44-SDB':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(44\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AB-ANE-456-SDB':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(456\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AB-ANE-490-SDB':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(49[0-4]\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
	                       			},
			        'AB-ANE-495-SDB':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(49[5-9]\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
	                       			},
			        'AB-ANE-6-SDB':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(6\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
	                       			},
			        'AB-ANE-7-SDB':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(7\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
	                       			},
			        'AB-ANE-9-SDB':{'re1':'(AB)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(9\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
	                       			},
				},
		   'pro_HYH34' :{'AA-MIT-3-CTE':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(MIT)',
			    		        're4':'(-| )?',
			    		        're5':'(3[5|6]\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AA-CTE-3-MIT':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(CTE)',
			    		        're4':'(-| )?',
			    		        're5':'(3[5|6]\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AA-MIT-0-CTE':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(MIT)',
			    		        're4':'(-| )?',
			    		        're5':'(05\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AA-CTE-0-MIT':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(CTE)',
			    		        're4':'(-| )?',
			    		        're5':'(05\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AA-SDB-40-ANE':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(40\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AA-SDB-43-ANE':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(43\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AA-SDB-44-ANE':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(44\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AA-SDB-495-ANE':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(49[5-9]\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AA-SDB-51-ANE':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(51\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AA-SDB-6-ANE':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(6\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AA-SDB-7-ANE':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(7\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AA-SDB-99-ANE':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(99\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-SDB-0-AEQ':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(0\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-SDB-36-IICS':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(36\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-SDB-36-IITF':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(36\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-SDB-30-IICS':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(30\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-SDB-30-IITF':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(30\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-SDB-99-AEQ':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(SDB)',
			    		        're4':'(-| )?',
			    		        're5':'(99\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-AEQ-0-SDB':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(AEQ)',
			    		        're4':'(-| )?',
			    		        're5':'(0\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-AEQ-30-IICS':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(AEQ)',
			    		        're4':'(-| )?',
			    		        're5':'(30\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-AEQ-30-IITF':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(AEQ)',
			    		        're4':'(-| )?',
			    		        're5':'(30\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-AEQ-36-IICS':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(AEQ)',
			    		        're4':'(-| )?',
			    		        're5':'(36\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-AEQ-36-IITF':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(AEQ)',
			    		        're4':'(-| )?',
			    		        're5':'(36\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-AEQ-99-SDB':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(AEQ)',
			    		        're4':'(-| )?',
			    		        're5':'(99\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-ANE-0-SDB':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(0\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-ANE-40-SDB':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(4[0|1]\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-ANE-43-SDB':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(43\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-ANE-44-SDB':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(44\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'([A-Z]?)'
			                       },
			        'AA-ANE-456-SDB':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(456\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
			                       },
			        'AA-ANE-490-SDB':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(49[0-4]\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
	                       			},
			        'AA-ANE-495-SDB':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(49[5-9]\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
	                       			},
			        'AA-ANE-6-SDB':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(6\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
	                       			},
			        'AA-ANE-7-SDB':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(7\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
	                       			},
			        'AA-ANE-9-SDB':{'re1':'(AA)',
			    		        're2':'(-| )?',
			    		        're3':'(ANE)',
			    		        're4':'(-| )?',
			    		        're5':'(9\\d+)',
			    		        're6':'(-| )?',
			    		        're7':'[A-Z]?'
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
					     project_pattern[project][channel]['re5']+
					     project_pattern[project][channel]['re6']+
					     project_pattern[project][channel]['re7'],re.IGNORECASE|re.DOTALL)
			if pattern.search(user_input):
				label = channel
				channel_number = pattern.search(user_input).group(5)
	if channel_number[0] == '3' and label.find('II') != -1:
		new_label = ''
		iitf_iics = raw_input('Is it a IICS or IITF?\
				\n\tpress "ENTER" for IICS\
				\n\tpress "anykey + ENTER" for IITF--> ')
		if iitf_iics:
			new_label = label[:-4] + 'IITF'
		else:
			new_label = label[:-4] + 'IICS'
		label = new_label[:]
	elif channel_number[0:2] == '99' and label[1:5].find('SD') != -1:
		new_label = ''
		aeq_ane = raw_input('Is it SD*-99-ANE or SD*-99-AEQ?\
				\n\tpress "ENTER" for ANE\
				\n\tpress "anykey+ENTER" for AEQ-->')
		if not aeq_ane:
			new_label = label[:-3] + 'ANE' 
		else:
			new_label = label[:-3] + 'AEQ'
		label = new_label
	print Debug, 'label = %s, channel_number= %s' % (label, channel_number)
	return (label, channel_number) 

def userRequire():
	sub_path   = 'null'
	final_path = 'null'
	struc_stat = 'null'  # if there is no desired channel number found in FTP, struc_stat will stay 'null' 
	user_input = raw_input('May I have your channel number please?--> ')
	dir_group_label, input_channel_number = patternGenerator(user_input)
	basement_path = dir_group[dir_group_label]
	#print 'basement_path %s' % basement_path

	for path in basementWalk(basement_path):
		if input_channel_number in path[0:17]:
			struc_stat = 'found'
			#print 'path %s' % path
			if not os.path.splitext(path)[1]:      # here is a bug. how to tell if path stands for a file?
				sub_path = path
				struc_label = 'sub_path' 
				final_path = ftp.path.join(basement_path, sub_path)
			else:
				struc_label = 'none_subpath' 
				final_path = basement_path
			#print 'struc_label = %s' % struc_label 
	if struc_stat == 'null':
		struc_label = None
	return final_path, struc_label, input_channel_number


def fileDownload(final_dirs, root_dir, final_files):
	'''
	change current dir to destinaton dir.
	and download files in the destination dir.
	'''
	download_host = ftplib.FTP(server)
	download_host.login(user, password)

	# make a dir use final_dirs in system download dir
	store_dir = storeDir()
	store_root_dir = os.path.join(store_dir, root_dir)

	#print 'final_files %s' % final_files
	if not final_files:                                            # final_files: value will be None for normal required files.
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
	elif final_files:	# final_files: value will be final name for DEN like files.
		for final_file in final_files:
			download_path_file = os.path.join(final_dirs[0], final_file)
			store_path_file = os.path.join(store_dir, final_file)
			download_host.retrbinary('RETR '+download_path_file, open(store_path_file, 'wb').write)
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
	'''
	type_label is distinguash the 2 kinds of directories structure on FTP server.
	such as MIT-0-CTE for case1, ANE-456-SDB for case2.
	in case1 there will be sub_path; in case2 there will be document, but no sub_path.
	'''
	final_dirs = []
	final_files = []
	root_dir = ''
	walk_dir, struc_label, input_channel_number = userRequire()
	#print struc_label
	if struc_label == 'sub_path':
		materials = walkDir(walk_dir)   
		for d in materials:
			final_dirs.append(d[0])
			root_dir = os.path.basename(final_dirs[0]) #root_dir is used to generate new folder in download folder, 
	elif struc_label == 'none_subpath':
		final_dirs.append(walk_dir)
		for lookup_file in ftp.listdir(walk_dir):
			if input_channel_number in lookup_file[0:18]:
				final_files.append(lookup_file)
				root_dir = os.path.split(lookup_file)[0][0:-4]
	elif struc_label == None:
		raw_input('Your required channel couldn\'t be found on server.\
				Please check channel number then try again.\
				\nPress \'ENTER\' to quit.')
		sys.exit()
	fileDownload(final_dirs, root_dir, final_files)
	



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

