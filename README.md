# Dubai-rent-prediction-using-linear-regression
The aim of this project is to be able to predict the rent of an apartment in Dubai using the following information: location, area (in sqft), number of bedrooms and the number of bathrooms. The model was then deployed using a flask server.

## Final Deployed Product
The image below shows what the final working version of this model should look like:
<img width="1440" alt="Screenshot 2022-10-15 at 19 13 24" src="https://user-images.githubusercontent.com/113924862/196002023-7af71511-7200-4ece-aa9d-67a07c3a5683.png">

## Scraping Process:
- The scraper.py files contains the code which was used to scrape the real estate website. The code has been heavily commented so that the process can be understood.
- The "Bayut Data.csv" file contains the scraped data for Dubai as of September, 2022.

## Model:
This folder contains:
- A notebook with the code that was used to clean the data, and to design and validate the model
- The notebook is very clearly annotated so following it is quite simple

## Server:
- This folder cotains a folder called "artifiacts", it contains a JSON and pickle file. These together form the model which will be used to make predictions
- It also contains server.py which is the flask server
- The util.py file contains all the routines that have to be performed

## Client:
- This folder contains the javascript, html and css files which were used to make the website
- As my foucs is on model building, the website isn't as aesthetic as it could be.
