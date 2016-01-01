def rotoworld_team_nickname_to_abbreviation(team_nickname):
    upper_case_team_nickname = team_nickname.upper()

    if upper_case_team_nickname == 'HAWKS':
        return 'ATL'

    if upper_case_team_nickname == 'CELTICS':
        return 'BOS'

    if upper_case_team_nickname == 'NETS':
        return 'BRK'

    if upper_case_team_nickname == 'HORNETS':
        return 'CHO'

    if upper_case_team_nickname == 'BULLS':
        return 'CHI'

    if upper_case_team_nickname == 'CAVALIERS':
        return 'CLE'

    if upper_case_team_nickname == 'MAVERICKS':
        return 'DAL'

    if upper_case_team_nickname == 'NUGGETS':
        return 'DEN'

    if upper_case_team_nickname == 'PISTONS':
        return 'DET'

    if upper_case_team_nickname == 'WARRIORS':
        return 'GSW'

    if upper_case_team_nickname == 'ROCKETS':
        return 'HOU'

    if upper_case_team_nickname == 'PACERS':
        return 'IND'

    if upper_case_team_nickname == 'CLIPPERS':
        return 'LAC'

    if upper_case_team_nickname == 'LAKERS':
        return 'LAL'

    if upper_case_team_nickname == 'GRIZZLIES':
        return 'MEM'

    if upper_case_team_nickname == 'HEAT':
        return 'MIA'

    if upper_case_team_nickname == 'BUCKS':
        return 'MIL'

    if upper_case_team_nickname == 'TIMBERWOLVES':
        return 'MIN'

    if upper_case_team_nickname == 'PELICANS':
        return 'NOP'

    if upper_case_team_nickname == 'KNICKS':
        return 'NYK'

    if upper_case_team_nickname == 'THUNDER':
        return 'OKC'

    if upper_case_team_nickname == 'MAGIC':
        return 'ORL'

    if upper_case_team_nickname == '76ERS':
        return 'PHI'

    if upper_case_team_nickname == 'SUNS':
        return 'PHO'

    if upper_case_team_nickname == 'TRAIL BLAZERS':
        return 'POR'

    if upper_case_team_nickname == 'KINGS':
        return 'SAC'

    if upper_case_team_nickname == 'SPURS':
        return 'SAS'

    if upper_case_team_nickname == 'RAPTORS':
        return 'TOR'

    if upper_case_team_nickname == 'JAZZ':
        return 'UTA'

    if upper_case_team_nickname == 'WIZARDS':
        return 'WAS'

    else:
        raise RuntimeError("unknown team nickname")


"""
@author: Crake
The main goal of this function is alert the user when a large
program has finished running.
It has three time-based functions. This lets the user know
when the function began, and how long it took.
It has two messaging functions.
1. The first takes an error title, and sends a message to the user altering
   her/him of the error
2. The second takes a start and end time, and a name of the function that takes
   a large amount of time for my reference and convenience. This function is
   called when the large program is completed, and sends the message to the
   user.
The way I use this setup as follows:
- I traditionally have a main() function.
- The main() will execute all of the functions of my major program.
- At the top of the main() I call get_time() which, non-surprisingly returns
  the time.
- I store it in some variable start_time.
- I also usually call show_Full_Time() that way at the top of the output for
  whatever program I'm running, I have the start time.
- After the program completes, and I'm at the end of main() I call
  doneTextSend(start_Time, get_time(), process_Name) where process_Name is
  a string for my reference later on.
Carrier	Email to SMS Gateway
*****************************************************************
Alltel	                        [10-digit phone number]@message.alltel.com
                Example: 1234567890@message.alltel.com
AT&T (formerly Cingular)        [10-digit phone number]@txt.att.net
                                [10-digit phone number]@mms.att.net (MMS)
                                [10-digit phone number]@cingularme.com
                Example: 1234567890@txt.att.net
Boost Mobile	                [10-digit phone number]@myboostmobile.com
                Example: 1234567890@myboostmobile.com
Nextel (now Sprint Nextel)	[10-digit telephone number]@messaging.nextel.com
                Example: 1234567890@messaging.nextel.com
Sprint PCS (now Sprint Nextel)	[10-digit phone number]@messaging.sprintpcs.com
                                [10-digit phone number]@pm.sprint.com (MMS)
                Example: 1234567890@messaging.sprintpcs.com
T-Mobile	                [10-digit phone number]@tmomail.net
                Example: 1234567890@tmomail.net
US Cellular	                [10-digit phone number]@email.uscc.net (SMS)
                                [10-digit phone number]@mms.uscc.net (MMS)
                Example: 1234567890@email.uscc.net
Verizon	                        [10-digit phone number]@vtext.com
                                [10-digit phone number]@vzwpix.com (MMS)
                Example: 1234567890@vtext.com
Virgin Mobile USA	        [10-digit phone number]@vmobl.com
                Example: 1234567890@vmobl.com
*****************************************************************
TROUBLE SHOOTING
I run this on Ubuntu 12.04 and this is written in Python 2.7.3
I have no real programming background, and have very little
experience with programming in general. I am writing this up
because this is one of my most helpful functions I've written,
and I want to help anyone who wants to use it as well. There
are some errors is this, but it works so I use it.
If your service provider is not covered in this list, Google
'how do I find out my phone number's email address'. That's how I
came up with this list, and it's not a hard feat to manage.
Verify that your
[10-digit phone number]@serviceProvider.something functions with
and actual email address before using this function to minimize
headaches further on down the line.
This uses Simple Mail Transfer Protocol
http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol
and the setup this program uses is for Gmail.
I recommend that you make a Gmail account, but that's only because
it's what I use. If you want to use another email provider,
search for it. I also recommend that you create an email account
for the express purpose of this program, and that the email account
is not linked to anything else (ie not your Reddit account). In my
opinion this is for your personal security, but hey, do as you will.
I've also encountered some errors when the function will execute,
but a text message will not be received. After reviewing my email
accounts sent message list, I've noted that the emails are sent,
and the error PROBABLY lies with the service provider.
One last thing of note: I start each line in the messages I send
with \n because that's the way I get it to work. There's a reason
behind this fact, however I've never bothered to look.
"""

import smtplib
from users.models import User


# Credentials (if needed)
# I recomend you create a new email account just for this



def doneTextSend(subject, report, impact, timestamp) :
    '''
    function takes the start and end time (both are floating points) of whatever
    your function is, and the function title (string).
    '''

    username = 'rotoworld.alerts'
    fromaddr = 'rotoworld.alerts@gmail.com'
    toaddrs  = User.objects.all()

    # The actual mail send
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.login(username, "rotoworld")

    for recipient in toaddrs:
        msg = "\r\n".join([
          "From: {0}",
          "To: {1}",
          "Subject: {2}",
          "",
          "{3}\r\n",
          "{4}\r\n",
          "{5} UTC"
        ]).format(fromaddr, recipient.email_address, subject, report, impact, timestamp)

        smtpObj.sendmail(fromaddr, recipient.email_address, msg)