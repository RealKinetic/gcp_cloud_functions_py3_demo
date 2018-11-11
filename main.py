import base64
import json
import logging

from google.cloud import datastore

MESSAGE_KIND = "Message"


def hello_pubsub(data, context):
    if not 'data'in data:
        logging.warn("*** NO DATA ***")
        return

    result = base64.b64decode(data['data']).decode('utf-8')

    logging.info("RESULT:")
    logging.info(result)

    json_result = json.loads(result)
    datastore_client = datastore.Client()

    message_key = datastore_client.key(MESSAGE_KIND, json_result['id'])
    message = datastore_client.get(message_key)

    if not message:
        logging.warn("Unable to load message for: {}".format(message_key))
        return

    message['acked'] = True
    datastore_client.put(message)

    logging.info("Message acked and saved.")
