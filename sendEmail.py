import os
import mimetypes
import smtplib
from email.message import EmailMessage
import logging
from dotenv import load_dotenv
from getDates import getTodaysDate, getYesterdaysDate
from logger import startLogger

# load_dotenv()

logger = startLogger()

def getFilePath(file_name):
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, file_name)
    return file_path

def readHtmlTemplate(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def deleteExcelFile(file_path):
    try:
        os.remove(file_path)
        logger.info(f"File deleted successfully: {file_path}")
    except OSError as e:
        logger.error(f"Error deleting file {file_path}: {e}")

def send_mail(subject: str, send_from: str, send_to: str, send_cc: str, message: str, directory: str, filename: str):
    try:
        # Create the email message
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = send_from
        msg['To'] = send_to
        msg['Cc'] = send_cc
        msg.set_content(message)
        path = os.path.join(directory, filename)

        if os.path.exists(path):
            ctype, encoding = mimetypes.guess_type(path)
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)
            
            with open(path, 'rb') as fp:
                msg.add_attachment(fp.read(),
                                   maintype=maintype,
                                   subtype=subtype,
                                   filename=filename)
        else:
            logger.error("File not found: %s", path)
            return

        smtp = smtplib.SMTP_SSL("smtp.sendgrid.net", 465)
        smtp.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASSWD"))
        smtp.send_message(msg)
        smtp.quit()
        logger.info("Email sent successfully!")
        deleteExcelFile(path)
    except Exception as e:
        logger.error("An error occurred: %s", str(e), exc_info=True)

def sendExcelSheetToMods(emailTo, ccRecepients):
    logger.info("Sending Email To Mods...")
    yesterDaysDate = getYesterdaysDate()
    todaysDate = getTodaysDate()
    subject = "Scom Coin Daily Excel Sheet | from Date: {} to {}".format(yesterDaysDate, todaysDate)
    emailFrom = os.environ.get("EMAIL_FROM")
    bodyText = "Dear Mods,\n\nPlease find attached The Daily Scom Users Excel Sheet for the date: {} to {}".format(yesterDaysDate, todaysDate)
    cwd = os.getcwd()
    excelFileName = "Daily_User_Data.xlsx"
    send_mail(
                subject,
                emailFrom,
                emailTo,
                ccRecepients,
                bodyText,
                cwd,
                excelFileName)