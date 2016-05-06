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

		#match status
		tags = soup.find("div", {"style" : "text-align:center;font-size: 18px;"})
		if tags.string == "Match over":
			self.status = 0
		else:
			self.status = 1

		#maps/scores
		self.maps = {}
		
		i = 0
		tags = soup.find("div", {"style" : "text-align: center;font-size: 12px;text-align: left;"})
		for imgdivs in tags.find_all("div", {"style" : "border: 1px solid darkgray;border-radius: 5px;width:280px;height:28px;margin-bottom:3px;"}):
			if imgdivs.img['style'] == "border-radius: 4px;opacity:0.4;":
				break
			scoredivs = tags.find_all("div", {"class" : "hotmatchbox"})
			m = scoredivs[i].find_all("span")
			self.maps[imgdivs.img['src'][40:-4]] = [m[0].string, m[1].string]
			i += 1


'''match0 = matchinfo("http://www.hltv.org/match/2302534-tyloo-renegades-pgl-kespa-regional-minor-championship-asia")


print(match0.team0)
print(match0.team1)
print(match0.playerlist0)
print(match0.playerlist1)
print(match0.date+" "+match0.time)
print(match0.status)
print(match0.maps)'''