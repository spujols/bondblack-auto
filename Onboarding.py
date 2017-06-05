#This script will cover the whole onboarding process from the invitation request to the hw selection, note header text  
# Payment info population and completion. Note: Signature upload is not included yet due to limitations with site upload tool.
from splinter import Browser
import csv
import datetime
import random
import os.path
import re
from random import randint
import base64

from time import sleep

def custonbd():
    #Functions to handle groups of users
    reqinvw()
    grtaccf()
    onbdcustfct()

count=2#By Modifying this number that specified number of user will be created, granted access and on-boarded.
def reqinvw():
    nwusr=0
    #count=2
    while nwusr<count:
        nwusr+=1
        reqinv()
        print "Request User invitation completed"
    print "A total of",nwusr,"users created"


def grtaccf():
    accgrus=0
    #count=2
    while accgrus<count:
        accgrus+=1
        grtacc()
        print "Access Granted scenario completed"
    print "A total of",accgrus,"users were granted access"


    #Standalone Functions
    #reqinv  #Activate this function to run Request invitation once.
    #grtacc() #Activate this function to run Grant Access once.
    #obdcust() #Activate this function to run Customer Onboarding once.

def onbdcustfct():
    csttobd=0
    while csttobd<count:
        csttobd+=1
        obdcust()
        print "User On-boarding scenario completed"
    print "A total of",csttobd,"users were successfully on-boarded"



def reqinv():
    with Browser ('chrome', incognito=True, fullscreen=True) as browser:
        url='http://dev-bondblack.bondco.io'
        browser.visit(url)
        sleep(1)
        rqtinv=browser.is_element_present_by_xpath(".//*[@id='container-nav']/div/div/ul/li[5]/a", wait_time=1)
        if rqtinv==True:
            print "Request invitation button found"

        browser.find_by_xpath(".//*[@id='container-nav']/div/div/ul/li[5]/a").click()
        sleep(1)

        #Reading Name list from csv file to pick random
        with open('names.csv', "r") as fname:
            lstnam=list()
            for n in fname:
                lstnam.append(n)
            rndnam=random.choice(lstnam)
            #print rndnam
        #Reading Job list from csv file to pick random
        with open('jobs.csv',"r") as jobs:
            lstjb=list()
            for j in jobs:
                lstjb.append(j)
            rndjb=random.choice(lstjb)
            #print rndjb
        #Generating a random number from 1 till 999 for the email
        emno1=randint(1,999)
        emno=str(emno1)#converting random number to string to be added to email.
        
        #print emailnstr
        
        email=base64.b64decode('c2lnZnJpZG8ucHVqb2xz')+"+"+emno+'@bond.co'
        print "Email",email,"will be used."

        #Filling Out Invite
        invhdr=browser.is_text_present('Please request access here!',wait_time=1)
        if invhdr==True:
            print "Request access header found. Proceeding to complete form"
        print "Name picked: ",rndnam,"Job: ",rndjb,"And Email: ",email
        print "Filling out form..."
        browser.fill('name',rndnam) #Random name out of a list of 1k
        browser.fill('company','Bond')
        browser.fill('title',rndjb)#Random job out of a list of .. a lot
        browser.fill('email',email)
        invftr=browser.is_text_present('No payment required to request an invitation', wait_time=1)
        if invftr==True:
            print "Footer msg: No payment required to request an invitation, found."
        print"Submitting Access Request form"
        browser.find_by_xpath(".//*[@id='request-invite-form']/div[5]/button").click()#clicking submit button
        sleep(1)
        frmscs=browser.is_element_present_by_xpath(".//*[@id='request-invite-form-success']", wait_time=1)
        if frmscs==True:
            print "Form submitted successfully. 'Thanks. We'll be in touch.' message displayed."



#reqinv() #Function to request access


def grtacc():
    with Browser ('chrome', incognito=True, fullscreen=True) as browser:
        url='http://dev-bondblack.bondco.io/portal'
        browser.visit(url)
        sleep(1)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password', base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        sleep(2)
        print "Logged in successfully"
        print "Looking for user to grant access"
        url1='http://dev-bondblack.bondco.io/portal/membership_requests'
        browser.visit(url1)
        sleep(1)

        #Looking for email that requested access

        membreqtpg=browser.find_by_tag('tbody')
        membreqtpg1=membreqtpg.html
        #print membreqtpg1
        usremail=re.findall('(sigfrido.pujols.*?@bond.co)',membreqtpg1)
        sleep(1)
        usrmail=usremail[0]
        print "Access will be granted to",usrmail


        #TESTING A THEORY (Worked as expected) Number 5 in this example indicated that code should click button no.5 called Grant access
        #browser.find_link_by_text('Grant Access')[5].click()
        #sleep(4)
        #quit()

        #Granting Access
        browser.find_link_by_text('Grant Access').click()
        sleep(1)
        #grtaccmd=browser.find_by_id('grant-access-modal')
        grtaccmd=browser.html
        grtaccmd1=re.findall('grant-access-email">(.*?)</span>', grtaccmd)
        grtaccm=grtaccmd1[0]
        print "User found in modal pop-up is",grtaccm
        #print usrmail

        if usrmail==grtaccm:
            browser.fill('discount','99')
            sleep(1)
            browser.find_by_xpath(".//*[@id='grant-access-form']/div[2]/button[2]").click()#Clicking grant access button from modal to finish giving access ot user.
            print "Access Granted with 99% discount"
            sleep(2)

        if usrmail!=grtaccm:
            print "User not found"
            sleep(1)
            browser.find_by_xpath(".//*[@id='grant-access-form']/div[2]/button[1]").click()#Clicking close button
            ####continue with new while for number of grant access to be selected
            sleep(2)
            n=1
            while n<1000:
                print "Looking for user",usrmail,"to grant access..."
                print "Attempt #",n
                sleep(1)
                browser.find_link_by_text('Grant Access')[n].click()
                sleep(1)
                grtaccmd=browser.html
                grtaccmd1=re.findall('grant-access-email">(.*?)</span>', grtaccmd)
                grtaccm=grtaccmd1[0]
                if usrmail==grtaccm:
                    browser.fill('discount','99')
                    sleep(2)
                    browser.find_by_xpath(".//*[@id='grant-access-form']/div[2]/button[2]").click()#Clicking grant access button from modal to finish giving access ot user.
                    print "Access Granted to",grtaccm,"with 99% discount"
                    break
                else:
                    n=n+1
                    browser.find_by_xpath(".//*[@id='grant-access-form']/div[2]/button[1]").click()#Clicking close button
                    sleep(1)
            sleep(2)
#grtacc()# Function to grant access to requested email

def obdcust():
    with Browser ('chrome', incognito=True, fullscreen=True) as browser:
        url='http://dev-bondblack.bondco.io/portal'
        browser.visit(url)
        sleep(1)
        browser.fill('email',base64.b64decode("c2lnZnJpZG8ucHVqb2xzQGJvbmQuY28="))
        browser.fill('password', base64.b64decode("RGFzaGJvYXJkMQ=="))
        browser.find_by_xpath("html/body/div[2]/div[2]/button").click()
        sleep(2)
        print "Logged in successfully"
        url2='http://dev-bondblack.bondco.io/portal/customers?email=sigfrido&status=Access%20granted'
        browser.visit(url2)
        sleep(1)
        browser.find_by_xpath(".//*[@id='customers_page']/table/tbody/tr[1]/td[1]/a").click()#clicking on any user created by me
        sleep(2)
        usernm=browser.find_by_tag('h3').text
        #print usernm
        usernam=re.findall('Customer:(.*?)   Delete Customer', usernm)
        custname=usernam[0]
        email=browser.find_by_id('emailInput').value #extracting user email
        email1=str(email)
        #email1=re.findall('value="(.*?)" data',email)
        print 'Customer name is',custname
        print 'Customer email is',email1
        #Extracting Onboarding URL
        obdurl=browser.find_by_tag('body')
        obdurl1=obdurl.html
        #print obdurl1
        obdurl2=re.findall('(/onboarding/.*?)" target',obdurl1)
        obdlink=obdurl2[0]
        print 'Onboarding URL is',obdlink

        #########################################################
        #Going to Onboarding Bond site for this particular customer
        bburl='http://dev-bondblack.bondco.io'
        cstonbd=bburl+obdlink
        print 'Full url is',cstonbd
        browser.visit(cstonbd)
        sleep(3)
        sttnsct=browser.url
        print "Currently in",sttnsct[-10:],"section of the Onboarding process"

        #Choose Stationery (Script will test Hand-engraved stationery scenario)
        onbp=browser.find_by_tag('h3').value
        print "The total price to pay will be",onbp



        browser.find_by_xpath("html/body/div[1]/div[2]/section[1]/div/div[2]/div[1]/div[2]/button").click()
        csttexthd=browser.is_element_present_by_text('Customize your stationery', wait_time=1)
        if csttexthd==True:
            print "Customize your stationery header present"

        #Choosing Paper color
        sleep(2)
        colorslst=["html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[1]/div/div[1]/label"#White
                ,\
        "html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[1]/div/div[2]/label"]#Beige

        colorsdic={"html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[1]/div/div[1]/label":'White'#White
                ,\
        "html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[1]/div/div[2]/label":'Beige'}#Beige
        #print colors
        rndppcl=random.choice(colorslst)

        browser.find_by_xpath(rndppcl).check()
        print "Paper Color selected is",colorsdic[rndppcl]

        sleep(1)
        browser.fill('headerText',custname)
        #Choosing Header Font colors (Black, Navy, Green...etc )

        sleep(1)
        hdtxtcld={"html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[3]/div/div[1]/label":'Black',\
        "html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[3]/div/div[2]/label":'Navy',\
        "html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[3]/div/div[3]/label":'Olive-Green',\
        "html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[3]/div/div[4]/label":'Gold',\
        "html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[3]/div/div[5]/label":'Red',\
        "html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[3]/div/div[6]/label":'Gray'}
        sleep(1)
        txtcont=0
        hdtxtcll=list()
        n=0
        while txtcont<len(hdtxtcld):
            hdtxtcll.append(hdtxtcld.keys()[n])
            txtcont=txtcont+1
            n=n+1

        rndhdtxcl=random.choice(hdtxtcll)
        print "Header Text Color selected is",hdtxtcld[rndhdtxcl]
        #Selecting Random Header Text Color
        browser.find_by_xpath(rndhdtxcl).click()
        sleep(1)

        htxtfntd={"html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[4]/div/label[1]/span":'Shaded Antique Roman',\
        "html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[4]/div/label[2]/span":'Italian Script',\
        "html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[4]/div/label[3]/span":'Medium Roman',\
        "html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[4]/div/label[4]/span":'Copperplate',\
        "html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[1]/div[1]/div[4]/div/label[5]/span":'Gothic Medium'}

        cont=0
        n=0
        htxtfnl=list()
        while cont<len(htxtfntd):
            htxtfnl.append(htxtfntd.keys()[n])
            cont=cont+1
            n=n+1
        #print htxtfnl
        rdhtxtfnt=random.choice(htxtfnl)

        print "Header Text Font selected",htxtfntd[rdhtxtfnt]
        sleep(1)
        #Selecting Random Header Text Font
        browser.find_by_xpath(rdhtxtfnt).click()
        sleep(1)
        #Proceeding to next page
        browser.find_by_xpath("html/body/div[1]/div[2]/section[2]/div/div[2]/form/div[3]/div/button").click()
        sleep(1)
        hwsct=browser.url
        print "Currently in",hwsct[-11:],"section of the onboarding process."

        #Bond House Signature+Your Signature
        browser.find_by_xpath("html/body/div[1]/div[2]/section[1]/div/div[2]/div[1]/div[2]/button").click()
        print "Bond House Signature + Your Signature selected"
        sleep(1)
        #Customize Your Handwriting Style
        #Add a randon var to select Print or Cursive
        #Add a random var to select Loose or Neat


        #Writing from dropdown (Print or Cursive)
        wrt={"html/body/div[1]/div[2]/section[2]/div/div/form/div[1]/div/div[1]/label/div[1]/ul/li[1]/a":'Print',\
        "html/body/div[1]/div[2]/section[2]/div/div/form/div[1]/div/div[1]/label/div[1]/ul/li[2]/a":'Cursive'}

        #Creating a list to pick the Writing
        cont=0
        n=0
        csthws=list()
        while cont<len(wrt):
            csthws.append(wrt.keys()[n])
            cont=cont+1
            n=n+1
        #print csthws

        #Style from dropdown (Loose or Neat)
        styl={"html/body/div[1]/div[2]/section[2]/div/div/form/div[1]/div/div[1]/label/div[2]/ul/li[1]/a":'Loose',\
        "html/body/div[1]/div[2]/section[2]/div/div/form/div[1]/div/div[1]/label/div[2]/ul/li[2]/a":'Neat'}

        #Creating a list to pick the Style
        cont=0
        n=0
        csthws1=list()
        while cont<len(styl):
            csthws1.append(styl.keys()[n])
            cont=cont+1
            n=n+1

        #print csthws1

        #Selecting Writing Randomly
        rndwrt=random.choice(csthws)

        #Selecting Style randomly
        rndstyl=random.choice(csthws1)
        #print rndstyl
        #print styl[rndstyl]
        sleep(1)


        browser.find_by_xpath("html/body/div[1]/div[2]/section[2]/div/div/form/div[1]/div/div[1]/label/div[1]/span/span").click()
        writ=browser.find_by_xpath(rndwrt).first
        writ.click()
                            #html/body/div[1]/div[2]/section[2]/div/div/form/div[1]/div/div[1]/label/div[1]
        sleep(1)
        browser.find_by_xpath("html/body/div[1]/div[2]/section[2]/div/div/form/div[1]/div/div[1]/label/div[2]/span/span").click()
        styl1=browser.find_by_xpath(rndstyl).first
        styl1.click()

        print "Customize your Handwriting style: I write",wrt[rndwrt],'and my style is',styl[rndstyl]

        #Handwriting Style
        hwstb=browser.html

        #Reg Expression to extract Handwriting List
        hwsstl=re.findall('ng-binding">(\w*?)</div></div>',hwstb)
        hwsstlx1=str(hwsstl)
        #print hwsstlx1
        hwsstlx=re.findall("u'(\w*?)'",hwsstlx1)
        print 'There is a total of',len(hwsstl),'Handwriting Styles available which are:',hwsstlx


        sleep(2)

        #Handwriting Styles Xpath List
        hwlsxp="html/body/div[1]/div[2]/section[2]/div/div/form/div[1]/div/div[2]/ul/li"
        n=1
        hwlsxp1ls=list()
        while n<=len(hwsstl):

            hwlsxp1=hwlsxp+'['+str(n)+']'
            #print hwlsxp1
            hwlsxp1ls.append(hwlsxp1)
            n=n+1
        #print hwlsxp1ls



        #Creating Dictionary to group Xpath + Handwriting styles available in page (per writing and style combo)
        hwsstll=len(hwsstl)
        cnt1=0
        my_dic1 = dict()
        while cnt1 < hwsstll:
            my_dic1[hwlsxp1ls[cnt1]] = hwsstl[cnt1]
            cnt1 = cnt1 + 1
        #print my_dic1

        #Selecting Handwriting Style
        rndhwsstl=random.choice(hwlsxp1ls)
        #print rndhwsstl
        sleep(1)
        browser.find_by_xpath(rndhwsstl).click()
        print "Handwriting Style selected is",my_dic1[rndhwsstl]


        #Add a Signature & Mark    ------ Currently not working (need new approach)
        #=======================================================================
        # sleep(1)
        # browser.find_by_xpath("html/body/div[1]/div[2]/section[2]/div/div/form/div[3]/div/div[1]/div[1]/button").click()
        #
        # #browser.find_by_xpath("html/body/div[6]/div/div[2]/div[3]/div/div[5]")
        #
        # #browser.attach_file(x,'/Bond Black/PATRICK-BATEMAN-signature-works.svg')
        # sleep(1)
        #
        # x=browser.find_by_xpath("html/body/div[4]/div/div[2]/div[3]/div/div[5]").click
        # x1=browser.find_by_text('Choose a local file')
        # browser.attach_file(x1,'/Bond Black/PATRICK-BATEMAN-signature-works.svg')
        #print "Signature Uploaded"
        #=======================================================================

        #Skipping Add signature for now
        msgsgn="If you'd rather not have your signature digitized,"
        msgsgn1=browser.is_text_present(msgsgn)
        if msgsgn1 ==True:
            print "Button clicked to not digitize signature."
        sleep(1)
        skpsgn=browser.find_by_xpath("html/body/div[1]/div[2]/section[2]/div/div/form/div[3]/div/div[3]/div/label/span[1]/strong")
        skpsgn.click()

        #Continuing Onboarding (Clicking next button)
        browser.find_by_xpath("html/body/div[1]/div[2]/section[2]/div/div/form/div[4]/div/button").click()
        print "Proceeding to Occasions page"
        sleep(1)

        #-------------------Populating Occasions page (this page is optional)---------------------------
        #Reading Occasions list from csv file to pick random
        with open('occasions.csv', "r") as foccas:
            lstocc=list()
            for n in foccas:
                lstocc.append(n)
            rndocc=random.choice(lstocc)

        browser.find_by_xpath("//INPUT[@id='occasion_title_0']").fill(rndocc)
        browser.find_by_xpath("html/body/div[1]/div[2]/section/div/form/div[1]/div/div[1]/div[2]/input").click()
        browser.find_by_xpath("html/body/div[4]")
        sleep(1)

        #Random numbers to select date on calendar
        cont=0
        mm=12
        mths=list()
        while cont<mm:
            cont=cont+1
            mths.append(cont)
        #print mths

        rndmonth=random.choice(mths)
        #print rndmonth

#         cont=0
#         dd=31
#         ds=list()
#         while cont<dd:
#             cont=cont+1
#             ds.append(cont)
        #print ds
        rndday=randint(1,30)#Selecing a random day number from 1 to 31

        #rndday=random.choice(ds)
        #print rndday

        if rndmonth==2:
            rndday=rndday-2
            if rndday<0:
                rndday=rndday+1
            #print rndday
        #print rndday


        #Selecting Month
        mths1={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June', 7:'July',8:'August',9:'September',\
        10:'October', 11:'November',12:'December'}

        print "Date selected is",mths1[rndmonth],rndday
        browser.find_by_value(rndmonth).click()
        sleep(1)




        browser.find_by_xpath("html/body/div[1]/div[2]/section/div/form/div[1]/div/div[1]/div[2]/input").click()
        sleep(1)
        #Selecting Day
        browser.find_by_text(rndday).click()


        sleep(1)

        print "Proceeding to Payments & Info Page"
        browser.find_by_xpath("html/body/div[1]/div[2]/section/div/form/div[2]/div/button").click()

        #Add your personal info & checkout - area
        #Populating phone with random number
        with open('phones.csv', "r") as fphones:
            lstphn=list()
            for n in fphones:
                lstphn.append(n)
            rndphn=random.choice(lstphn)
        sleep(1)
        browser.find_by_xpath("html/body/div[1]/div[2]/section/div/form/div[1]/div/div/input[3]").fill(rndphn)

        #-----------------------------Populating Home Return Address-----------------------------------
        sleep(1)
        with open('businesses.csv', "r") as fbusiness:
            lsbus=list()
            for n in fbusiness:
                lsbus.append(n)
            rndbus=random.choice(lsbus)#Home Return Address - Business
        print "Business selected for Home Return Address is",rndbus

        with open('streets.csv', "r") as fstreets:
            lsst=list()
            for n in fstreets:
                lsst.append(n)
            rndst=random.choice(lsst)#Home Return Address - Street
        print "Street populated",rndst

        browser.fill('business',rndbus)
        browser.fill('address_1',rndst)

        sleep(1)
        #List of States to select random state and city
        stat=['New York', 'New Jersey', 'California', 'Florida']
        ny=['New York','Syracuse', 'Buffalo', 'Rochester']
        nj=['Jersey City','Trenton', 'Hoboken', 'Paterson']
        ca=['Los Angeles','San Diego', 'Sacramento', 'Beverly Hills']
        fl=['Miami', 'Tampa', 'Naples', 'Fort Lauderdale']
        #print stat
        rndstat=random.choice(stat)
        print "State selected for Home Return Address is",rndstat
        if rndstat == 'New York':
            rndcity=random.choice(ny)
            browser.fill('city',rndcity)#City will vary depending on state selected
            print "City selected for Home Return Address is", rndcity
        if rndstat=='New Jersey':
            rndcity=random.choice(nj)
            browser.fill('city',rndcity)#City will vary depending on state selected
            print "City selected Home Return Address is", rndcity
        if rndstat=='California':
            rndcity=random.choice(ca)
            browser.fill('city',rndcity)#City will vary depending on state selected
            print "City selected Home Return Address is", rndcity
        if rndstat == 'Florida':
            rndcity=random.choice(fl)
            browser.fill('city',rndcity)#City will vary depending on state selected
            print "City selected Home Return Address is", rndcity

        browser.find_by_xpath("html/body/div[1]/div[2]/section/div/form/div[2]/div[1]/div/div[1]/div/div[1]").click()#Clicking on State dropdown
        sleep(1)
        browser.find_by_xpath("html/body/div[1]/div[2]/section/div/form/div[2]/div[1]/div/div[1]/div/div[1]/input").fill(rndstat)#Searching for state on dropdown
        sleep(1)
        browser.find_by_xpath("html/body/div[1]/div[2]/section/div/form/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/span").click() #Clicking on State

        zip1= randint (10000,99999)
        print "Zip code for Home Return Address is",zip1
        browser.fill('zip',zip1)
        sleep(1)
        # --------------------Populating Business Return Address
        #Reusing lists and processes created for Home
        rndbus1=random.choice(lsbus)#Business Return Address - Business
        browser.fill('business_business',rndbus1)
        rndst1=random.choice(lsst)
        print "Business selected for Business Return Address is",rndst1
        browser.fill('business_address_1',rndst1)
        rndstat1=random.choice(stat)
        print "State selected for Business Return Address is",rndstat1
        if rndstat1 == 'New York':
            rndcity=random.choice(ny)
            browser.fill('business_city',rndcity)#City will vary depending on state selected
            print "City selected for Business Return Address is", rndcity
        if rndstat1=='New Jersey':
            rndcity=random.choice(nj)
            browser.fill('business_city',rndcity)#City will vary depending on state selected
            print "City selected Business Return Address is", rndcity
        if rndstat1=='California':
            rndcity=random.choice(ca)
            browser.fill('business_city',rndcity)#City will vary depending on state selected
            print "City selected Business Return Address is", rndcity
        if rndstat1 == 'Florida':
            rndcity=random.choice(fl)
            browser.fill('business_city',rndcity)#City will vary depending on state selected
            print "City selected Business Return Address is", rndcity
        browser.find_by_xpath("html/body/div[1]/div[2]/section/div/form/div[2]/div[2]/div/div[1]/div/div[1]").click()
        sleep(1)
        browser.find_by_xpath("html/body/div[1]/div[2]/section/div/form/div[2]/div[2]/div/div[1]/div/div[1]/input").fill(rndstat1)
        sleep(1)
        browser.find_by_xpath("html/body/div[1]/div[2]/section/div/form/div[2]/div[2]/div/div[1]/div/div[2]/div").click()
        #html/body/div[1]/div[2]/section/div/form/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]
        zip2=randint(10000,99999)
        print "Zip selected for Business Return Address is",zip2
        browser.fill('business_zip',zip2)

        sleep(1)
        #-----------------------Populating Credit Card Info----------------------------
        cc=[4242424242424242,4012888888881881,4000056655665556,5555555555554444,5200828282828210,5105105105105100,\
            378282246310005,371449635398431]
        rndcc=random.choice(cc)
        rndcc1=str(rndcc)

        mm=randint(1,12)
        yy=randint(18,25)
        cvv=randint(111,999)
        print "Credit Card No. to use is",rndcc,"with expiration date of",mm,"/",yy
        browser.fill('cc_number', rndcc1)
        browser.fill('exp_month',mm)
        browser.fill('exp_year',yy)
        browser.fill('cc_cvc',cvv)
        print "Credit card info populated"
        sleep(1)

        disct=browser.html
        disct1=re.findall('ng-binding">(\S*?)</h1>',disct)
        print "Membershipt Price to pay is",disct1[0]
        disct2=re.findall('discount">(\S*?) off total',disct)
        print "Discount applied is of",disct2[0],"off total"
        sleep(1)
        browser.find_by_xpath("html/body/div[1]/div[2]/section/div/form/div[5]/div/div/button").click()#Clicking Pay & Finish button
        print "Pay & Finish button clicked"
        sleep(4)
        print "Proceeding to order complete page"
        blog=browser.is_element_present_by_xpath("html/body/div[1]/section[1]/div/div/div/div/div[1]",wait_time=1)
        if blog==True:
            print "Bond logo found on header"
        succ=browser.is_text_present('Your order has been submitted successfully. Thank you!')
        if succ==True:
            print "User On-boarding is now complete."
        sleep(4)


        # Variable for timestamp
        now = datetime.datetime.now()
        
        #Adding Headers to .CSV file
        msgs_exist = os.path.isfile('user_onboarded.csv')
        
        if not msgs_exist:
            with open('user_onboarded.csv', 'wb') as onbd:

                fieldnames = ['#', 'name','email','date_onboarded']
                writer = csv.DictWriter(onbd, fieldnames=fieldnames)
                writer.writeheader()
            
        # Counting Messages for .CSV list

        with open('user_onboarded.csv', "r") as onbd:
            count = 0
            rdcsv1 = open('user_onboarded.csv')
            rdcsv2 = rdcsv1.read()
            reader = csv.reader(onbd, delimiter=",")
            data = list(reader)
            row_count = len(data)-1
            for line in rdcsv2:
                count = row_count + 1                
            

        with open('user_onboarded.csv', "a") as onbd:

            fieldnames = ['#', 'name','email','date_onboarded']
          
            #writer.writeheader() #-- This would add the header to each row of the CSV file. 
            #Previously created var 'count' used in .csv file to reflect total messages
            writer = csv.DictWriter(onbd, fieldnames=fieldnames,lineterminator='\n')                
            writer.writerow({'#': count, 'name': custname,'email':email,
                             'date_onboarded': now.strftime("%Y-%m-%d %H:%M")})  
            # format for the timestamp (Year,Month,Day,Hour,Min)


custonbd()
