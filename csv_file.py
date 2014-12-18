import requests, json, csv

with open('headline_count.csv', 'w', newline='') as csvfile:

	for year in range(1915,2015):

		begin_date = str(year) + '0101'
		end_date = str(year) + '1231'
		headline_term = 'headline:("birth control")'


		payload = {'fq': headline_term, 'begin_date': begin_date, 'end_date': end_date, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
		r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

		data = json.loads(r.text)

		# print (json.dumps(data, indent=4))

		# print ("year:", year)
		## get count
		count = data['response']['meta']['hits']
		# print ("count:",count)

		## divide by 10 to find total number of pages for year
		pages = int(count / 10)
		# print ("pages:",pages)

		# csv_data = []
		# csv_data.append(['year:',year,'count:',count])
		# print (csv_data)
		# the above list (csv_data) prints what we want in the terminal

		filewriter = csv.writer(csvfile, delimiter=',')

		filewriter.writerow(['year:',year,'count:',count])
		# 	filewriter.writerow(csv_data)







