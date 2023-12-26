import openpyxl
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def addInvalidUsersToExcelSheet(user):
    excel_file_path = "invalidUsers.xlsx"  # Change this to your Excel file path
    sheet_name = "InvalidUsers"  # Change this to your sheet name

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



def addInvalidPostsToExcelSheet(user):
    excel_file_path = "invalidUsers.xlsx"  # Change this to your Excel file path
    sheet_name = "InvalidPosts"  # Change this to your sheet name

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
        user.scomuserNum,
        user.id,
        user.socialMedia,
        user.socialMediaType,
        user.scomUserName,
        user.url,
        user.followers,
        user.validated,
        user.proxyJobID,
        user.totalPayment
    ]
    sheet.append(new_row)

    # Save the Excel file
    workbook.save(excel_file_path)
