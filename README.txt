hptimeline
==========
This project is a timeline from 1915 to the present showing headlines with the words “birth control” from the New York Times. We wrote a script in Python (nytimes_api.py) to pull the relevant data from the NYT Article Search API; this included the publish date, a text snippet, and the URL to the full article. Running this script resulted in one JSON file for each year that included all the headlines and data for that year—a total of 100 files. A second script (timeline_js.py) pulled these files together into a single JSON file, and reformatted the data to fit the parameters outlined by the Timeline JS platform. We then downloaded a Bootstrap theme for Timeline JS to use with our JSON file. 

The last script (csv_file.py) we wrote pulled the number of headlines per year and wrote this information out as a CSV file. Using this data, we created a visualization charting the number of headlines over time. We used this graph as the landing page image on the timeline, and further edited the HTML to optimize the display.


— Run nytimes_api.py to create 100 JSON files with headline data
— Run timeline_js.py to make one file with the data correctly formatted for Timeline JS
— Download Bootstrap theme for Timeline JS, and put JSON file in the directory
— Locally host directory to see timeline
— Run csv_file.py to get headline count data
— Edit HTML to include the image and to zoom out

Graph image link: http://www.samantharaddatz.com/uploads/3/8/5/7/3857159/2615005_orig.png

Credits:
Rachel Bronstein (@rmaryab)
Hannah Goldstein (@han_goldstein)
Samantha Raddatz (@samradd)
