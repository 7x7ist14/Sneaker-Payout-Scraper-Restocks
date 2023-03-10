# Sneaker-Payout-Scraper-Restocks
A Scraper that sends you every payout price for all sizes of a sneaker on Restocks in your discord channel


# Requirements:
1. Check if you have all the needed Python libraries.

+ requests (pip install requests)
+ json (pip install json)
+ BeautifulSoup (pip install beautifulsoup4)
+ Discord (pip install discord.py)
+ selenium (pip install selenium)

--> to install them just write the pip install... command in your Terminal.

# Chrome Driver
Please Check that you have the same version of the chrome driver in the folder with the scraper files as your main chrome is!
To check that go to "chrome://settings/help" and click on "About Chrome".
After that go to https://chromedriver.chromium.org/downloads and download the right version.
If your version isn't the same as in the Folder, just download your version and replace the chrome-driver file.
In the folder is the version: ChromeDriver 110.0.5481.77

2. Open the "Config" file and input your Discord Bot-Token and the name of the discord channel (exact name of the channel. not the server name!) were you want to use the scraper in.

3. Open and run the "discord_embed" file. (best for this is VS-Code in my opinion)

4. Write the keyword ($r) + SKU in your discord server.
   format: $r SKU --> (example: $r CW1590-100)
   You can also change the keyword command in the config file if you want to.


The Scraper will now send you all listed sizes and their payout prices in the discord channel.
Also the Restocks product URL is in the blue title.
At the bottom of the discord message you can also find the StockX, Restocks, Sneakit and Hypeboost Product URL to the Scraped Product.

# Return Message Example:
The return message looks like this:

![image](https://user-images.githubusercontent.com/103487648/224415176-96d7eb22-cd05-48f5-bb9a-65132deef512.png)
