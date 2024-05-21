import requests
import json

def lambda_handler(event, context):
    # Slack Webhook URL for sending messages
    url = "your-Webhook-URL"

    # Set default avatar and username for the Slack message
    data = {
        "icon_emoji": ":boom:",
        "username": "Ajou ilzzo AWS Guard-Duty",
    }
    
    # Extracting necessary information from the AWS CloudWatch event
    event_detail = event.get("detail", {})
    finding_id = event_detail.get("id")
    finding_type = event_detail.get("type")
    finding_title = event_detail.get("title")
    finding_severity = event_detail.get("severity")
    finding_description = event_detail.get("description")

    # Create Slack message payload with embedded content
    payload = {
        "channel": "#aws-trigging-channel",
        "text": "Automation Forensic is executed.",
        "attachments": [
            {
                "title": "AWS GuardDuty Finding Details",
                "fields": [
                    {
                        "title": "Type",
                        "value": finding_type,
                        "short": True
                    },
                    {
                        "title": "Title",
                        "value": finding_title,
                        "short": True
                    },
                    {
                        "title": "Severity",
                        "value": str(finding_severity),
                        "short": True
                    },
                    {
                        "title": "Description",
                        "value": finding_description,
                        "short": False
                    }
                ],
                "actions": [
                    {
                        "type": "button",
                        "text": "View in GuardDuty",
                        "url": f"https://ap-northeast-2.console.aws.amazon.com/guardduty/home?region=ap-northeast-2#/findings?macros=current&fId={finding_id}"
                    }
                ]
            }
        ]
    }

    # Merge data and payload
    data.update(payload)

    # Send the Slack message using the Webhook URL
    result = requests.post(url, json=data)
    
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        # Handle HTTP error if the message delivery fails
        return {
            'statusCode': 400,
        }
    else:
        # Return a success response if the message is delivered successfully
        return {
            'statusCode': 200,
            'body': json.dumps("Payload delivered successfully, code {}.".format(result.status_code))
        }
