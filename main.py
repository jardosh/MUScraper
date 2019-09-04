#! D:\python
# charset utf-8
import requests
import smtplib
from bs4 import BeautifulSoup
from datetime import datetime
from email.mime.text import MIMEText

# python 3.6.8

# add URLs that you want to monitor
sections = {
    "Examination Announcements": "http://mu.ac.in/portal/student-section/examination/",
    "Examination related circulars SH 2019": "http://mu.ac.in/portal/examination-related-circulars-sh-2019/",
    "Result of Revaluation cases": "http://mu.ac.in/portal/university-news/results-of-revaluation-cases/",
    "Circulars For University Staff":"http://mu.ac.in/portal/circular-for-permanent-employees/revised-syllabus-3/circulars-for-university-staff/",
    "Notifications": "http://mu.ac.in/portal/notification/",
    "Department Announcements":"http://mu.ac.in/portal/useful-link/department-announcements-2/"
}

def run():

    data = "<html><head></head><body>"
    recent = ""
    past = ""
    email = 0

    for title in sections:
        
        r = requests.get(sections[title])
        recent += "\n<p><b>Section: <a href=\"" + sections[title] + "\">" +  title + "</a></b><br>\n"
        past += "\n<p><b>Section: <a href=\"" + sections[title] + "\">" +  title + "</a></b><br>\n"
        thepage = r.content
        soup = BeautifulSoup(thepage, "html.parser")
        
        ulist = soup.find('ul', class_='gdl-accordion')
        if (ulist == None):
            ulist = soup.find('ul', class_="")
            
        links = ulist.find_all( "a")
        for i in links:
            url = i.get("href")
            if (url.endswith("pdf")):
                req = requests.get(url);
                date_time_obj = datetime.strptime(req.headers["Last-Modified"], '%a, %d %b %Y %H:%M:%S %Z')
                diff = datetime.utcnow() - date_time_obj
                
                if diff.days <= 1:
                    recent += "<b>Recent: " + str(date_time_obj) + "<br> <a href=\"" +url + "\">" + i.get_text() + "</a></b><br> \n"
                    email += 1
                else:
                    past += "Past: " + str(date_time_obj) + "<br> <a href=\"" + url + "\">" + i.get_text()+  "</a><br>\n"
                    break

    
    data += "<h2>Recent</h2>" + recent + "<hr>" +  "<h2>Past</h2>" + past + "</body></html>"
    if (email):
        gmail(data, email)
    else:
        print("No new notifications")

def gmail(data, email):
    
    GMAIL_SMTP_SERVER = 'smtp.gmail.com'
    GMAIL_SMTP_PORT = 587
    GMAIL_SENDER = "<add your gmail account>"
    GMAIL_APP_PASSWORD = "<add your app specific password>" # Check and generate app password here - https://myaccount.google.com/apppasswords
    RECIPIENT = GMAIL_SENDER # change this to whoever, use list if multiple
    
    
    conn = smtplib.SMTP(GMAIL_SMTP_SERVER, GMAIL_SMTP_PORT) # smtp address and port
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
    conn.login(GMAIL_SENDER, GMAIL_APP_PASSWORD)
    
    text_subtype = 'html'
 
    msg = MIMEText(data, text_subtype)
    msg['Subject']= str(email) + " New Mumbai University Notifications\n\n"
    msg['From']   = GMAIL_SENDER # some SMTP servers will do this automatically, not all
    msg['Content-Type'] = "text/html; charset=utf-8"

    conn.sendmail(GMAIL_SENDER, RECIPIENT,  msg.as_string())
    conn.quit()
    print('Sent notificaton e-mail to ' + RECIPIENT)

run()