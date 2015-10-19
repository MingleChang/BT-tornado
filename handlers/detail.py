#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.base import BaseHandler

class DetailHandler(BaseHandler):
	def  get(self,fileid):
		self.render('detail.html')

	def  post(self,fileid):
		self.render('detail.html')