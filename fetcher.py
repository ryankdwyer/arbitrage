import os
import time

import requests
from bs4 import BeautifulSoup as BS

import utils


class Fetcher:

    def __init__(self, filename):
        FILEPATH = utils.FILEPATH
        f = open(FILEPATH + filename)
        self.links = []
        for line in f:
            line = line.split(' ')
            self.links.append((line[0], int(line[1])))


    def do_work(self):
        while 1:
            link = self.links.pop()

            print "Working on link: %s" % link[0]

            if self.can_fetch(link[1]):
                html = self.fetch(link[0])
                if html:
                    scraped_data = self.scrape(html)
                    print "Scraped data: %s" % scraped_data
                else: 
                    print "Error scraping data"
            else:
                print "Too soon to fetch"

            link = (link[0], time.time())

            self.links.insert(0, link)

            print 'Sleeping for %s seconds...' % utils.INTERVAL

            time.sleep(utils.INTERVAL)


    def can_fetch(self, last_fetch):
        now = time.time()
        minutes_since = (now - last_fetch) / 60

        if minutes_since > utils.FETCH_EVERY:
            return True
        return False    


    def fetch(self, link):
        res = requests.get(link, headers=utils.HEADERS)

        if res.status_code == requests.codes.ok:
            parsed = BS(res.text, 'html.parser')
        else:
            print "Response code: %s" % res.status_code
            return False
        
        return parsed


    def scrape(self, html):
        data = {}
        ids = utils.AMAZON_DATA

        for id in ids:
            value = html.find(id=id)
            value = value.string
            if value:
                data[id] = value
        return data
