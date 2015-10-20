#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
from models.models import File
import os.path
from settings import STATIC_PATH
from common.btcode import BTCode
import json

class DetailHandler(BaseHandler):
	def  get(self,fileid):
		self.showFile(fileid)

	def  post(self,fileid):
		self.showFile(fileid)

	def showFile(self,fileid):
		files=self.db.query(File.path,File.title,File.fileid).filter(File.fileid==fileid)
		if files.count==0:
			self.render('detail.html',file={})
		else:
			file=files[0]
			filepath=os.path.join(STATIC_PATH,file[0])
			dic=BTCode.decodepath(filepath)
			dic['title']=file[1]
			dic['fileid']=file[2]
			self.render('detail.html',file=dic)