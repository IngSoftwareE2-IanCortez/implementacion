import csv
from singleton_decorator import singleton


DB_NAME = 'database.csv'
PUBLISHER_TIMEOUT = 2000	# 20 req/sec


@singleton
class Publisher:
	def save_topic(self, message: str, topic: str) -> str:
		try:
			with open(DB_NAME, mode='a', newline='') as file:
				csv_file = csv.writer(file)
				data = [message, topic]
				csv_file.writerow(data)
			return 'ok'
			
		except Exception as e:
			print(e)
			return 'fail'