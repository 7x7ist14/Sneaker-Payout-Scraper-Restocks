# Sneaker-Payout-Scraper-Restocks
A Scraper that sends you every payout price for all sizes of a sneaker on Restocks in your discord channel


# Requirements:

Check if you have all the needed Python libraries.

-->To install all needed libraries just do this:
+ open the folder that contains all files (the folder name should be "Sneaker-Payout-Scraper-Restocks") in your file Explorer.
+ click on the path and write "cmd" --> now press enter
+ you should now see a cmd window, you just have to type "pip install -r requirements.txt" 
+ all needed libraries should now be installed and your good to go :)

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


![image](https://user-images.githubusercontent.com/103487648/224491259-c6f97f2b-49a3-4e82-b787-b355ad10670e.png)


![image](https://user-images.githubusercontent.com/103487648/224491299-5de27831-ed1e-48d6-ae17-105ada7f9733.png)

