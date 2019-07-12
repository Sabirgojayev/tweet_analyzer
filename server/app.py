from flask import Flask
from flask import request, jsonify, make_response

from static.prediction import get_prediction_for_tweet
import tensorflow as tf

app = Flask(__name__)
graph = tf.get_default_graph()


@app.route('/predict', methods=['POST'])
def predict():
    tweet = request.get_json()['tweet']

    # required to correctly handle tensorflow session
    global graph
    with graph.as_default():
        prediction = get_prediction_for_tweet(tweet)

    response_body = {
        "prediction": str(prediction),
    }

    return make_response(jsonify(response_body), 200)


if __name__ == '__main__':
    app.run()