import requests, json, re

## create a function to use later to name the json files
def JsonFileName(x,y,z):
	separator = '_'
	result = x + separator + y + separator + z + '.json'
	return result

# DateConverter function takes NYT date string and turns it into TimelineJS-compatible date
# NYT >> "startDate": "1931-01-05T00:00:00Z"
# TimelineJS >> "startDate":"2011,12,10"

def DateConverter(date):
	year = date[0:4]
	month = date[5:7]
	day = date[8:10]
	comma = ","
	result = year + comma + month + comma + day
	return result

## create a list to append later
json_list = []

for year in range(1915,2015):

	begin_date = str(year) + '0101'
	end_date = str(year) + '1231'
	headline_term = 'headline:("birth control")'


	payload = {'fq': headline_term, 'begin_date': begin_date, 'end_date': end_date, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
	r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

	data = json.loads(r.text)

	# print (json.dumps(data, indent=4))

	print ("year:", year)
	## get count
	count = data['response']['meta']['hits']
	print ("count:",count)

	## divide by 10 to find total number of pages for year
	pages = int(count / 10)
	print ("pages:",pages)
	

	## loop through pages with dates
	for a_page in range(0,pages+1):

		payload = {'fq': headline_term, 'begin_date': begin_date, 'end_date': end_date, 'page': a_page, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
		r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

		data = json.loads(r.text)

		## pull headlines and date of publication

		if data['response']['docs']:

			for article in data['response']['docs']:
				headline = article['headline']['main']
				pub_date = DateConverter(article['pub_date'])
				web_url = article['web_url']
				snippet = article['snippet']


				## combine the gathered data
				headline_list = {"headline": headline, "pub_date": pub_date, "web_url": web_url, "snippet": snippet}

				# print (headline_list)

				## add the new data to the empty list
				json_list.append(headline_list)

				## use a regular expression to pull just the year out of the date
				# p = re.compile('\d\d\d\d')
				# m = p.search(headline_list)

				## name the file "headline", the number of results, and the year (regular expression)
				## replace str(year) below with (m.group(0)) for the regular expression to work
	file_name = JsonFileName("headlines","count" + str(count),str(year))

				## write the json files for each year
	with open(file_name, 'w') as f:
		f.write(json.dumps(json_list,indent=4))

	json_list = []



