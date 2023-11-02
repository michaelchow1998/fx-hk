from service.UserAgentService import UserAgentService
import requests

class HSBCReq():

    user_agent_service = UserAgentService()

    url = "https://rbwm-api.hsbc.com.hk/digital-pws-tools-investments-eapi-prod-proxy/v1/investments/exchange-rate?locale=en_HK"


    headers = {
        "User-Agent": user_agent_service.get_random_user_agent()
    }

    def get_data(self):

        response = requests.get(url=self.url,  headers=self.headers)

        print(response.status_code)
        print(response.text)