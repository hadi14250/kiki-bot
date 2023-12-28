import openpyxl
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def addInvalidUsersToExcelSheet(user):
    excel_file_path = "Daily_User_Data.xlsx"  
    sheet_name = "Invalid Accounts"  

    # Open or create the Excel file
    try:
        workbook = openpyxl.load_workbook(excel_file_path)
    except FileNotFoundError:
        workbook = Workbook()

    # Select or create the sheet
    if sheet_name in workbook.sheetnames:
        sheet = workbook[sheet_name]
    else:
        sheet = workbook.create_sheet(sheet_name)

        # Add headers if the sheet is newly created
        headers = ["ScomuserNum", "ID", "SocialMedia", "SocialMediaType", "ScomUserName", "URL", "Followers", "Validated", "ProxyJobID"]
        for col_num, header in enumerate(headers, 1):
            col_letter = get_column_letter(col_num)
            sheet[f"{col_letter}1"] = header

    # Append user information to a new row
    new_row = [
        user.scomuserNum,
        user.id,
        user.socialMedia,
        user.socialMediaType,
        user.scomUserName,
        user.url,
        user.followers,
        user.validated,
        user.proxyJobID
    ]
    sheet.append(new_row)

    # Save the Excel file
    workbook.save(excel_file_path)

def addValidUsersToExcelSheet(user):
    excel_file_path = "Daily_User_Data.xlsx"  
    sheet_name = "valid Accounts"  

    # Open or create the Excel file
    try:
        workbook = openpyxl.load_workbook(excel_file_path)
    except FileNotFoundError:
        workbook = Workbook()

    # Select or create the sheet
    if sheet_name in workbook.sheetnames:
        sheet = workbook[sheet_name]
    else:
        sheet = workbook.create_sheet(sheet_name)

        # Add headers if the sheet is newly created
        headers = ["ScomuserNum", "ID", "SocialMedia", "SocialMediaType", "ScomUserName", "URL", "Followers", "Validated", "ProxyJobID"]
        for col_num, header in enumerate(headers, 1):
            col_letter = get_column_letter(col_num)
            sheet[f"{col_letter}1"] = header

    # Append user information to a new row
    new_row = [
        user.scomuserNum,
        user.id,
        user.socialMedia,
        user.socialMediaType,
        user.scomUserName,
        user.url,
        user.followers,
        user.validated,
        user.proxyJobID
    ]
    sheet.append(new_row)

    # Save the Excel file
    workbook.save(excel_file_path)


def addInvalidPostsToExcelSheet(post):
    excel_file_path = "Daily_User_Data.xlsx"  
    sheet_name = "Invalid Posts"  

    # Open or create the Excel file
    try:
        workbook = openpyxl.load_workbook(excel_file_path)
    except FileNotFoundError:
        workbook = Workbook()

    # Select or create the sheet
    if sheet_name in workbook.sheetnames:
        sheet = workbook[sheet_name]
    else:
        sheet = workbook.create_sheet(sheet_name)

        # Add headers if the sheet is newly created
        headers = ["ScomuserNum", "ID", "SocialMedia", "SocialMediaType", "ScomUserName", "URL", "Followers", "Validated", "ProxyJobID", "Reward"]
        for col_num, header in enumerate(headers, 1):
            col_letter = get_column_letter(col_num)
            sheet[f"{col_letter}1"] = header

    # Append user information to a new row
    new_row = [
        post.scomuserNum,
        post.id,
        post.socialMedia,
        post.socialMediaType,
        post.scomUserName,
        post.url,
        post.followers,
        post.validated,
        post.proxyJobID,
        post.totalPayment
    ]
    sheet.append(new_row)

    # Save the Excel file
    workbook.save(excel_file_path)


def addValidPostsToExcelSheet(post):
    excel_file_path = "Daily_User_Data.xlsx"  
    sheet_name = "Valid Posts To Be Rewarded"  

    # Open or create the Excel file
    try:
        workbook = openpyxl.load_workbook(excel_file_path)
    except FileNotFoundError:
        workbook = Workbook()

    # Select or create the sheet
    if sheet_name in workbook.sheetnames:
        sheet = workbook[sheet_name]
    else:
        sheet = workbook.create_sheet(sheet_name)

        # Add headers if the sheet is newly created
        headers = ["ScomuserNum", "ID", "SocialMedia", "SocialMediaType", "ScomUserName", "URL", "Followers", "Validated", "ProxyJobID", "Reward"]
        for col_num, header in enumerate(headers, 1):
            col_letter = get_column_letter(col_num)
            sheet[f"{col_letter}1"] = header

    # Append user information to a new row
    new_row = [
        post.scomuserNum,
        post.id,
        post.socialMedia,
        post.socialMediaType,
        post.scomUserName,
        post.url,
        post.followers,
        post.validated,
        post.proxyJobID,
        post.totalPayment
    ]
    sheet.append(new_row)

    # Save the Excel file
    workbook.save(excel_file_path)

def add_InValid_Followers_But_Valid_Posts_To_Excel_Sheet(post):
    excel_file_path = "Daily_User_Data.xlsx"  
    sheet_name = "Valid Posts But Invalid Followers"  

    # Open or create the Excel file
    try:
        workbook = openpyxl.load_workbook(excel_file_path)
    except FileNotFoundError:
        workbook = Workbook()

    # Select or create the sheet
    if sheet_name in workbook.sheetnames:
        sheet = workbook[sheet_name]
    else:
        sheet = workbook.create_sheet(sheet_name)

        # Add headers if the sheet is newly created
        headers = ["ScomuserNum", "ID", "SocialMedia", "SocialMediaType", "ScomUserName", "URL", "Followers", "Validated", "ProxyJobID", "Reward"]
        for col_num, header in enumerate(headers, 1):
            col_letter = get_column_letter(col_num)
            sheet[f"{col_letter}1"] = header

    # Append user information to a new row
    new_row = [
        post.scomuserNum,
        post.id,
        post.socialMedia,
        post.socialMediaType,
        post.scomUserName,
        post.url,
        post.followers,
        post.validated,
        post.proxyJobID,
        post.totalPayment
    ]
    sheet.append(new_row)

    # Save the Excel file
    workbook.save(excel_file_path)
