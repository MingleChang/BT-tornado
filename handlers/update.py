#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.base import BaseHandler
from settings import STATIC_PATH
import os.path
from models.models import File
import json
import uuid

class UpdateHandler(BaseHandler):
	def  get(self):
		self.render('update.html')

	def  post(self):
		upload_path=os.path.join(STATIC_PATH,'files')
		file_metas=self.request.files['file']
		for meta in file_metas:
			filename=meta['filename']
			filepath=os.path.join(upload_path,filename)
			with open(filepath,'wb') as up: 
				up.write(meta['body'])
			fileid=uuid.uuid1().hex
			btfile=File()
			btfile.fileid=fileid
			btfile.title=filename
			btfile.path=os.path.join('files',filename)
			self.db.add(btfile)
			self.db.commit()
			self.db.close()
		self.redirect('/update')