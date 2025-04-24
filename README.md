# DataSC-Essences
Data Science Essences project- steam store
For the data collection- we used the command:
"python steam_scraper.py --apps 730 570 578080 --limit 4000 --outfile reviews.csv"
in the terminal.
![alt text](image-2.png)

With that we collected the data that we needed (12,000 rows) in csv file "reviews.csv".

The tools that we used were:

*powershell prompt
*requests library – does the actual web-request: “GET this Steam URL, give me the JSON back.”
*argparse (built-in) – lets us pass flags like --apps 730 instead of hard-coding numbers.
*csv module (built-in) – writes each review line-by-line into reviews.csv.