import smtplib

def KirimNotifikasi():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login('vendingdispenser@gmail.com', 'password')

	subject = 'Air Habis!'
	body = 'Air dalam kemasan 19 liter sudah habis dan perlu diganti'

	msg = f'Subject:{subject}\n\n{body}'
	server.sendmail('vendingdispenser@gmail.com', 'vendingdispenser@gmail.com', msg)
	print("mail sent")