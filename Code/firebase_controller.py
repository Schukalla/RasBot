# firebase.py

import os
import firebase_admin
from firebase_admin import credentials, firestore
import time
import keyboard

class Firebasec:
	def __init__(self):
		config = {
    		#[API_Key]
		}

		cred = credentials.Certificate(config)
		app = firebase_admin.initialize_app(cred)

		db = firestore.client()
		self.rasbots_ref = db.collection("rasBots")
		rasbots = self.rasbots_ref.stream()

	def response(self):
		None

	def getdir(self):
		query = self.rasbots_ref.where("rasBotId", "==", "1234")
		docs = query.stream()
		#print("\r", end="")
		for doc in docs:
			data = doc.to_dict()
			return data['x'], data['y']



