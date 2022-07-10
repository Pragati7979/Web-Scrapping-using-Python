from autoscraper import AutoScraper

amazon_url="https://www.amazon.in/s?k=samsung"

wanted_list=["₹36,990","Samsung Galaxy S20 FE 5G (Cloud Mint, 8GB RAM, 128GB Storage)"]

scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)

print(scraper.get_result_similar(amazon_url,grouped=True))

scraper.set_rule_aliases({'rule_fz73':'Price','rule_i1ne':'Title'})
scraper.keep_rules(['rule_fz73','rule_i1ne'])
scraper.save('amazon-search')