# data_science_project
Data Science Demo Project

Demo project objectives:
1. Build charts on hits for job posting website
2. The hits information must contain: source City/Country, date and time 
3. Enhance Job Postings with data from another job posting website (example: Glassdoor)
4. The Job postings must contain: City/Country, job title, skills

# Solution - Part 1 and 2
As the first step, I needed to create a dataset with the information required, but as I have no access to this type of information, I build my own dataset.

The base dataset is build combining the files:
- cities_per_country.csv --> contain the list of the most important cities per country code
- coutry_codes_data.csv --> contains the list of country codes and country names
- trafficdata.csv --> contains the data traffic (originally from android apps downloads) but we can use it to simulate website traffic.
All these files are available in the repository.

The script WebTrafficCreator.py combines these data files a create a csv file with the fields required as described on the guidelines.

In order to use it, please change the file path to the ones on your computer.

Once we get the csv file, we use the second script (JobsWebsiteTrafficDataAnalysis.py). Again, please consider updating the paths defined on the script with the ones on your computer.

It is recomended to run this script on an IDE like Spider, so you are able to run the script by pieces, in order to visualize the results of each action.


# Solution - Part 3 and 4
We need to create a new dataset of job posts with the information indicated on the guidelies, for that we do a little bit of Web Scrapping on the VanHack job site to get the list of the last 100 job posts.

Once we have that information, we can generate a couple of charts indicating which are the cities with the most number of jobs and which are the most demanded skills in the market.

After that, the script does more Web Scrapping on the Glassdoor.com site in order to get the average salaries for each job title we got from the VanHack site.

With that information, it is possible to make a chart with most paid jobs enhancing in this way the original dataset obtained from the VanHack site.

In this case, the script is provided in the form of a Jupyter Notebook. It is also recomended to run this script step by step, in order to get a better understanding of the different actions defined on the script.

