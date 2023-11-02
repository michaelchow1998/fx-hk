from service.UserAgentService import UserAgentService
import requests

class COMMReq():

    user_agent_service = UserAgentService()

    url = "https://www.hk.bankcomm.com/hk/hk/en/exchange/getForeignExchangeData.do"


    headers = {
        "User-Agent": user_agent_service.get_random_user_agent()
    }

    def get_data(self):
        response = requests.post(url=self.url,  headers=self.headers)

        print(response.status_code)
        print(response.text)