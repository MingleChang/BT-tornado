#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bencode

class BTCode(object):
	def __init__(self):
		pass
	
	@staticmethod
	def decodepath(path):
		btfile=open(path,'rb')
		return BTCode.decodefile(btfile)

	@staticmethod
	def decodefile(btfile):
		btinfo=bencode.bdecode(btfile.read()).get('info')
		dic={}
		files=[]
		dic['name']=btinfo.get('name')
		dic['length']=BTCode.byteto(btinfo.get('piece length'))
		fileinfos=btinfo.get('files')
		fileinfos.sort(key=lambda obj:obj.get('length'), reverse=True) 
		for info in fileinfos:
			filedic={}
			filedic['path']=info['path'][0]
			filedic['length']=BTCode.byteto(info['length'])
			files.append(filedic) 
		dic['files']=files
		return dic

	@staticmethod
	def byteto(byte):
		if byte<1024:
			return str(byte)+'bytes'
		elif byte/1024.0<1024:
			return str(float('%0.2f'%(byte/1024.0)))+'KB'
		elif byte/1024.0/1024.0<1024:
			return str(float('%0.2f'%(byte/1024.0/1024.0)))+'MB'
		else:
			return str(float('%0.2f'%(byte/1024.0/1024.0/1024.0)))+'GB'
