import csv
from singleton_decorator import singleton


DB_NAME = 'database.csv'
PUBLISHER_TIMEOUT = 2000	# 20 req/sec


@singleton
class Publisher:
	def save_topic(self, message: str, topic: str) -> str:
		try:
			with open(DB_NAME, mode='a') as file:
				csvFile = csv.writer(file)
				csvFile.writerow([message, topic])
			return 'ok'
		except Exception as e:
			print(e)
			return 'fail'