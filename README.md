Python 3 Google Cloud Function Demo
===================================

### Local

Create a virtual environment for your python function(s).

```sh
$ mkvirtualenv -a $PWD -p `which python3` py3cloundfunc
```

Install dependencies locally

``` sh
$ pip install -r requirements.txt
```

Run the app

```
$ python main.py
```

View it in the browser

``` sh
$ open http://localhost:8080
```

### Manual Deployment

Deploy it

```sh
$ gcloud functions deploy hello_pubsub --runtime python37 --trigger-resource TOPIC_NAME --trigger-event google.pubsub.topic.publish
```
