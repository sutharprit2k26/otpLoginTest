def genrateSendOTP(email_id):
    import random
    import smtplib

    server = smtplib.SMTP('mail.smtp2go.com',2525)
    server.starttls()
    server.login('mr.robot@fsociety.com','Fsociety@123')
    genrateSendOTP.otp = ''.join([str(random.randint(0,9)) for i in range(4)])
    msg='Hello, Your OTP is '+genrateSendOTP.otp
    print(msg)
    genrateSendOTP.otp = int(genrateSendOTP.otp)
    server.sendmail('qurative.ai@qurative.com',email_id,msg)
    server.quit()

def checkOTP(myotp):
    myotp = int(myotp)
    if genrateSendOTP.otp == myotp:
        return True
    else:
        return False