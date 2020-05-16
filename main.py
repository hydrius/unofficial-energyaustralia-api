import requests
    
class EnergyAustraliaAPI():
    """
    Just a quick and dirty API implementation of EnergyAustralia
    daily data usage

    Warning:
    Incorrect username/password combination causes 1 hr lockouts.

    """

    def __init__(self,username,password):
        
        self.username = username
        self.password = password

        self.login_url = "https://www.energyaustralia.com.au/myaccount/login"

    def _return_URL(self, date):
        """
            Returns URL with date range.
            Requires: 
                - Checking date format (2020-01-31)
                - Check for increasing date
        """

        if len(date) != 2:
            return "DATE RANGE NOT SUPPLIED"

        date_from = date[0]
        date_to = date[1]

        url = f"https://www.energyaustralia.com.au/myaccount/api/usage/9658533534/daily?from={date_from}&to={date_to}"
        return url

    def _payload(self):
        payload = {
            "username": self.username,
            "password": self.password
            }

        return payload
    
    def get_daily_data(self,date):

        url = self._return_URL(date)

        with requests.Session() as s:
            p = s.post(self.login_url, data=self._payload())
            
            link = "https://www.energyaustralia.com.au/myaccount/api/usage/9658533534/daily?from=2020-05-01&to=2020-05-31"
            data = s.get(url)
            data = data.json()
            return data[0]   
            





if __name__ == "__main__":
    username = "username"
    password = "password"

    date = ["2020-01-01", "2020-05-31"]

    EA_API = EnergyAustraliaAPI(username,password)

    data = EA_API.get_daily_data(date)
    
    for day in data:
        info = f"On {day['readDate']}, you consumed {day['consumption']} kWh with an estimated usage cost {day['cost']}"
        print(info)

