from bs4 import BeautifulSoup
import requests

class matchinfo():
	def __init__(self,url):
		self.url = url
		self.scrape()
	def scrape(self):
		headers = {
			"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
			"accept-encoding": "gzip,deflate,sdch",
			"accept-language": "en-US,en;q=0.8",
		}
	
		r = requests.get(self.url, headers=headers)
	
		if r.status_code != 200:
			print("request denied")
			return
		else: 
			print("scraping " + self.url)
	
		soup = BeautifulSoup(r.content, "html.parser")

		#find team names
		tags = soup.find_all("a", {"class" : "nolinkstyle"})
		self.team0 = tags[0].string
		self.team1 = tags[1].string

		#player names
		self.playerlist0 = []
		self.playerlist1 = []

		i = 0
		for tag in soup.find_all("span", {"style" : "font-size:12px;"}):
			if i < 5:
				self.playerlist0.append(tag.string)
			else:
				self.playerlist1.append(tag.string)
			i += 1

		#date/time
		tags = soup.find("span", {"style" : "font-size:14px;"})
		self.date = tags.string.strip()
		tags = soup.find("span", {"style" : "margin-left:10px;"})
		self.time = tags.string.strip()

		#maps
		self.maps = []
		for tags in soup.find_all("img", {"style" : "border-radius: 4px;;"}):
			src = str(tags['src'])
			if src == "http://static.hltv.org//images/hotmatch/tba.png":
				self.maps.append("TBA")
			elif src == "http://static.hltv.org//images/hotmatch/dust2.png":
				self.maps.append("dust2")
			elif src == "http://static.hltv.org//images/hotmatch/cache.png":
				self.maps.append("cache")
			elif src == "http://static.hltv.org//images/hotmatch/nuke.png":
				self.maps.append("nuke")
			elif src == "http://static.hltv.org//images/hotmatch/cobblestone.png":
				self.maps.append("cobble")
			elif src == "http://static.hltv.org//images/hotmatch/mirage.png":
				self.maps.append("mirage")
			elif src == "http://static.hltv.org//images/hotmatch/overpass.png":
				self.maps.append("overpass")
			elif src == "http://static.hltv.org//images/hotmatch/train.png":
				self.maps.append("train")
			elif src == "http://static.hltv.org//images/hotmatch/inferno.png":
				self.maps.append("inferno")
			else:
				self.maps.append("UNKWN")



match0 = matchinfo("http://www.hltv.org/match/2302158-tsm-complexity-ecs-season-1")


print(match0.team0)
print(match0.team1)
print(match0.playerlist0)
print(match0.playerlist1)
print(match0.date+" "+match0.time)
print(match0.maps)