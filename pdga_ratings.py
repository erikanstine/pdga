import requests

from datetime import datetime as dt

from lxml import etree


USER_AGENT = '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'''


def get_player_page(pdga_num):
	player_page = requests.get('https://www.pdga.com/player/{}'.format(pdga_num))

	return player_page.html

def get_ratings_detail():
	# Get rounds already included

	detail_page = requests.get('https://www.pdga.com/player/{}/details'.format(pdga_num))

	return detail_page.

def get_event_links(n):
	page_html = get_player_page(n)
	
	page_tree = etree.parse(page_html)
	event_links = page_tree.[x.href]




def get_league_page():
	return


def parse_league_page():
	# Parse event in 
	return


def parse_tournament_page():
	return 


def parse_date(date_string):

	return

def make_league_date_list(date_string):
	# eg., 26-Sep to 28-Nov-2020
	date_format_string = "%d-%b-%Y"
	fstring, tstring = date_string.split(" to ")
	to_date = dt.strptime(tstring, date_format_string)
	from_date = dt.strptime("{}-{}".format(fstring, to_date.year), date_format_string)

	return [from_date + dt.timedelta(days=x) for x in range(0, (to_date - from_date).days, 7)]



'''
1. Get existing ratings
2. Check new rounds for more recent than included rounds
3. Calculate new rating
'''