import csv
from io import StringIO
from datetime import datetime
from fastapi import UploadFile
from Infrastructure.email.send_mail import EmailSender as email_sender
from Infrastructure.database.database import Database as db

class ReadCsvUseCase:
    async def read_csv(data: UploadFile):
        contents = await data.read()
        decoded = contents.decode()
        buffer = StringIO(decoded)
        reader = csv.reader(buffer)
        try:
            next(reader)
            for name, governmentId, email, debtAmount, debtDueDate, debtId in reader:
                debtAmount = float(debtAmount)
                debtDueDate = datetime.strptime(debtDueDate, '%d-%m-%Y').date()

                message = f"""\
                <html>
                    <body>
                        <p>Hello, {name}!<br> 
                        Your debt with value: US$ {debtAmount} is here, and his due date is {debtDueDate}.
                        </p>
                    </body>
                </html>
                """.format(name=name, debtAmount=debtAmount, debtDueDate=debtDueDate)

                sended = await email_sender.send_email(
                    subject="Attention with your debt!", 
                    receiver=email, 
                    email_body=message)
        
        except Exception as e:
            print(e)
            return "an error ocurred"
        
        date = datetime.now
        await db.insert_upload(date) 
        return date