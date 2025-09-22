import psutil
import os
import time
import sys
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

SENDER_EMAIL = "marvellous.prithviraj@gmail.com"
APP_PASSWORD = "xvzz zfha sjkp cmoo"

def Createlog(Foldername, receiver_email):
    if not os.path.exists(Foldername):
        os.mkdir(Foldername)
        
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","")
    timestamp = timestamp.replace("/","")
    
    Filename = os.path.join(Foldername,"Marvellous%s.log"%(timestamp))
    
    fobj = open(Filename,"w")
    
    broder = "-"*80 + "\n"
    fobj.write(broder)
    fobj.write("\n\t\tMarvellous infosystems Process log\n")
    fobj.write("\t\tlog file is created at:"+time.ctime()+"\n")
    fobj.write(broder)
    Data = ProcessScan()
    
    for value in Data:
        fobj.write("%s \n\n" %value)
    fobj.write(broder)
    fobj.close()
    send_logs_via_email(Filename, receiver_email)
    
def ProcessScan():

    listprocess = []    
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            info['vms'] = proc.memory_info().vms / (1024*1024)
            listprocess.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess) :
            pass
    
    return listprocess 

def send_logs_via_email (filename, receiver_email):
    
    subject = "Log details"
    body = "Hi,\nPlease find the attached log file."
    
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = receiver_email or "marvellous.prithviraj@gmail.com"
    message["Subject"] = subject
    
    
    message.attach(MIMEText(body, "plain"))
    
    attachment = open(filename, "rb")

    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={os.path.basename(filename)}",
    )
    message.attach(part)
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    
    s.login(SENDER_EMAIL, APP_PASSWORD)
    
    s.sendmail(SENDER_EMAIL, receiver_email, message.as_string())
    print("Email sent successfully!")
    s.quit()

    if(len(sys.argv) == 3):
        Createlog(sys.argv[1], sys.argv[2])
    # send_logs_via_email()
    
    
if __name__ =="__main__":
    main()