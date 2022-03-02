import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('group3@apsjorhat.org',"apsj#12345678")
message="hello testing smtp at night"
s.sendmail('group3@apsjorhat.org','jyotishmanpathak32@gmail.com',message)
