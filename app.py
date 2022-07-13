from flask import Flask, jsonify, request
from clients.publisher import Publisher
from clients.subscriber import Subscriber


app = Flask(__name__)


publisher = Publisher()
subscriber = Subscriber()


@app.route('/message/<topic>')
def get_topics(topic):
	response = subscriber.get_topics(topic=topic)
	print('Res:', response)
	return jsonify(response)


@app.route('/message', methods=['POST'])
def post_topic():
	data = request.get_json()
	d1 = data["message"]
	d2 = data["topic"]
	response = publisher.save_topic(message=d1, topic=d2)
	return response


app.run(port=5000, debug=True)