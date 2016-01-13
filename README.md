## Command

        /usr/bin/python ./KBackUp.py

## Configuration

        k_b_u = KBackUp(host, login, password)
        
The above instruction initialize the backup object with host, login, password for your FTP server.

If you want a confirmation by email use the following instruction, and specify "email to", a gamil user name and his password.

        k_b_u.confirmation_email(to, gmail_user, gmail_password)
        
Setup your target directory and where to store the create archive localy:

        k_b_u.set_directories(target_directory, output_directory)
        
Finally call the archiving and sending functions

        k_b_u.archive()
        k_b_u.send_to_ftp()
        
You will find a example of "main" in "KBackUp.py.

## Automatisation

I use this script to backup all my git archive from a Raspberry Pi 2 to a distant FTP every night by the following procedure:

        $crontab -e
       
What is in my crontab:

        30 4 * * * /usr/bin/python /home/pi/backup_to_ftp/KBackUp.py
