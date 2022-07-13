import csv
from singleton_decorator import singleton


DB_NAME = 'database.csv'
SUBSCRIBER_TIMEOUT = 1000	# 40 req/sec


@singleton
class Subscriber:
	def get_topics(self, topic: str) -> list:
		res = []
		try:
			with open(DB_NAME, mode='r') as file:
				csvFile = csv.reader(file)
				for linea in csvFile:
					if linea[1] == topic:
						res.append(linea)
		except Exception as e:
			print(e)
		return res