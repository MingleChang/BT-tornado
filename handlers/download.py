#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
from models.models import File
import os.path
from settings import STATIC_PATH

class DownloadHandler(BaseHandler):
	def  get(self,fileid):
		self.download(fileid)

	def  post(self,fileid):
		self.download(fileid)

	def  download(self,fileid):
		files=self.db.query(File.path,File.title).filter(File.fileid==fileid)
		if files.count()==0:
			self.write('文件不存在')
		else:
			upload_path=os.path.join(STATIC_PATH,files[0][0])
			filename=files[0][1]
			self.set_header ('Content-Type', 'application/octet-stream')
			self.set_header ('Content-Disposition', 'attachment; filename='+filename)
			with open(upload_path, 'rb') as f:
				while True:
					data = f.read(1024)
					if not data:
						break
					self.write(data)
			self.finish()