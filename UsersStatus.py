#Scripts goes into BB Portal Dev and extract user counts by status
#
#http://dev-bondblack.bondco.io/portal/membership_requests
# http://dev-bondblack.bondco.io/portal/customers?status=Not+set
# http://dev-bondblack.bondco.io/portal/customers?status=Access+granted
# http://dev-bondblack.bondco.io/portal/customers?status=On-boarding+complete
# http://dev-bondblack.bondco.io/portal/customers?status=Account+ready


from splinter import Browser
import csv
import datetime
import random
import os.path
import re
from time import sleep
import base64
    

def UsrStt():
    # Go to URL
        with Browser('chrome', fullscreen=False, incognito=True) as browser:
            url = "http://dev-bondblack.bondco.io/portal"
            browser.visit(url)
            browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
            browser.fill('password', base64.b64decode("RGFzaGJvYXJkMQ=="))
            lgnbtn=browser.is_element_present_by_xpath("html/body/div[2]/div[2]/button", wait_time=1)
            if lgnbtn==True:
                print "Login button found, Clicking to log in"
            lgnbtn=browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
            
            print "Proceeding to check count per user status"
            sleep(1)
            #Going to page of User with Status Access Granted
            url1='http://dev-bondblack.bondco.io/portal/customers?status=Access+granted'
            browser.visit(url1)
            sleep(1)
            #url1=browser.url
            #print url1
            
            extract1=browser.find_by_id('customers_page')
            extract=extract1.html
            #print extract
            #Finding Users with specific Status (Access Granted)
            accgrt=re.findall('<td>(Access granted*?)</td>',extract)
            
            #Looking for page amount
            pgamt1=browser.find_by_id('customers_paginator')
            pgamt2=pgamt1.html
            pgamt=re.findall('data-lp="(\d)">',pgamt2)
            try: 
                a=pgamt[-1]#Getting the last page number
            except:
                #If no more than one page exist error will appear
                print "Only one page exist for granted access user, skipping page count."
                a=1#Getting page number
            b=int(a)
            x=b+1
            #print b
            c=len(accgrt)
            d=int(c)
            #print d
            #print accgrt
            count=1
            accgrtct=list()
            #accgrtct1=list()
            while count<=x:
                try:
                    if count==1:
                        #print "Current page is #",count
                        extract1=browser.find_by_id('customers_page')
                        extract=extract1.html
                        #print extract
                        #Finding Users with specific Status (Access Granted)
                        accgrt=re.findall('<td>(Access granted*?)</td>',extract)
                        cntaccgrt=len(accgrt)
                        print "Current Page has",cntaccgrt,"Users with Access Granted Status"
                        accgrtct.append(cntaccgrt)
                        print "Total of users so far is",accgrtct
                        count=count+1
                        #browser.find_link_by_text(count).click()
                        sleep(1)
                        break
                    
                except:
                    print "More than one page exist with status Access Granted, proceeding to next page."    
                    if count >1:
                        #print "Above page 1" 
                        browser.find_link_by_text(count).click()
                        #print "Current page is #",count
                        extract2=browser.find_by_id('customers_page')
                        extract3=extract2.html
                        #print extract
                        #Finding Users with specific Status (Access Granted)
                        accgrt=re.findall('<td>(Access granted*?)</td>',extract3)
                        cntaccgrt=len(accgrt)
                        #print "Current Page has",cntaccgrt1,"Users Statuses"
                        accgrtct.append(cntaccgrt)
                        #print "Total of users so far per page is",accgrtct1
                        count=count+1
                        #browser.find_link_by_text(count).click()
                        sleep(1)
                        if count==x:
                            extract2=browser.find_by_id('customers_page')
                            extract3=extract2.html
                            #print extract
                            #Finding Users with specific Status (Access Granted)
                            accgrt=re.findall('<td>(Access granted*?)</td>',extract3)
                            cntaccgrt=len(accgrt)
                            #print "Current Page has",cntaccgrt1,"Users Statuses"
                            accgrtct.append(cntaccgrt)
                            #print "Total of users so far per page is",accgrtct1
                            break
                
            sum=0    
            for elem in accgrtct:
                sum=sum+elem
            print "Access Granted Users equal:",sum,". In",count-1,"pages",sum,"Users exist with Status Access Granted"
            

           
           #Going to page of User with Status Onboarding Complete
            url1='http://dev-bondblack.bondco.io/portal/customers?status=On-boarding+complete'
            browser.visit(url1)
            sleep(1)
        #    extract1=browser.find_by_id('customers_page')
        #   extract=extract1.html
            #print extract
            #Finding Users with specific Status (Onboarding Complete)
        #    onbdcompl=re.findall('<td>(On-boarding complete*?)</td>',extract)
            #print onbdcompl
            
            #Looking for page amount
            pgamt1=browser.find_by_id('customers_paginator')
            pgamt2=pgamt1.html
            pgamt=re.findall('data-lp="(\d)">',pgamt2)
            try: 
                a=pgamt[-1]#Getting the last page number
            except:
                print "Only 1 page exist with Onboarding Completed customers, proceeding to count..."
                a=1
            b=int(a)
            z=b+1
            #print b
            #print z
            #c=len(onbdcompl)
            #d=int(c)
            
            count=0
            onbdcomplcnt=list()
            onbdcomplcnt2=list()
            while count<z:
                if count==0:
                    #print "Current page is #",count+1
                    extract12=browser.find_by_id('customers_page')
                    extract13=extract12.html
                    #print extract
                    #Finding Users with specific Status (On-boarding Complete)
                    onbdcompl=re.findall('<td>(On-boarding complete*?)</td>',extract13)
                    cntaccgrt10=len(onbdcompl)
                    #print "Current Page has",cntaccgrt10,"Users with On-boarding complete Status"
                    onbdcomplcnt.append(cntaccgrt10)
                    #print "Total of users so far is",onbdcomplcnt
                    count=count+1
                    #browser.find_link_by_text(count).click()
                    sleep(1)
                    
                    
                else:
                    count=count+1
                    
                    #print count
                    sleep(1)
                    browser.find_link_by_text(count).click()
                   # print "Current page is #",count
                    extract12=browser.find_by_id('customers_page')
                    extract13=extract12.html
                    #print extract
                    #Finding Users with specific Status (Access Granted)
                    onbdcompl=re.findall('<td>(On-boarding complete*?)</td>',extract13)
                    #print onbdcompl
                    cntaccgrt10=len(onbdcompl)
                   # print "Current Page has",cntaccgrt10,"Users Statuses"
                    onbdcomplcnt2.append(cntaccgrt10)
                   # print "Total of users so far per page is",onbdcomplcnt2
                    #count=count+1
                    #browser.find_link_by_text(count).click()
                    sleep(1)
                    count=count+1
                    if count==z:
                        extract12=browser.find_by_id('customers_page')
                        extract13=extract12.html
                        #print extract
                        #Finding Users with specific Status (Access Granted)
                        onbdcompl=re.findall('<td>(On-boarding complete*?)</td>',extract13)
                        cntaccgrt10=len(onbdcompl)
                       # print "Current Page has",cntaccgrt10,"Users Statuses"
                        onbdcomplcnt2.append(cntaccgrt10)
                        #print "Total of users so far per page is",onbdcomplcnt2
                        break
                
            sum=0    
            for elem in onbdcomplcnt2:
                sum=sum+elem
            print "Onboarding Complete Users equal:",sum,". In",count-1,"pages",sum,"Users exist with Status Onboarding Complete"

                
                #Printing the exact amount of users with that status
                #print b*d,"Users with Status: On-Boarding Complete found"
                
            
            
            #Going to page of User with Status Account ready
            url1='http://dev-bondblack.bondco.io/portal/customers?status=Account+ready'
            browser.visit(url1)
            sleep(1)
                        
            #print accntrdy
            
            #Looking for page amount
            pgamt1=browser.find_by_id('customers_paginator')
            pgamt2=pgamt1.html
            pgamt=re.findall('data-lp="(\d)">',pgamt2)
            a=pgamt[-1]#Getting the last page number
            b=int(a)#last page number as an Int
            #print b
            #Printing the exact amount of users with that status
            
            cont=1
            acrdlst=list()
            while cont<b:
            #Finding Users with specific Status (Account Ready)
                extract1=browser.find_by_id('customers_page')
                extract=extract1.html
                accntrdy=re.findall('<td>(Account ready*?)</td>',extract)
                acrdln=len(accntrdy)
                #print acrdln
                acrdlst.append(acrdln)
                cont=cont+1
                browser.find_link_by_text(cont).click()
                #print "Current page is #",cont
                sleep(1)
                if cont==b:
                    extract1=browser.find_by_id('customers_page')
                    extract=extract1.html
                    accntrdy=re.findall('<td>(Account ready*?)</td>',extract)
                    acrdln=len(accntrdy)
                    #print acrdln
                    acrdlst.append(acrdln)
                    #cont=cont+1
                    #browser.find_link_by_text(cont).click()
                    #print "Current page is #",cont
                    sleep(1)
                    break
            
            sum=0
            for elem in acrdlst:
                sum=sum + elem
            print "Account Ready Users equal:",sum,". In",cont,"pages",sum,"Users exist with Status Account Ready"
            
            
            #Going to page of User with Status Deleted
            url1='http://dev-bondblack.bondco.io/portal/customers?status=Deleted'
            browser.visit(url1)
            sleep(1)
            
            #Looking for page amount
            pgamt1=browser.find_by_id('customers_paginator')
            pgamt2=pgamt1.html
            pgamt=re.findall('data-lp="(\d)">',pgamt2)
            a=pgamt[-1]#Getting the last page number
            b=int(a)#last page number as an Int
            #print b
            
            cont1=1
            dellst=list()
            while cont1<b:
                extract1=browser.find_by_id('customers_page')
                extract=extract1.html
                dlted=re.findall('<td>(Deleted*?)</td>',extract)
                #print dlted
                dellen=len(dlted)
                #print dellen
                dellst.append(dellen)
               # print dellst
                cont1=cont1+1
                browser.find_link_by_text(cont1).click()
                sleep(1)
                if cont1==b:
                    extract1=browser.find_by_id('customers_page')
                    extract=extract1.html
                    dlted=re.findall('<td>(Deleted*?)</td>',extract)
                    dellen=len(dlted)
                    dellst.append(dellen)
                    #print dellst
                    #cont1=cont1+1
                    #browser.find_link_by_text(cont1).click()
                #quit()
            
            sum=0
            for elem in dellst:
                sum = sum+elem
            print "Deleted Users equal:",sum,". In",cont,"pages",sum,"Users exist with Status Deleted"
            
            
            #Going to page of User with Status "Not Set"
            url1='http://dev-bondblack.bondco.io/portal/customers?status=Not+set'
            browser.visit(url1)
            sleep(1)
            
            #Looking for page amount
            pgamt1=browser.find_by_id('customers_paginator')
            pgamt2=pgamt1.html
            pgamt=re.findall('data-lp="(\d)">',pgamt2)
            a=pgamt[-1]#Getting the last page number
            b=int(a)#last page number as an Int
            #print b
            
            
            cont2=1
            ntlst=list()
            while cont2<b:
                extract1=browser.find_by_id('customers_page')
                extract=extract1.html
                notset=re.findall('<td>(Not set*?)</td>',extract)
                #print notset
                nslen=len(notset)
                #print nslen
                ntlst.append(nslen)
                #print ntlst
                cont2=cont2+1
                browser.find_link_by_text(cont2).click()
                sleep(1)
                
                if cont2==b:
                    extract1=browser.find_by_id('customers_page')
                    extract=extract1.html
                    notset=re.findall('<td>(Not set*?)</td>',extract)
                    #print notset
                    nslen=len(notset)
                    #print nslen
                    ntlst.append(nslen)
                    #cont2=cont2+1
                    #browser.find_link_by_text(cont2)
                
            sum=0
            for elem in ntlst:
                sum=sum+elem
            print "Not Set Users equal:",sum,". In",cont2,"pages",sum,"Users exist with Status Not Set"
                
                
                
            #Going to Membership request page"
            url1='http://dev-bondblack.bondco.io/portal/membership_requests'
            browser.visit(url1)
            sleep(2)  
            
            #Looking for page amount
            pgamt1=browser.find_by_id('customers_paginator')
            pgamt2=pgamt1.html
            pgamt=re.findall('data-lp="(\d)">',pgamt2)
            a=pgamt[-1]#Getting the last page number
            b=int(a)#last page number as an Int
            #print b
       
            cont3=1
            mmbrqlst=list()
            uniqidlst=list()
            
            while cont3<=b:
                
                sleep(1)
                extract1=browser.find_by_tag('tbody')
                extract=browser.html
                #print extract
                mmbrq=re.findall('>(Grant Access*?)</a>',extract)
                #print mmbrq
                mmbrqln=len(mmbrq)
                mmbrqlst.append(mmbrqln)
                #print "There are currently",mmbrqlst,"Membership Requests."
                
                unqid=re.findall('<td>([a-z0-9_]{15})</td>',extract)#Looking for a range of 15 chars consisting of numbers and letters mixed.
                unqidln=len(unqid)
                #print unqid
                uniqidlst.append(unqidln)
                #print "There are currently only",uniqidlst,"users with Unique Ids."
                sleep(1)
                cont3=cont3+1
                if cont3>b:
                    break
                browser.find_link_by_text(cont3).click()
                sleep(1)
            #Getting total of Membership request
            sum=0
            for elem in mmbrqlst:
                sum=elem+sum
            
            
            #Getting total of Unique IDs    
            sum1=0
            for elem1 in uniqidlst:
                sum1 = elem1+sum1
            
            print "Membership Requests equal:",sum,". In",b,"pages,",sum,"Users exist with Membership Request pending. And only",sum1,"have Unique Ids."
                
            quit()
            
UsrStt()            