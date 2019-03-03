# CraftBeerChecker
Scrapes the taproom list for the local breweries and alerts to new or favored offerings.

This is a little project I started for myself becasue I constantly found myself missing out on tasting some very limited time offering from my favorite local craft brewery. This is primarliy a learning project for me to practice with some libraries I've not worked with before.

## Roadmap 
* Feature - (Packages to learn)

* Webscraping - (Selenium Webdriver, BeautifulSoup, PostgreSQL)

      * Build it in a general form so that it can be table driven (only 
      requirment to add another brewery to be scraped should be to add a 
      new row to the DB)

* Analysis - (pandas, PostgreSQL)
      
      * Report on new offerings of the day at each particular brewery.
      * Have a watchlist of favorite offerings or styles to report on 
      when they become available.
      * Check the daily new offerings list against historic data and report 
      on brand new (never released before) offerings
      
* Reporting - (???)
  
      * Want to send emails out to communicate the analysis
