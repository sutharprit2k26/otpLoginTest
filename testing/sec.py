import random
import smtplib

otp = ''.join([str(random.randint(0,9)) for i in range(4)])
print(otp)
print(type(otp))