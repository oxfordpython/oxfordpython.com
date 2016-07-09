# Slack module for sending to webhook
import requests
import json
from ..settings import SLACK_TOKEN, SLACK_USERNAME, SLACK_ICON_URL, SLACK_CHANNEL

def send_to_slack(message):
    '''
    Send message to slack webhook
    '''
    payload = {'text': message, 'username': SLACK_USERNAME,
               'icon_url': SLACK_ICON_URL, 'channel': SLACK_CHANNEL}
    server_url = 'https://hooks.slack.com/services/{0}'.format(SLACK_TOKEN)
    requests.post(server_url, data=json.dumps(payload))