import requests
from bs4 import BeautifulSoup

page = requests.get('https://quotes.toscrape.com')

#https://brightdata.com/blog/how-tos/web-scraping-with-python?kw=&cpn=14745430544&cam=aw_all_products-all_geos-search_dsa_blog-kw_en-desktop_blog-how-tos__612826796311&utm_term=&utm_campaign=all_products-all_geos-search_dsa_blog-kw_en-desktop&utm_source=adwords&utm_medium=ppc&utm_content=blog-how-tos&hsa_acc=1393175403&hsa_cam=14745430544&hsa_grp=136943771953&hsa_ad=612826796311&hsa_src=g&hsa_tgt=dsa-1649388330704&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&cq_src=google_ads&cq_cmp=14745430544&cq_term=&cq_plac=&cq_net=g&cq_plt=gp&gclid=Cj0KCQiA_bieBhDSARIsADU4zLd5lqvsXpjBjmN0uuMWpZjl5SHvNtXqcU5QNCBISjc9PaBnhK64pXUaArbtEALw_wcB