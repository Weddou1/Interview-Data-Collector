import data_collector
import mongo_connector
from dotenv import load_dotenv

load_dotenv()

collection = initiate_collection()

driver = make_driver()

scroll_and_connect("https://www.facebook.com",driver, os.getenv('MAIL_FACEBOOK'), os.getenv('PASSWORD_FACEBOOK'))

scroll_and_search(driver, "Le décès du président chirac")
scroll_and_click_publication(driver)
res_code=scroll_and_get_html(driver)

res_code=set(list(filter(None,res_code)))

for i in res_code:
    collection.insert_one({"content":i})