from crawler import *
choice = input("Press 1 for pdf or 2 for docx or 3 to upload a file: ")
if choice == '1':
    download_pdf()
if choice == '2':
    download_docx()
if choice == '3':
    upload_file_using_client()