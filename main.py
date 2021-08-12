from requests_html import HTMLSession

cookies = {
    "rwe#lang": "en",
    "fonts-all-loaded": "is-cached",
    "et_allow_cookies": "0",
    "gdpr-settings-cookie": "1|true|8/12/2021|8/12/2023|454930304",
}

headers = {
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    "sec-ch-ua-mobile": "?0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://www.rwe.com/en/rwe-careers-portal/job-offers?cm=RWE%20Supply%20%26%20Trading%20GmbH&fa=P-24",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

params = (
    ("cm", "RWE Supply & Trading GmbH"),
    ("fa", "P-24"),
)

session = HTMLSession()
r = session.get(
    "https://www.rwe.com/en/rwe-careers-portal/job-offers",
    cookies=cookies,
    headers=headers,
    params=params,
)

r.html.render()
job_offers = r.html.find("div.headtext")
print("-------------RWEST IT Job Offers-------------")
for job_offer in job_offers:
    job_offer_attr = job_offer.text.split("\n")
    print("Role: " + job_offer_attr[0])
    print("Location: " + job_offer_attr[1])
    print("Duration: " + job_offer_attr[2])
    print("Date: " + job_offer_attr[3])
    print()
