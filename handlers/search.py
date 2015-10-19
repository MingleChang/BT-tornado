#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
from models.models import File
from sqlalchemy.orm import class_mapper
import json

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
			dic={}
			dic['fileid']=file[0]
			dic['title']=file[1]
			dic['path']=file[2]
			arr.append(dic)
		self.render('search.html',files=arr)