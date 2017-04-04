#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 14:49:53 2017

@author: jennydoyle
"""

#    # save content of URL to variable page
    url = "http://www.indeed.com/jobs?q=data+scientist+%2420%2C000&start="
    x=0
    url_start = url+str(x) 
    page = requests.get(url_start).content
    page = BeautifulSoup(page)

    jobs = []
    for tag in page.find_all('a', title=True, attrs={'data-tn-element':'jobTitle'}):
        print tag['title']
#    

    
def numbers_commas_to_int(string):
    import locale # given a string of a number with commas, convert to float
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') #for american comma notation
    # if european comma notation needed, change 2nd parameter to 'fr_FR'
    num = int(locale.atof(string))
    return int(num)

def get_location(webpage):
    locations = []
    for tag in webpage.find_all('span', attrs={'class':'location'}):
        locations.append(tag.text)
    
def get_company(webpage):
    companies = []
    for tag in webpage.find_all('span', attrs={'class':'company'}):
        companies.append(tag.text)

def get_job(webpage):
    jobs = []
    for tag in webpage.find_all('a', title=True, attrs={'data-tn-element':'jobTitle'}):
        jobs.append(tag['title'])
    
def get_salary(webpage):
    salaries = []
    salary1 = webpage.find('td').find('nobr')
    salary2 = webpage.div.div.div
    if type(salary1)=='NoneType':
        salaries.append('None')
    else:
        salaries.append(salary)
    
salaries = []
count = 0
for listing in page.find_all('div',attrs={'class':['row  result']}): #,'  row  result','row sjlast result','lastRow  row  result']}):
     count+=1
     print count
    
    
    
    
    if type( listing.find('td').find('nobr') ) == 'NoneType'
    
    print listing.find('td').find('nobr')
    print listing.find('div').find('div').find('div')
    
    salary1 = listing.find('td').find('nobr')
    
    salary2 = listing.find('div').find('div')
    
    if type(salary1)!='NoneType':
        salaries.append(salary1)
    elif type(salary2) != 'NoneType':
        salaries.append(salary2)
    else:
        salaries.append('None')
    



def get_description(webpage):
    descriptions = []
    for description in webpage.find_all('span', attrs={'itemprop':"description"}):
        descriptions.append(description.text.strip('\n'))


def scrape_indeed():
    import requests
    from bs4 import BeautifulSoup
    
    # save content of URL to variable page
    url = "http://www.indeed.com/jobs?q=data+scientist+%2420%2C000&start="
    x=0
    url_start = url+str(x) # if we set the start variable in the URL to 0 to begin with, it will first pull up results 1-10
    
    page = requests.get(url_start).content
    page = BeautifulSoup(page)
        

    # create an empty list for each column in our master job listings dataframe
    # full job postings will match up by index across lists 
    job_postings=[]

    # start at the first page of results and record the total number of results
    # this will be used to help us flip through all of the pages of results
    # the URL format uses start=x where x is a result number (instead of page number)
    for results in page.find_all('div', attrs={'id':'searchCount'}):
        count = str(results.text).split()    # take the full line that says 'Jobs x to y of z' and turn into a list
        total = count[len(count)-1]          # set total to z, the total number o[f results
        total = numbers_commas_to_int(total) # since there are commas if the number > 999, this function will deal with that and convert to int
    x = 0 # if we set the start variable in the URL to 0 to begin with, it will first pull up results 1-10
    while x <= total:
        url_new_page = url + str(x)
        page = requests.get(url_new_page).content
        page = BeautifulSoup(page)
        
        for listing in page.find_all('div',attrs={'class':['row  result','  row  result','row sjlast result','lastRow  row  result']}):
        
            get_job(listing)         # put all job titles for each posting on current results page into job list
            print 'jobs = ',len(jobs)
            get_company(listing)     # put all companies for each posting on current results page into companies list
            print 'companies = ',len(companies)
            get_location(listing)    # put all locations for each posting on current results page into locations list
            print 'locations = ',len(locations)
            get_salary(listing)      # put all salaries for each posting on current results page into salaries list
            print 'salaries = ',len(salaries)
            get_description(listing) # put all descriptions for each posting on current results page into descriptions list
            print 'descriptions = ',len(descriptions)
                           
#            x += 10               # increase x by 10 for the next loop
            y = x + 5             # for some reason there are 15 listings onth e pages even though it says 10
            if not (len(jobs) == y & len(companies) == y & len(locations) == y & len(salaries) == y & len(descriptions) == y ):
                print 'Error: not all attributes of each job posting for results ', str(x-10),' - ', str(x), 'have been recorded. Process aborted.'
                break
    
            
            else:
                
                for i in range(0, 10):
                    row = []
                    for each in (jobs, locations, companies, salaries, descriptions):
                        row.append(each[i])
                    job_postings.append(row)
