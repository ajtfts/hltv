#example script to save data to google sheet
#output spreadsheet can be found here: https://docs.google.com/spreadsheets/d/1TD3zF8H3HriOV0MT7EC727T26GahIWV9p5NaxsjA7Mg/edit#gid=0
import gspread
import hltv
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('YOUR_KEY_HERE.json', scope) #follow directions at https://gspread.readthedocs.io/en/latest/oauth2.html to obtain key/do other stuff with gspread

gc = gspread.authorize(credentials)

sheet = gc.open('hltv-spreadsheet').sheet1

match = hltv.matchinfo("http://www.hltv.org/match/2302534-tyloo-renegades-pgl-kespa-regional-minor-championship-asia")

sheet.update_acell('B1', match.team0)
sheet.update_acell('C1', match.team1)

i = 2
for key in match.maps:
	mapadd = "A" + str(i)
	scoreadd0 = "B" + str(i)
	scoreadd1 = "C" + str(i)
	sheet.update_acell(mapadd, key)
	sheet.update_acell(scoreadd0, match.maps[key][0])
	sheet.update_acell(scoreadd1, match.maps[key][1])
	i += 1