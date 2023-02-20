# Page to crawl sites for PDF's
import requests
from bs4 import BeautifulSoup
import boto3
from pprint import pprint
import pathlib
import os

BUCKET_NAME = 'mental-health-sxk-1'


def download_pdf():
    url = input("What URL do we want to get PDF's from: ")

    response = requests.get(url)
    print(response)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all hyperlinks present on webpage
    links = soup.find_all('a')
    for link in links:
        i = 0
        if '.pdf' in link.get('href', []):
            i += 1
            print("Downloading file: ", i)

            # Get response object for link
            response = requests.get(link.get('href'))

            # Write content in pdf file
            pdf = open("pdf" + str(i) + ".pdf", 'wb')
            pdf.write(response.content)
            pdf.close()
            print("File ", i, " downloaded")

    print("All PDF files downloaded")


def download_docx():
    url = input("What URL do we want to get docx files from: ")

    response = requests.get(url)
    print(response)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all hyperlinks present on webpage
    links = soup.find_all('a')
    for link in links:
        i = 0
        if '.docx' in link.get('href', []):
            i += 1
            print("Downloading file: ", i)

            # Get response object for link
            response = requests.get(link.get('href'))

            # Write content in pdf file
            docx = open("docx" + str(i) + ".docx", 'wb')
            docx.write(response.content)
            docx.close()
            print("File ", i, " downloaded")

    print("All docx files downloaded")


def upload_file_using_client():  # WIP
    """
    Uploads file to S3 bucket using S3 client object
    :return: None
    """
    file_to_upload = input("what is uploading: ")
    s3 = boto3.client("s3")
    bucket_name = BUCKET_NAME
    object_name = file_to_upload
    file_name = os.path.join(pathlib.Path(__file__).parent.resolve(), file_to_upload)
    response = s3.upload_file(file_name, bucket_name, object_name)
    pprint(response)  # prints None

# https://brightdata.com/blog/how-tos/web-scraping-with-python?kw=&cpn=14745430544&cam=aw_all_products-all_geos-search_dsa_blog-kw_en-desktop_blog-how-tos__612826796311&utm_term=&utm_campaign=all_products-all_geos-search_dsa_blog-kw_en-desktop&utm_source=adwords&utm_medium=ppc&utm_content=blog-how-tos&hsa_acc=1393175403&hsa_cam=14745430544&hsa_grp=136943771953&hsa_ad=612826796311&hsa_src=g&hsa_tgt=dsa-1649388330704&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&cq_src=google_ads&cq_cmp=14745430544&cq_term=&cq_plac=&cq_net=g&cq_plt=gp&gclid=Cj0KCQiA_bieBhDSARIsADU4zLd5lqvsXpjBjmN0uuMWpZjl5SHvNtXqcU5QNCBISjc9PaBnhK64pXUaArbtEALw_wcB
