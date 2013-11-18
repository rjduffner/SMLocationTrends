import pyipinfodb
import api_service
import simplemapplot
import requests

states_dictionary = {
        'AK': 'ALASKA',
        'AL': 'ALABAMA',
        'AR': 'ARKANSAS',
        'AS': 'AMERICAN_SAMOA',
        'AZ': 'ARIZONA',
        'CA': 'CALIFORNIA',
        'CO': 'COLORADO',
        'CT': 'CONNECTICUT',
        'DC': 'DISTRICT_OF_COLUMBIA',
        'DE': 'DELAWARE',
        'FL': 'FLORIDA',
        'GA': 'GEORGIA',
        'GU': 'GUAM',
        'HI': 'HAWAII',
        'IA': 'IOWA',
        'ID': 'IDAHO',
        'IL': 'ILLINOIS',
        'IN': 'INDIANA',
        'KS': 'KANSAS',
        'KY': 'KENTUCKY',
        'LA': 'LOUISIANA',
        'MA': 'MASSACHUSETTS',
        'MD': 'MARYLAND',
        'ME': 'MAINE',
        'MI': 'MICHIGAN',
        'MN': 'MINNESOTA',
        'MO': 'MISSOURI',
        'MP': 'NORTHERN_MARIANA_ISLANDS',
        'MS': 'MISSISSIPPI',
        'MT': 'MONTANA',
        'NA': 'NATIONAL',
        'NC': 'NORTH_CAROLINA',
        'ND': 'NORTH_DAKOTA',
        'NE': 'NEBRASKA',
        'NH': 'NEW_HAMPSHIRE',
        'NJ': 'NEW_JERSEY',
        'NM': 'NEW_MEXICO',
        'NV': 'NEVADA',
        'NY': 'NEW_YORK',
        'OH': 'OHIO',
        'OK': 'OKLAHOMA',
        'OR': 'OREGON',
        'PA': 'PENNSYLVANIA',
        'PR': 'PUERTO_RICO',
        'RI': 'RHODE_ISLAND',
        'SC': 'SOUTH_CAROLINA',
        'SD': 'SOUTH_DAKOTA',
        'TN': 'TENNESSEE',
        'TX': 'TEXAS',
        'UT': 'UTAH',
        'VA': 'VIRGINIA',
        'VI': 'VIRGIN_ISLANDS',
        'VT': 'VERMONT',
        'WA': 'WASHINGTON',
        'WI': 'WISCONSIN',
        'WV': 'WEST_VIRGINIA',
        'WY': 'WYOMING'
}

class SMLocationTrends() :
    def __init__(self) :
        self.api = api_service.ApiService('pcpuk2dfxdwggu6gfssxqa6t', 'UFHR1aBDl2QjFoOzyDhoj91aM1Q3Atp-HtOvcI8kBk.HIBEdrGLtGKLnbSmHGcE-cNkJnPOaR1t-jiJqrE3iqUwObKHbg3NuTB-u5W6w9bg=')
        self.ip_list = self.get_ips_of_respondents('45533333')
        print self.get_us_response_information_by_state(self.ip_list)

    def get_ips_of_respondents(self,survey_id):
        add_list = []
        responses = self.api.get_respondent_list({'survey_id': survey_id, 'fields':['ip_address']})
        for data in responses['data']:
            add_list.append(data['ip_address'])
        return add_list
    
    def get_location_data(self, ip):
        base_url = 'http://api.ipinfodb.com/v3/ip-city/'
        params = {'key':'ccfd7803a6ddd304d590cd37c92826f9ddaaecc180b69888ffaf7a83b4973586', 'ip':ip, 'format':'json'}
        resp = requests.get(url=base_url, params=params)
        return resp.json()

    def get_us_response_information_by_state(self, ip_list):
        states = []
        for ip in ip_list:
            resp = self.get_location_data(ip)
            if resp['countryCode'] == 'US':
                states.append(resp['regionName'])

        
        state_count = {}
        for key in states_dictionary.keys():
            i = states.count(states_dictionary[key])
            if i>0:
                state_count[states_dictionary[key]] = i
            
        return state_count


    def get_us_response_information_by_county(self, ip_list):
        pass
    def get_world_response_information_by_country(self, ip_list):
        pass

    def get_visual_map(self, states_list):
        pass
            

sm_map = SMLocationTrends()


#
# NEED TO ADD IN RESPONSES
# get responses
#

'''
#a = api.get_survey_list()
#for x in a['data']:
#print x

data = api.get_survey_details({'survey_id': '45533333'})
#print data
print data['data']['title']['text']
responses = api.get_respondent_list({'survey_id': '45533333', 'fields':['ip_address']})
#url = responses['data'][3]['ip_address']

for url in responses['data']:
    print url['ip_address']
    
    #ip_location = 'http://api.hostip.info/get_json.php?ip=' + url['ip_address'] + '&position=true'

    ip_location = 'http://api.ipinfodb.com/v3/ip-city/?key=ccfd7803a6ddd304d590cd37c92826f9ddaaecc180b69888ffaf7a83b4973586&ip=' + url['ip_address'] + '&format=json'

    #ip_location = 'http://www.geody.com/geoip.php?ip=' + url['ip_address']   
    resp = requests.get(url=ip_location, params=None)
    #print resp.content
    print resp.json()


#ids = []
#ids.append(responses['data'][0]['respondent_id'])
#print ids
#print api.get_responses({'survey_id': '45533333', 'respondent_ids': ids})

#print api.get_respondent_list({'survey_id': '45533333'})

example_colors = ["#FC8D59","#FFFFBF","#99D594"]
state_value = {"TX":2, "WI":1, "IL":1, "AK":0, "MI":0, "HI":2}
make_us_state_map(data=state_value, colors=example_colors)



example_colors = ["#FC8D59","#FFFFBF","#99D594"]
country_value = {"us":1, "au":2, "gb":0}
make_world_country_map(data=country_value, colors=example_colors)



        #ip_location = 'http://api.hostip.info/get_json.php?ip=' + url['ip_address'] + '&position=true'
        #ip_location = 'http://api.ipinfodb.com/v3/ip-city/?key=ccfd7803a6ddd304d590cd37c92826f9ddaaecc180b69888ffaf7a83b4973586&ip=' + ip_list[0] + '&format=json'
        #ip_location = 'http://www.geody.com/geoip.php?ip=' + url['ip_address']
        #resp = requests.get(url=ip_location, params=None)

'''
