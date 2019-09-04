# Mumbai University Scraper for Notifications, Circulars and Announcements
## Fetch recent posts and send gmail notifications 

### Python Version
This app is built on python version 3.6.8

## Premise
Mumbai University has long list of broadcast messages on their website in a very rudimentary format. It is very hard for the consumers to browse through multitude of sections, links and pdfs, which again are devoid of the date posted. The pdf files are scanned images of a signed document and hence not digitally searchable.

## Sections to Scan
There are 6 presets to scan and notify. If needed, this can be updated as required, in main.py

## Output
Output contains two parts
* Recent (less than a day old) for each sections (if any).
  Contains all the messages (Date, Title and URL) posted which are less than a day old. If you happen to run the app more than once, these will be repeated
* Past (any other posts) for each sections (if any).
  Limited to just one post (Date, Title, and URL) to give you a reference to older posts
  
If there are no recent posts, no email notification is triggered

## Gmail Integration
The app is preconfigured to send email notifications via Gmail account. Please see [Google Accounts](https://myaccount.google.com/apppasswords) to set your username and app password.
You can send the notification to one or more recipients

## Windows Scheduler
This app comes with a template xml file that can be imported in to the Windows Task Scheduler.
It is pre-configured to run once, at 5:00 pm every day
Please update the full path to the bat file (xpath /Actions/Exec/Command). Also update the shebang line in main.py for the batch file to locate the python executable

### Personalize
* main.py
  * Change shebang line to point to python executable
  * Change sections as per your requirements
  * Change gmail username and app specific password
* mu.bat
  * Change location to main.py
* Mmbai University Scraper.xml
  * Change path to reflect absolute path for main.py


 
