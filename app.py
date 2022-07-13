from flask import Flask, jsonify, request
from clients.publisher import Publisher
from clients.subscriber import Subscriber


app = Flask(__name__)


publisher = Publisher()
subscriber = Subscriber()


@app.route('/message/<topic>')
def get_topics(topic):
	data = request.headers.get('topic')
	response = subscriber.get_topics(topic=data)

	res = []
	for x in range(len(response)):
		d = {'message': response[x][0], 'topic': response[x][1]}
		res.append(d)

	return jsonify(res)


@app.route('/message', methods=['POST'])
def post_topic():
	data = request.form
	d1 = data["message"]
	d2 = data["topic"]
	response = publisher.save_topic(message=d1, topic=d2)
	return response


app.run(port=5000, debug=True)