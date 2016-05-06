#example script to save data to google sheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import main

scope = ["https://spreadsheets.google.com/feeds"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('YOUR_KEY_HERE.json', scope)

gc = gspread.authorize(credentials)

sheet = gc.open('hltv-spreadsheet').sheet1

match = main.matchinfo("http://www.hltv.org/match/2302534-tyloo-renegades-pgl-kespa-regional-minor-championship-asia")

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