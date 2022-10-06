* get_data.py 
  * get information on Taipei attractions including title, location district, longitude, latitude, and imageUrl from the webpage
  * save attraction information as data.csv
* movie_crawler.py 
  * get article titles starting with keywords of [好雷], [普雷], [負雷] for 10 pages on PTT Movie
  * save article titles in the order of [好雷], [普雷], [負雷] as movie.txt (Time: at 10:11 p.m. Teusday, on October 4, 2022)
* week-3.html 
  * display 10 images and titles of Taipei attractions
* week-3-ver-2.html
  * modify the "titleList" and "titleList2" separately contain 4 titleItems in week-3 to only one "titleList" which could append 8 titleItems
  * details: using flex-wrap to wrap 8 items into 2 rows with 4 items and altered item width and margin width by percentage rather than px in the media query condition with max-width of 1200 px and 600px
* week-3-ver-3.html
  * add a "LoadMore" button under the page and hambergur list
  * details: once the "LoadMore" button is clicked, the "titleList" will append 8 items by the origin items. once the hambergur list is clicked, a sidebar on the right will show, and hide when clicking on the page
