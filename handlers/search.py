#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
from models.models import File
import os.path
from settings import STATIC_PATH
from common.btcode import BTCode
class SearchHandler(BaseHandler):
	def  get(self):
		searchkey=self.get_argument('searchkey','')
		if searchkey=='':
			self.redirect('/')
		else:
			self.search(searchkey)

	def  post(self):
		searchkey=self.get_argument('searchkey','')
		if searchkey=='':
			self.redirect('/')
		else:
			self.search(searchkey)

	def search(self,searchkey):
		files=self.db.query(File.fileid,File.title,File.path,File.create).filter(File.title.like(u"%"+searchkey+"%"))
		arr=[]
		for file in files:
			filepath=os.path.join(STATIC_PATH,file[2])
			dic=BTCode.decodepath(filepath)
			dic['fileid']=file[0]
			dic['title']=file[1]
			arr.append(dic)
		self.render('search.html',files=arr)