# This tool will help you search for jobs on Indeed!
# Currently, it really only searches for searches in
# a list, but it's coming along!

from personal_info import search_list, location
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from project_functions import count_items_in_list, bash_command
from datetime import datetime

num_of_things_to_search = count_items_in_list(search_list, 'quiet')
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

firefox = webdriver.Firefox()
firefox.get('http://indeed.com/')
sleep(3)


for current_string in range(num_of_things_to_search):
    current_search = search_list[current_string]
    job_search = firefox.find_element_by_id('text-input-what')
    location_search = firefox.find_element_by_id('text-input-where')
    job_search.clear()
    job_search.send_keys(current_search)
    location_search.clear()
    location_search.send_keys(location)
    location_search.send_keys(Keys.RETURN)
    sleep(3)
    src = firefox.page_source

    if 'Just posted' in src:
        print(f"'{current_search}' yielded a result that was just posted!")
        bash_command(f"echo 'POSTED NOW: {firefox.current_url} at {current_time}' >> justPostedURLs.txt")
    elif 'Today' in src:
        print(f"A job's been posted today for search, '{current_search}'")
        bash_command(f"echo 'Posted Today: {firefox.current_url} at {current_time}' >> justPostedURLs.txt")
    else:
        print(f'{current_search} yielded nothing new.')

    firefox.back()
    sleep(1)
