import requests
import json
from fake_useragent import UserAgent
import sys

def usage():
	print "python getTimeStamps.py www.url.com"

time_stamps = set()
urls = []
def main(argv):
	ua = UserAgent()
	ua.update()
	base_url = argv[1]
	url = 'http://web.archive.org/__wb/calendarcaptures?url=http://'+base_url+'&selected_year=2017'
	headers = {'User-Agent':ua.random}
	response = requests.get(url)
	json_obj = json.loads(response.text)
	for month in json_obj:
		if month:
			for week in month:
				if week:
					for day in week:
						if day:
							for ts in day['ts']:
								time_stamps.add(ts)
	for ts in time_stamps:
		urls.append('http://web.archive.org/web/'+str(ts)+'/http://'+base_url)
	print urls
if __name__ == '__main__':
    main(sys.argv)
