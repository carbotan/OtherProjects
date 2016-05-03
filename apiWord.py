import requests

apiWord = requests.get("http://randomword.setgetgo.com/get.php?len=7")
print(apiWord.text)