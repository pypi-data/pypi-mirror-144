# svi_data

Code to download American Community Survey Data and [create the Social Vulnerability Index (SVI) data from CDC](https://www.atsdr.cdc.gov/placeandhealth/svi/documentation/SVI_documentation_2018.html). SVI combines data from several different domains into an overall health index:

![](https://www.atsdr.cdc.gov/placeandhealth/svi/documentation/pdf/CDC-SVI-Variables.jpg?_=81002)

This code downloads the data into a pandas dataframe for a given geography (either county, zipcode, census tract, or block group). It is as simple as (running from the root of the directory):

    from src import svi
    key = svi.get_key('census_api.txt') # read in census api key from text file
    svi_zips = svi.get_svi(key,'zip')   # download the SVI data for zipcodes in the US

Packages that need to be installed for this to work are the pandas and [census](https://github.com/datamade/census). Also you will need to sign up for a [census API key](https://api.census.gov/data/key_signup.html) (it is free), and will need access to the internet.

# Future Development

In the `/src/prep_acs.py` functions, it has functions to download the ACS data from the FTP site and creates a localized sqllite database with *all* of the census variables for a given year. Future work will incorporate this as a potential way to grab the data to create the SVI or additional variables from the 5 year ACS (which are available at various geographies). 

This work was supported by [Gainwell technologies](https://www.gainwelltechnologies.com/).
