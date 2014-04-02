# Uses requests library: http://docs.python-requests.org/en/latest/
import requests
import json

# SM Host
HOST = "https://api.surveymonkey.net"
# limit on number of times to try each request to Mashery
MASHERY_REQUEST_COUNT = 5


# Currently provides the following SurveyMonkey
# API v2 methods:
#   get_respondent_list
#   get_responses
#   get_survey_details
#   get_survey_list
#   get_collector_list
# Handles http using the requests module
class ApiService(object):
    def __init__(self, api_key, access_token):
        self.client = requests.session()
        self.client.headers = {
            "Authorization": "bearer %s" % access_token,
            "Content-Type": "application/json"
        }
        self.client.params = {
            "api_key": api_key
        }

    ############################################
    ######### SurveyMonkey API Methods #########
    ############################################

    # v2.get_respondent_list
    def get_respondent_list(self, data=None):
        data = data if data is not None else {}

        uri = HOST + "/v2/surveys/get_respondent_list"
        # if the user specifies a page, just return data for that specific page
        if "page" in data:
            return self._make_post_request(uri, data)
            # We need to poll for new pages until we have grabbed all
        # of our respondents
        current_page = 1
        respondent_list = []
        while True:
            data["page"] = current_page
            res = self._make_post_request(uri, data)
            if res["status"] != 0:
                return res
            for respondent in res["data"]["respondents"]:
                respondent_list.append(respondent)
            if len(res["data"]["respondents"]) == res["data"]["page_size"]:
                # There are potentially more pages of respondents to grab
                current_page += 1
            else:
                # We have finished getting all respondents
                break
        return {"status": 0, "data": respondent_list}

        # v2.get_responses

    def get_responses(self, data=None):
        data = data if data is not None else {}
        uri = HOST + "/v2/surveys/get_responses"

        # we need a function to divide up the respondent id list into
        # chunks of a maximum of 10 respondents
        def respondent_chunks(r_ids, max_count=10):
            for i in xrange(0, len(r_ids), max_count):
                yield r_ids[i: i + max_count]

                # make sure respondent_ids is a key in data

        if "respondent_ids" not in data:
            return {"status": 3, "errmsg": "Error: respondent_ids required"}
            # now divide up the respondent list into multiple lists of 10 max
        # respondents
        respondent_id_lists = list(respondent_chunks(data["respondent_ids"]))
        responses = []
        for respondent_list in respondent_id_lists:
            data["respondent_ids"] = respondent_list
            res = self._make_post_request(uri, data)
            if res["status"] != 0:
                return res
            for response in res["data"]:
                responses.append(response)
        return {"status": 0, "data": responses}

    # v2.get_survey_details
    def get_survey_details(self, data=None):
        data = data if data is not None else {}
        uri = HOST + "/v2/surveys/get_survey_details"
        return self._make_post_request(uri, data)

    # v2.get_survey_list
    def get_survey_list(self, data=None):
        data = data if data is not None else {}
        uri = HOST + "/v2/surveys/get_survey_list"
        # if the user specifies a page, just return data for that specific page
        if "page" in data:
            return self._make_post_request(uri, data)
            # We need to poll for new pages until we have grabbed all
        # of our surveys
        current_page = 1
        survey_list = []
        while True:
            data["page"] = current_page
            res = self._make_post_request(uri, data)
            if res["status"] != 0:
                return res
            for survey in res["data"]["surveys"]:
                survey_list.append(survey)
            if len(res["data"]["surveys"]) == res["data"]["page_size"]:
                # There are potentially more pages of surveys to grab
                current_page += 1
            else:
                # We have finished getting all surveys
                break
        return {"status": 0, "data": survey_list}

    # v2.get_collector_list
    def get_collector_list(self, data=None):
        data = data if data is not None else {}
        uri = HOST + "/v2/surveys/get_collector_list"
        # if the user specifies a page, just return data for that specific page
        if "page" in data:
            return self._make_post_request(uri, data)
            # We need to poll for new pages until we have grabbed all
        # of our collectors
        current_page = 1
        collector_list = []
        while True:
            data["page"] = current_page
            res = self._make_post_request(uri, data)
            if res["status"] != 0:
                return res
            for collector in res["data"]["collectors"]:
                collector_list.append(collector)
            if len(res["data"]["collectors"]) == res["data"]["page_size"]:
                # There are potentially more pages of collectors to grab
                current_page += 1
            else:
                # We have finished getting all collectors
                break
        return {"status": 0, "data": collector_list}

    # v2.get_response_counts
    def get_response_counts(self, data=None):
        data = data if data is not None else {}
        uri = HOST + "/v2/surveys/get_response_counts"
        return self._make_post_request(uri, data)

    #############################################
    ######## API Service Private Methods ########
    #############################################

    # This will try up to MASHERY_REQUEST_COUNT times to get a valid response
    # from Mashery
    def _make_post_request(self, uri, data=None):
        data = data if data is not None else {}
        for i in range(MASHERY_REQUEST_COUNT):
            response = self._post_request(uri, data)
            if response is not None:
                return response
        return {
            "status": 1,
            "errmsg": "Did not receive a valid response from Mashery"
        }

    def _post_request(self, uri, data=None):
        data = data if data is not None else {}
        response = self.client.post(uri, data=json.dumps(data))
        if "x-mashery-error-code" in response.headers:
            return None
        return response.json()
