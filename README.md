# README

# Introduction

This is a very quick and dirty unofficial API implementation for Energy Australia.

Warnings:

    - Incorrect username/password combination causes 1 hr lockouts.
    - This may break tomorrow. Working as of 2020-05-16

# Requirements

* Python3
* Requests 

# Background

Energy Australia provides daily energy usage, price and minimum, maximum temperatures.

This daily information is provided in a list with each day represented as a dictionary. The following keys are available for each day. 

    - "nmi"                     Unique identifier?
    - "consumption"             Energy consumption (kWh)
    - "estimatedConsumption"    Always None?
    - "readDate"                Date
    - "prevDate"                Same as above
    - "interval"                Always 0?
    - "cost"                    Cost of consumed electricity ($)
    - "minTemp"                 Temperature in your city/location? Not sure on accuracy?
    - "maxTemp"                 Same as above

# Usage

This will get you daily data from between 1 January 2020 to 31st May 2020.

The date range must be provided as a string in a two element list. The following format is acceptable - "2020-01-01".  

    username = "username"
    password = "password"

    date = ["2020-01-01", "2020-05-31"]

    EA_API = EnergyAustraliaAPI(username,password)

    data = EA_API.get_daily_data(date)
    
    # Loop over the list to get each day
    for day in data:
        info = f"On {day['readDate']}, you consumed {day['consumption']} kWh with an estimated usage cost {day['cost']}"
        print(info)


# Final

This is a very quick and dirty implementation with very limited error checking.

Pull requests welcome.



# Licence

MIT