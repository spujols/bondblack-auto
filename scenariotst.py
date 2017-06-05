#This test script will log into BB Portal Prod to extract every Handwriting Style to date
#Then proceed to save it to a .csv file labeled handwriting
from splinter import Browser
from datetime import datetime
import base64
from time import sleep
import re
import csv
import os.path
#import datetime


#now=datetime.datetime.now()
#now=now1.strftime("%H:%M")
#later='11:30'


def scenariotst():
    #hwextrt()
    logsval()
    jobsch()
    
   
def hwextrt():
    with Browser('chrome', fullscreen=False, incognito=True) as browser:
         
        try:
            url='https://www.bondblack.com/portal/log_in'
            browser.visit(url)
            
        except:#Checking for issues accessing BB Portal.
            error1=browser.is_element_present_by_text('Page Not Found')
            if error1==True:
                print 'Page Not Found error'
            error2=browser.is_element_present_by_text('Bad Gateway')
            if error2==True:
                print "502 Error: Bad Gateway"
            error3=browser.is_element_present_by_text('Service Unavailable')
            if error3==True:
                print "503 Error: Service Unavailable"
            error4=browser.is_element_present_by_text('Gateway Timeout')
            if error4==True:
                print "504 Error: Gateway Timeout"                
            
        #Login into portal    
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password', base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        sleep(1)
        url2='https://www.bondblack.com/portal/customer/basic-info?id=Qyb3iPFZH2'
        browser.visit(url2)
        sleep(10)


        
        hwext=browser.html# Check HW Styles document from desktop
        #print hwext
        
        
        #hwext1=re.findall('<option value=.\d{1,7}.>(\D*?)</option>',hwext)
        hwext1=re.findall('<select id=.handwriting_id.(.*?)</select>',hwext)
        #print hwext1
        hwext2=str(hwext1)
        #print hwext2
        hwext3=re.findall('<option value=.\d{1,7}.>(\D*?)</option>',hwext2)
        print hwext3
        
            #Adding Headers to .CSV file
        hwss_exist = os.path.isfile('handwriting.csv')

        if not hwss_exist:#Creating .csv file if it doesnt exist
            with open('handwriting.csv', 'wb') as hws:

                fieldnames = ['#', 'handwriting style','date_extracted']
                writer = csv.DictWriter(hws, delimiter=',', lineterminator='\n',fieldnames=fieldnames)#Lineterminator helps with new line(avoids blank line in between rows)
                writer.writeheader()
        #Adding data to existing .csv
        with open('handwriting.csv', "a") as hws:
            fieldnames = ['#', 'handwriting style','date_extracted']
            writer = csv.DictWriter(hws, delimiter=',', lineterminator='\n',fieldnames=fieldnames)
            count=0
            for item in hwext3:
                    count=count+1
    #                writer.writerow({'#': count, 'handwriting style': item,'date_extracted': now.strftime("%Y-%m-%d %H:%M")})            
            
            

                
def logsval():
        with Browser ('chrome',incognito=True, fullscreen=False) as browser:
            url='http://dev-bondblack.bondco.io/portal/orders'#Going 1st to orders page to extract orders count
            #url='http://bondblack.com/portal/orders'
            browser.visit(url)
            browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
            browser.fill('password', base64.b64decode("RGFzaGJvYXJkMQ=="))
            browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
            sleep(2)
            ordersp=browser.html
            content = ordersp.encode('utf8')#solves encoding situation for unmanaged chars
            #print content
            #Looking for page amount in Orders tab
            varpagct=re.findall('var numPages = (.*?);',content)

            nopgs=varpagct[0]
            print "There is currently a total of",nopgs,'Order pages'
            #Looking for orders with status New
            try:
                newst=re.findall('>(New)</a>',content)
                newodct=len(newst)
                print 'There is currently a total of',newodct,'Orders in status New.'
            except:
                print "There are currently no orders with New status"
            #Looking for orders with status Processing
            try:  
                prost=re.findall('>(Processing)</a>',content)
                prodct=len(prost)
                print 'There is currently a total of',prodct,'Orders in Processing status.'
            except:
                print "There are currently no orders with Processing status."
            #Looking for orders in Sent Status
            try:  
                sentst=re.findall('>(Sent)</a>',content)
                sentct=len(sentst)
                print 'There is currently a total of',sentct,'Orders in Sent status.'
            except:
                print "There are currently no orders with Sent status."
            
            ordlst=list()
            ordttl=int(newodct+prodct+sentct)
            print 'There is a total of',ordttl,'Orders in BB portal (Count does not include: Scheduled, Pending Address or Cancelled orders)'
            
            #Going to Logs page
            url1='http://dev-bondblack.bondco.io/portal/jobs-log'
            browser.visit(url1)
            sleep(2)
            #Extracting Logs content
            logscntt=browser.html
            logscntt1=logscntt.encode('utf8')
            #print logscntt1
            lordttl=re.findall('<td>Report: Total Orders: (\d*?). Total',logscntt1)#Pulls number of order's total from page 
            lgordtt=int(lordttl[0])#since row will be repeated multiple times we request element 0, meaning first element from list
            #Number pulled will hold the last check of logs and therefore the alleged current total of orders.
            
            if ordttl == lgordtt:
                print "Logs order's count is accurate, matches the total number of orders in Order's page.",lgordtt,'Orders'
            else:
                print "Count mismatch, Logs count is not accurate, review issue (current number does not match Order's page count)"
            #Scenario completed
def jobsch():
    with Browser ('chrome',incognito=True, fullscreen=False) as browser:
                url='https://dev-bondblack.bondco.io/portal/jobs-log'#Going 1st to orders page to extract orders count
                #url='http://bondblack.com/portal/orders'
                browser.visit(url)
                browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
                browser.fill('password', base64.b64decode("RGFzaGJvYXJkMQ=="))
                browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
                #Logs Page content             
                logsp=browser.html
                content = logsp.encode('utf8')#solves encoding situation for unmanaged chars
                #print content
                #Looking for page amount in Orders tab
                varpagct=re.findall('var numPages = (.*?);',content)
    
                nopgs=varpagct[0]
                print "There is currently a total of",nopgs,'Logs pages'
                bdcont=browser.find_by_tag('tbody').value
                syncst=re.findall('Synch Status Orders \d+/+\d+/+\d+ (\d+.\d+.\d+)....',bdcont)#Extracting Sync status time lapse
                #print syncst
                #--------------- Checking for 5 min time lapse for Sync Order Job to run-----------------
                a=str(syncst[0])
                b=str(syncst[1])
                c=str(syncst[2])
                d=str(syncst[3])
                FMT = '%H:%M:%S'
                 
                timelapse1 = datetime.strptime(a, FMT) - datetime.strptime(b, FMT)
                timelapse2 = datetime.strptime(c, FMT) - datetime.strptime(d, FMT)
                #print timelapse1
                #print timelapse2
                x='00:08:50'
                y='00:04:00'
                timelapsec=datetime.strptime(x,FMT) - datetime.strptime(y,FMT)
                #print timelapsec
                if timelapse1>=timelapsec and timelapse2>=timelapsec:
                    print 'Sync Order Job completed. It successfully ran after 5 min time lapse'
                #print bdcont
                
                
                
scenariotst()
        
        