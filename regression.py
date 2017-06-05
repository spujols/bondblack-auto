#This script will serve several purposes as of now it includes:
#Extracting every id from portal and saving it to a .csv file called "customer_ids"
#Testing redirect on login (pointing to every url in portal then testing if it goes there after login in, including sub tabs).
from splinter import Browser
import csv
import datetime
import random
import os.path
import re
from random import randint
import base64
from time import sleep
import pandas as pd

def redirect_login():
#     orders()
#     cancellations()
#     drafts()
#     customers()
#     membership_requests()
#     dashboard()
#     admins()
#     file_exports()
#     reporting()
#     samples()
#     create()
    
    #Customers Sub tabs
    id()
    basic_info()
    onboarding()
    addresses()
    messages()
    occasions()
    charges() 
    
    
def orders():
    with Browser ('chrome',incognito=True, fullscreen=False) as browser:
        url='https://dev-bondblack.bondco.io/portal/orders'
        browser.visit(url)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password', base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        #After logging user must be taken to Orders section
        url1=browser.url
        if url1==url:
            print "User successfully redirected to Orders section"
        
        sleep(2)
def cancellations():
    with Browser ('chrome',incognito=True, fullscreen=False) as browser:
        url='https://dev-bondblack.bondco.io/portal/orders/cancellations'
        browser.visit(url)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password', base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        #After logging user must be taken to Cancellations section
        url1=browser.url
        if url1==url:
            print "User successfully redirected to Cancellations section"
        sleep(2)

def drafts():
    with Browser ('chrome',incognito=True, fullscreen=False) as browser:
        url='https://dev-bondblack.bondco.io/portal/orders/drafts'
        browser.visit(url)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password', base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        #After logging user must be taken to Drafts section
        url1=browser.url
        if url1==url:
            print "User successfully redirected to Drafts section"
        sleep(2)


def customers():
    with Browser ('chrome',incognito=True, fullscreen=False) as browser:
        url='https://dev-bondblack.bondco.io/portal/customers'
        browser.visit(url)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        #After logging user must be taken to Customers section
        url1=browser.url
        if url1==url:
            print "User successfully redirected to Customers section"
        sleep(2)

def membership_requests():
    with Browser ('chrome',incognito=True, fullscreen=False) as browser:
        url='https://dev-bondblack.bondco.io/portal/membership_requests'
        browser.visit(url)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        #After logging user must be taken to Membership Request section
        url1=browser.url
        if url1==url:
            print "User successfully redirected to Membership Request section"
        sleep(2)


def dashboard():
    with Browser ('chrome',incognito=True, fullscreen=False) as browser:
        url='https://dev-bondblack.bondco.io/portal/dashboard'
        browser.visit(url)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        #After logging user must be taken to Dashboard section
        url1=browser.url
        if url1==url:
            print "User successfully redirected to Dashboard section"
        sleep(2)

def admins():
    with Browser ('chrome',incognito=True, fullscreen=False) as browser:
        url='https://dev-bondblack.bondco.io/portal/admins'
        browser.visit(url)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        #After logging user must be taken to Admins section
        url1=browser.url
        if url1==url:
            print "User successfully redirected to Admins section"
        sleep(2)


def file_exports():
    with Browser ('chrome',incognito=True, fullscreen=False) as browser:
        url='https://dev-bondblack.bondco.io/portal/file-exports'
        browser.visit(url)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        #After logging user must be taken to File Exports section
        url1=browser.url
        if url1==url:
            print "User successfully redirected to File Exports section"
        sleep(2)
        
def reporting():
    with Browser ('chrome',incognito=True, fullscreen=False) as browser:
        url='https://dev-bondblack.bondco.io/portal/reporting'
        browser.visit(url)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        #After logging user must be taken to Reporting section
        url1=browser.url
        if url1==url:
            print "User successfully redirected to Reporting section"
        sleep(2)

def samples():
    with Browser ('chrome',incognito=True, fullscreen=False) as browser:
        url='https://dev-bondblack.bondco.io/portal/samples'
        browser.visit(url)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        #After logging user must be taken to Samples section
        url1=browser.url
        if url1==url:
            print "User successfully redirected to Samples section"
        sleep(2)



def create():
    with Browser ('chrome',incognito=True, fullscreen=False) as browser:
        url='https://dev-bondblack.bondco.io/portal/samples/create'
        browser.visit(url)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        #After logging user must be taken to Sample Creation section
        url1=browser.url
        if url1==url:
            print "User successfully redirected to Samples Creation section"
        sleep(2)




#Getting Customers Id 
def id():
    with Browser ('chrome', incognito=True, fullscreen=False) as browser:
        url='http://dev-bondblack.bondco.io/portal/customers'
        browser.visit(url)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        
        usrid=browser.find_by_tag('tbody')
        usrid2=usrid.html
        #usrid1=re.findall ('customer.id=([a-z0-9_]{10})">.*?', usrid2)
        usrid1=re.findall ('customer.id=(\S.*?)">', usrid2)#Extracting Customer Id
        #print usrid2
        #print usrid1# List of all current Ids (Each id correspond to existing customers in portal)
        rndid=random.choice(usrid1)
        #print 'Id to use is',rndid
        url22='http://dev-bondblack.bondco.io/portal/customer?id='+rndid
        browser.visit(url22)
        sleep(1)
        stat=browser.find_by_name('status').value
        #print stat
        if stat=='Access granted':
            nam1=browser.find_by_tag('h3').value
            nam=nam1[9:-15]
            print 'Customer Name is',nam
        else:
            nam1=browser.find_by_tag('h3').value
            nam=nam1[9:]
            print 'Customer Name is',nam
        sleep(2)
        

        now = datetime.datetime.now()# Variable for timestamp
        
        #Adding Headers to .CSV file
        usrid_exist = os.path.isfile('customers_ids.csv')
        
        if not usrid_exist:#Creating .csv file if it doesnt exist
            with open('customers_ids.csv', 'wb') as ids:

                fieldnames = ['#', 'user_id','customer_name','date_added']
                writer = csv.DictWriter(ids, fieldnames=fieldnames)
                writer.writeheader()
    
            # Counting Ids for .CSV list

        with open('customers_ids.csv', "r") as f:
            count = 0
            rdcsv1 = open('customers_ids.csv')
            rdcsv2 = rdcsv1.read()
            reader = csv.reader(f, delimiter=",")
            data = list(reader)
            row_count = len(data)-1
            for line in rdcsv2:
                count = row_count + 1    

        #Adding data to existing .csv
        with open('customers_ids.csv', "a") as ids:
            fieldnames = ['#', 'user_id','customer_name','date_added']
            writer = csv.DictWriter(ids, fieldnames=fieldnames)                
            writer.writerow({'#': count, 'user_id': rndid,'customer_name': nam,'date_added': now.strftime("%Y-%m-%d %H:%M")})
        
    #quit()


#Going to customers sub tab        
        
        
def basic_info():
    with Browser ('chrome', incognito=True, fullscreen=False) as browser: 
        #Storing content of User Id column from Csv file
        
        df = pd.read_csv('customers_ids.csv')
        usrid_column = df.user_id #you can also use df['column_name']
        #print usrid_column # Use to view content of .csv column listed and counted
        rndusrid=random.choice(usrid_column)
        #print rndusrid   

        #Going into url with for Random user id   
        url='http://dev-bondblack.bondco.io/portal/customer/basic-info?id='+rndusrid
        print 'Full URL is',url
        browser.visit(url)
        sleep(1)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        sleep(2)
        stat=browser.find_by_name('status').value
        #print stat
        if stat=='Access granted':
            nam1=browser.find_by_tag('h3').value
            nam=nam1[9:-15]
            print 'Customer Name is',nam
        else:
            nam1=browser.find_by_tag('h3').value
            nam=nam1[9:]
            print 'Customer Name is',nam
        
        #Looking for specific tag to then check for user location and print it
        tagpres2=browser.find_by_tag('ul')
        tagpres1=tagpres2.html
        #print tagpres1
        #activ=re.findall('class="(active)">',tagpres1)
        #print activ
        activ=re.findall('active">(\s{9}.*?)</a>',tagpres1)
        activ1=activ[0]
        
        actstr=str(activ1)
        section1=re.findall('role="tab">(\D*)',actstr)
        #print actstr
        #print section1[0]
        section=section1[0]
        print 'User was successfully redirected to section',section
        #print tagpres1
        sleep(2)
        

def onboarding():
    with Browser ('chrome', incognito=True, fullscreen=False) as browser: 
        #Storing content of User Id column from Csv file
        df = pd.read_csv('customers_ids.csv')
        usrid_column = df.user_id #you can also use df['column_name']
        #print usrid_column # Use to view content of .csv column listed and counted
        rndusrid=random.choice(usrid_column)
        
        url='http://dev-bondblack.bondco.io/portal/customer/onboarding?id='+rndusrid
        print 'Full URL is',url
        browser.visit(url)
        sleep(1)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        sleep(2)
        delbtn=browser.is_element_visible_by_xpath("html/body/div[4]/header/h3/a")
        #print delbtn
        if delbtn == True:

            nam1=browser.find_by_tag('h3').value
            nam=nam1[9:-15]
            print 'Customer Name is',nam
        else:
            nam1=browser.find_by_tag('h3').value
            nam=nam1[9:]
            print 'Customer Name is',nam
            
         #Looking for specific tag to then check for user location and print it
        tagpres2=browser.find_by_tag('ul')
        tagpres1=tagpres2.html
        #print tagpres1
        #activ=re.findall('class="(active)">',tagpres1)
        #print activ
        activ=re.findall('active">(\s{9}.*?)</a>',tagpres1)
        activ1=activ[0]
        
        actstr=str(activ1)
        section1=re.findall('role="tab">(\D*)',actstr)
        #print actstr
        #print section1[0]
        section=section1[0]
        print 'User was successfully redirected to section',section
        #print tagpres1
        sleep(2)
  
def addresses():
    with Browser ('chrome', incognito=True, fullscreen=False) as browser: 
        #Storing content of User Id column from Csv file
        df = pd.read_csv('customers_ids.csv')
        usrid_column = df.user_id #you can also use df['column_name']
        #print usrid_column # Use to view content of .csv column listed and counted
        rndusrid=random.choice(usrid_column)
        
        url='http://dev-bondblack.bondco.io/portal/customer/addresses?id='+rndusrid
        print 'Full URL is',url
        browser.visit(url)
        sleep(1)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        sleep(2)
        delbtn=browser.is_element_visible_by_xpath("html/body/div[4]/header/h3/a")
        #print delbtn
        if delbtn == True:

            nam1=browser.find_by_tag('h3').value
            nam=nam1[9:-15]
            print 'Customer Name is',nam
        else:
            nam1=browser.find_by_tag('h3').value
            nam=nam1[9:]
            print 'Customer Name is',nam
         #Looking for specific tag to then check for user location and print it
        tagpres2=browser.find_by_tag('ul')
        tagpres1=tagpres2.html
        #print tagpres1
        #activ=re.findall('class="(active)">',tagpres1)
        #print activ
        activ=re.findall('active">(\s{9}.*?)</a>',tagpres1)
        activ1=activ[0]
        
        actstr=str(activ1)
        section1=re.findall('role="tab">(\D*)',actstr)
        #print actstr
        #print section1[0]
        section=section1[0]
        print 'User was successfully redirected to section',section
        #print tagpres1
        sleep(2)
        
def messages():    
    with Browser ('chrome', incognito=True, fullscreen=False) as browser: 
        #Storing content of User Id column from Csv file
        df = pd.read_csv('customers_ids.csv')
        usrid_column = df.user_id #you can also use df['column_name']
        #print usrid_column # Use to view content of .csv column listed and counted
        rndusrid=random.choice(usrid_column)
        
        url='http://dev-bondblack.bondco.io/portal/customer/messages?id='+rndusrid
        print 'Full URL is',url
        browser.visit(url)
        sleep(1)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        
        sleep(2)
        delbtn=browser.is_element_visible_by_xpath("html/body/div[4]/header/h3/a")
        #print delbtn
        if delbtn == True:

            nam1=browser.find_by_tag('h3').value
            nam=nam1[9:-15]
            print 'Customer Name is',nam
        else:
            nam1=browser.find_by_tag('h3').value
            nam=nam1[9:]
            print 'Customer Name is',nam
         #Looking for specific tag to then check for user location and print it
        tagpres2=browser.find_by_tag('ul')
        tagpres1=tagpres2.html
        #print tagpres1
        #activ=re.findall('class="(active)">',tagpres1)
        #print activ
        activ=re.findall('active">(\s{9}.*?)</a>',tagpres1)
        activ1=activ[0]
        
        actstr=str(activ1)
        section1=re.findall('role="tab">(\D*)',actstr)
        #print actstr
        #print section1[0]
        section=section1[0]
        print 'User was successfully redirected to section',section
        #print tagpres1
        sleep(2)
        
def occasions():
    with Browser ('chrome', incognito=True, fullscreen=False) as browser: 
        #Storing content of User Id column from Csv file
        df = pd.read_csv('customers_ids.csv')
        usrid_column = df.user_id #you can also use df['column_name']
        #print usrid_column # Use to view content of .csv column listed and counted
        rndusrid=random.choice(usrid_column)
        
        url='http://dev-bondblack.bondco.io/portal/customer/occasions?id='+rndusrid
        print 'Full URL is',url
        browser.visit(url)
        sleep(1)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        sleep(2)
        delbtn=browser.is_element_visible_by_xpath("html/body/div[4]/header/h3/a")
        #print delbtn
        if delbtn == True:

            nam1=browser.find_by_tag('h3').value
            nam=nam1[9:-15]
            print 'Customer Name is',nam
        else:
            nam1=browser.find_by_tag('h3').value
            nam=nam1[9:]
            print 'Customer Name is',nam
         #Looking for specific tag to then check for user location and print it
        tagpres2=browser.find_by_tag('ul')
        tagpres1=tagpres2.html
        #print tagpres1
        #activ=re.findall('class="(active)">',tagpres1)
        #print activ
        activ=re.findall('active">(\s{9}.*?)</a>',tagpres1)
        activ1=activ[0]
        
        actstr=str(activ1)
        section1=re.findall('role="tab">(\D*)',actstr)
        #print actstr
        #print section1[0]
        section=section1[0]
        print 'User was successfully redirected to section',section
        #print tagpres1
        sleep(2)

def charges():   
    with Browser ('chrome', incognito=True, fullscreen=False) as browser: 
        #Storing content of User Id column from Csv file
        df = pd.read_csv('customers_ids.csv')
        usrid_column = df.user_id #you can also use df['column_name']
        #print usrid_column # Use to view content of .csv column listed and counted
        rndusrid=random.choice(usrid_column)
        
        url='http://dev-bondblack.bondco.io/portal/customer/charges?id='+rndusrid
        print 'Full URL is',url
        browser.visit(url)
        sleep(1)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password',base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        sleep(2)
        delbtn=browser.is_element_visible_by_xpath("html/body/div[4]/header/h3/a")
        #print delbtn
        if delbtn == True:

            nam1=browser.find_by_tag('h3').value
            nam=nam1[9:-15]
            print 'Customer Name is',nam
        else:
            nam1=browser.find_by_tag('h3').value
            nam=nam1[9:]
            print 'Customer Name is',nam
         #Looking for specific tag to then check for user location and print it
        tagpres2=browser.find_by_tag('ul')
        tagpres1=tagpres2.html
        #print tagpres1
        #activ=re.findall('class="(active)">',tagpres1)
        #print activ
        activ=re.findall('active">(\s{9}.*?)</a>',tagpres1)
        activ1=activ[0]
        
        actstr=str(activ1)
        section1=re.findall('role="tab">(\D*)',actstr)
        #print actstr
        #print section1[0]
        section=section1[0]
        print 'User was successfully redirected to section',section
        #print tagpres1
        sleep(2)

#     onboarding() # id function must be enabled for this one to run
#     addresses() # d function must be enabled for this one to run
#     messages() # id function must be enabled for this one to run
#     occasions() # id function must be enabled for this one to run
#     charges() # id function must be enabled for this one to run   
        
        
        
redirect_login()