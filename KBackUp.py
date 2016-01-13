### Deruazvincent@gmail.com

import ftplib
import os
import tarfile
import smtplib
import datetime
from email.mime.text import MIMEText

class KBackUp:
    def __init__(self, host, login, password):
        self.host = host
        self.login = login
        self.password = password
        self.target_directory = './'
        self.output_directory = './'
        self.confirme_by_email = False

    ### self.target_directory -> directory to backup
    ### self.output_directory -> directory to store the archive
    def set_directories(self, target_directory, output_directory):
        self.target_directory = target_directory
        self.output_directory = output_directory

    def archive(self):
        self.home_dirs = [name for name in os.listdir(self.target_directory) if os.path.isdir(os.path.join(self.target_directory, name))]
        tar = tarfile.open(os.path.join(self.output_directory, 'archive.tar.gz'), 'w:gz')
        for directory in self.home_dirs:
            full_dir = os.path.join(self.target_directory, directory)
            tar.add(full_dir)
        tar.close()

    def send_to_ftp(self):
        session = ftplib.FTP(self.host, self.login, self.password)
        file = open(self.output_directory + 'archive.tar.gz', 'rb')
        session.storbinary('STOR archive.tar.gz', file)
        file.close()
        session.quit()
        if self.confirme_by_email:
            print "sending confirmation email"
            self.send_confirmation()

    def confirmation_email(self, to, gmail_user, gmail_password):
        self.confirme_by_email = True
        self.to = to
        self.gmail_user = gmail_user
        self.gmail_password = gmail_password

    def send_confirmation(self):
        smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(self.gmail_user, self.gmail_password)
        today = datetime.datetime.now()
        msg = MIMEText("At " + today.strftime('%H:%M:%S') + "\nBackup done! ")
        msg['Subject'] = 'Backup on %s' % today.strftime('%b %d %Y')
        msg['From'] = self.gmail_user
        msg['To'] = self.to
        smtpserver.sendmail(self.gmail_user, [self.to], msg.as_string())
        smtpserver.quit()


if __name__ == '__main__':
    k_b_u = KBackUp('', '', '')
    k_b_u.confirmation_email('', '', '')  ### Optional
    k_b_u.set_directories('/home/pi/gitdir/', '/home/pi/')

    print "Start archiving directory"
    k_b_u.archive()
    print "End archiving directory"
    print "Start sending"
    k_b_u.send_to_ftp()
    print "End sending"
