# Word Cloud Server

## Usage
1. Open up: http://naresh1318.pythonanywhere.com/
2. Send POST request with a json object:
```angular2
curl -d '{"key1":"value1"}' -H "Content-Type: application/json" -X POST http://naresh1318.pythonanywhere.com/word
```
3. See it pop up:

![alt text](https://raw.githubusercontent.com/Naresh1318/word_cloud_server/master/README/browser.jpg "Logo Title Text 1")

4. Refresh page to reset.

## Built using
* Flask
* Vue JS
