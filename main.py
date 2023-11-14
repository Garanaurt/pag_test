import time
from datetime import datetime, timedelta
import random
from random import randint
import pyautogui as pag
from pyautogui import ImageNotFoundException
import platform
import pyperclip
import re
import webbrowser

keywords_list = ['python', 'js'] # keywords for search

site = "https://habr.com" # our site

num_visits = 2 

class TrafficBot:
    def __init__(self, site_url, search_keywords, num_visits):
        self.site_url = site_url
        self.search_keywords = search_keywords.copy()
        self.system = platform.system()
        self.num_visits = num_visits


    def start_browser(self) -> None:
        """start browser in os, tested on linux"""
        if self.system == 'Linux':
            webbrowser.open('https://www.google.com/')
            time.sleep(3)
        elif self.system == 'Windows':
            webbrowser.open('https://www.google.com/')
            time.sleep(3)


    def close_browser(self) -> None:
        pag.hotkey('ctrl', 'w')


    def move_proportionally(self, x, y, duration=0)-> None:
        """move mouse propotionally screen size 1366/768"""
        original_width, original_height = 1366, 768
        size = pag.size()
        new_width, new_height = (size.width, size.height)
        relative_width = x / original_width
        relative_height = y / original_height
        new_x = int(relative_width * new_width)
        new_y = int(relative_height * new_height)
        pag.moveTo(new_x, new_y, duration)


    def search_and_fool_site(self)-> None:
        """main method for searching and visits site"""
        visit_done = 0
        while visit_done < self.num_visits:
            self.start_browser()
            time.sleep(3)
            keywords = self.search_keywords.copy()
            random.shuffle(keywords)
            site_fool = False
            while not site_fool:
                try:
                    keyword = keywords.pop()
                    site_fool = self.search(keyword)
                    if site_fool:
                        visit_done += 1
                except IndexError:
                    print('all keywords are passed or the list of keywords is empty')
                    self.close_browser()
            else:
                print(f'site fooling done - #{visit_done}')
                self.close_browser()
        quit()
                
            
    def search(self, keyword) -> bool:
        """on the first iteration of the search, the bot gets all the links on the page and randomly jumps to two for it,
        if our site on the first page - the bot goes to it after the first two pages
        on the second and + iteration, the bot checks our site on the search page, if the site on it, the bot goes to it"""
        start = 1
        first_iter = True
        for _ in range(50): # 50 pages
            self.load_search_page(keyword, start)
            self.move_proportionally(300, 340, 1) # go to free area

            site_on_page = self.check_site_on_page()

            if first_iter == True:
                sites_for_visit =  self.get_random_sites_for_visit()
                two_random_sites = random.sample(range(len(sites_for_visit)), 2)
                for k, v in sites_for_visit.items():
                    if k in two_random_sites:
                        for index, box in enumerate(v):
                            if box != site_on_page[1] and index == 1:
                                self.visit_site(randint(10, 15), box, k)
                                time.sleep(2)
                                pag.press('home')
                                time.sleep(1)
                if site_on_page[0] == True:
                    self.visit_site(randint(300, 600), site_on_page[1], site_on_page[2])
                    return True
                first_iter = False
                start = 10
            else:
                if site_on_page[0] == True:
                    self.visit_site(randint(300, 600), site_on_page[1], site_on_page[2])
                    return True
                start += 10
        return False
    

    def get_random_sites_for_visit(self) -> dict:
        """Get links on the page for random visits"""
        sites_for_visit = {}
        for i in range(6):
            results = pag.locateAllOnScreen('https.png')
            sites_for_visit[i] = results
            self.move_proportionally(300, 340)
            pag.scroll(-3)
            time.sleep(1)
        pag.press('home')
        return sites_for_visit
    

    def load_search_page(self, keyword, start) -> None:
        """get search page google.com"""
        #self.move_proportionally(500, 80)
        #pag.click()
        url = f'https://www.google.com/search?q={keyword}&start={start}'
        pag.hotkey('ctrl', 'a')
        time.sleep(1)
        pag.press('del')
        time.sleep(1)
        pag.write(url)
        pag.press('enter')
        time.sleep(1)
        

    def check_site_on_page(self) -> tuple:
        """find our link in the text of the page. If site-link on page - check coordinates"""
        pag.hotkey('ctrl', 'a')
        pag.hotkey('ctrl', 'c')
        self.move_proportionally(1000, 300)
        pag.click()
        links = re.findall(r'https?://[^\s]+', pyperclip.paste())
        if self.site_url in links:
            find = False
            scroll = 0
            while not find:
                try:
                    coord = pag.locateOnScreen('site_url_screen.png')
                    find = True
                except ImageNotFoundException:
                    self.move_proportionally(660, 300)
                    pag.scroll(-3)
                    time.sleep(1)
                    scroll +=1
            return True, coord, scroll
        else:
            return False, False, False


    def visit_site(self, time_to_visit, coords, scroll) -> None:
        """visit the site from the search page and scroll it"""
        for _ in range(scroll):
            pag.scroll(-3)
            time.sleep(1)
        time.sleep(1)
        pag.click(coords)
        time.sleep(2)
        time_start = datetime.now()
        while datetime.now() - time_start < timedelta(seconds=time_to_visit):
            pag.scroll(randint(-10, -4))
            time.sleep(randint(1, 3))
            pag.scroll(randint(3, 9))
            time.sleep(randint(1, 3))
        else:
            pag.hotkey('alt', 'left')
 

if __name__ == "__main__":
    site_url = site
    search_keywords = keywords_list
    num_visits = num_visits

    bot = TrafficBot(site_url, search_keywords, num_visits)
    bot.search_and_fool_site()
