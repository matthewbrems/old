#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:46:40 2017

@author: jennydoyle
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:46:26 2017

@author: jennydoyle
"""
import pandas as pd
indeed = pd.DataFrame(columns=['job','company','location','salary','description'])

#.encode('utf-8')
def numbers_commas_to_int(string):
    import locale # given a string of a number with commas, convert to float
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') #for american comma notation
    # if european comma notation needed, change 2nd parameter to 'fr_FR'
    num = int(locale.atof(string))
    return int(num)

def get_location(webpage):
    tag = webpage.find('span', attrs={'class':'location'})
    try:
        return tag.text
    except:
        pass
    
def get_company(webpage):
    tag = webpage.find('span', attrs={'class':'company'})
    try:
        return tag.text.strip('\n')
    except:
        pass

def get_job(webpage):
    tag = webpage.find('a', title=True, attrs={'data-tn-element':'jobTitle'})
    try:
        return tag['title']
    except:
        pass

def get_salary(webpage):
    try:
        return webpage.find('table').tr.td.nobr.renderContents()
    except:
        pass

def get_description(webpage):
    description = webpage.find('span', attrs={'itemprop':"description"})
    try:
        return description.text.strip('\n')
    except:
        pass

def compile_files():
    import glob
    import pandas as pd
    import numpy as np
    indeed_csvs = '/Users/jennydoyle/Desktop/dsi/DC-DSI4/projects/03-Project/indeed/'
    files = glob.glob(indeed_csvs + '*.csv')
    print files
    indeed_final = pd.DataFrame(columns=['job','company','location','salary','description'])
    for f in files:
        f = pd.read_csv(f, names=['job','company','location','salary','description'],low_memory=False)
        indeed_final = indeed_final.append(f)
    indeed_final.drop_duplicates(inplace=True)
#    indeed = np.array(indeed_final)
    return indeed_final

def scrape_indeed():
    ## compile previously scraped results to see if there are new jobs to add
    indeed = compile_files()    
    base = len(indeed)
    import requests
    from bs4 import BeautifulSoup
    import datetime
    import time
    import re
    import numpy as np
    start = datetime.datetime.now()
    print 'Start time: ',start.strftime("%Y-%m-%d %H:%M:%S")
    print 'Base file has ', base, ' records'
    
    # save content of URL to variable page
    url = "http://www.indeed.com/jobs?q=data+scientist+%2420%2C000&fromage=last&start="
    x=0
    url_start = url+str(x) # if we set the start variable in the URL to 0 to begin with, it will first pull up results 1-10

    page = requests.get(url_start).content
    soup = BeautifulSoup(page,'lxml')
    print 'Page scraped & souped'
    # start at the first page of results and record the total number of results
    # this will be used to help us flip through all of the pages of results
    # the URL format uses start=x where x is a result number (instead of page number)
    for results in soup.find('div', attrs={'id':'searchCount'}):
        count = str(results).split()    # take the full line that says 'Jobs x to y of z' and turn into a list
        total = count[len(count)-1]          # set total to z, the total number o[f results
        total = numbers_commas_to_int(total) # since there are commas if the number > 999, this function will deal with that and convert to int
    x = 0 # if we set the start variable in the URL to 0 to begin with, it will first pull up results 1-10

    while x <= total/3:
        url_new_page = url + str(x)
        page = requests.get(url_new_page).content
        soup = BeautifulSoup(page)
        
        for num_listings in  soup.find('div', attrs={'id':'searchCount'}) :
            num_listings = num_listings.split()[3]
        
        main = soup.find('td',{'id':'resultsCol'})   # limit our searching to solely the results portion of the page
        results = main.find_all('div', {'class': re.compile("result$")}) # create a list consisting only of the 15 results

        for i in range(len(results)):
            job = get_job(results[i])
            company = get_company(results[i])         # put all companies for each posting on curent results page into companies list
            location = get_location(results[i])       # put all locations for each posting on current results page into locations list
            salary = get_salary(results[i])           # put all salaries for each posting on current results page into salaries list
            description = get_description(results[i]) # put all descriptions for each posting on current results page into descriptions list

            add_job = pd.DataFrame([[job, company, location, salary, description]], columns = ['job','company','location','salary','description'])
            a = np.array(add_job)
            if (indeed == a).all(1).any() == False:
                indeed = indeed.append(add_job)                


                
        x+=10
        new = len(indeed) - base
        elapsed = datetime.datetime.now() - start
        remaining = total - x
        est_pages = remaining/10
        
        
        print 'Added ', new, ' jobs-- scraped ',num_listings,' of ', total, ' listings in ', elapsed, '; ', est_pages, ' pages remaining'
        
        time.sleep(0.5)
            
    finish = datetime.datetime.now()
    now = finish.strftime("%Y-%m-%d %H:%M:%S")
    print 'Finish time: ',now

    elapsed = finish-start
    print 'Elapsed: ',elapsed
    indeed = pd.DataFrame(indeed)
    indeed.to_csv('/Users/jennydoyle/Desktop/dsi/DC-DSI4/projects/03-Project/indeed/'+now+'.csv',sep=',', encoding='utf-8')
    return indeed

