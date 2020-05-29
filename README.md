# Word Cloud Server

## Install
1.
```bash
docker build -t word_cloud_server:latest .
```

2.
```bash
docker run -p 5000:5000 word_cloud_server:latest
```

## Usage
1. Open up: http://naresh1318.pythonanywhere.com/
2. Send POST request with a json object:
```angular2
curl -d '{"key1":"value1"}' -H "Content-Type: application/json" -X POST http://naresh1318.pythonanywhere.com/word
```
3. See it pop up:

![alt text](https://files.naresh1318.com/public/word_cloud_server/index.png "Logo Title Text 1")

4. Refresh page to reset.

## Built using
* Flask
* Vue JS
