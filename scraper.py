from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime
import re
import csv

#TODO can make this more general. Give the general version target_url and brewery variables as inputs and have site specific cleaning/scraping steps confined to thier own functions (or use decorators?)
def altamont_scraper(target_url, brewery, name_element_type, name_element_name, style_element_type, style_element_name, abv_element_type, abv_element_name):

    option = webdriver.ChromeOptions()
    option.add_argument("incognito")
    option.add_argument("headless")

    # target_url = "https://altamontbeerworks.com/1/taproom/"

    browser = webdriver.Chrome(executable_path="/home/adam/Documents/Projects/CraftBeerChecker/Utils/chromedriver", chrome_options=option)

    browser.get(target_url)

    timeout = 20
    try:
        WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.CLASS_NAME ,'item-title-color')))
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()

    if name_element_type == 'class':
        beers_name_finder = browser.find_elements_by_class_name(name_element_name)
    elif name_element_type == 'other': #TODO fill out the other types of capture tags (ID, nth child of something etc. as determined when encountered)
        pass

    if style_element_type == 'class':
        beers_style_finder = browser.find_elements_by_class_name(style_element_name)
    elif style_element_type == 'other':
        pass

    if abv_element_type == 'class':
        beers_abv_finder = browser.find_elements_by_class_name(abv_element_name)
    elif abv_element_type == 'other':
        pass



    # beers_name_finder = browser.find_elements_by_class_name('beer-name')
    # beers_style_finder = browser.find_elements_by_class_name('beer-style')
    # beers_abv_finder = browser.find_elements_by_class_name('abv')

    beers_name = [x.text for x in beers_name_finder]
    beers_style = [x.text for x in beers_style_finder]
    beers_abv = [x.text for x in beers_abv_finder]

    today = str(datetime.date.today())
    # brewery = "Altamont"

    output_list = []
    if len(beers_name) == len(beers_style) and len(beers_style) == len(beers_abv):

        for name, style, abv in zip(beers_name, beers_style, beers_abv):
            my_reg_ex = ".{}".format(style)
            name_clean = re.sub(my_reg_ex, '', name)
            item = [name_clean, style, abv, today, brewery]
            output_list.append(item)
    else:
        for name in beers_name:
            item =[name, "ERR", "ERR", today, brewery]
            output_list.append(item)

    #Saves scraped data to a csv file
    with open('beer_log.csv', mode='a') as csvfile:
        record_writer = csv.writer(csvfile)
        for row in output_list:
            record_writer.writerow(row)

    print("Checked {}'s tap list".format(brewery))


    browser.quit()

altamont_scraper("https://altamontbeerworks.com/1/taproom/", "Altamont", 'class', 'beer-name', 'class', 'beer-style', 'class', 'abv')