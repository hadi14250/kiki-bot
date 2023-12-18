import json
import re

def getTwitterFollowers(soupHtml):
    try:
        script_tag = soupHtml.find('script', {'type': 'application/ld+json'})
        if (script_tag):
            script_text = script_tag.string
        else:
            return (None)
        cleaned_json_string = re.sub(r'[ \n\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', script_text)
        json_data = json.loads(cleaned_json_string)

        # Extract the userInteractionCount for the "Follows" action
        follows_count = None
        interaction_statistic = json_data.get('author', {}).get('interactionStatistic', [])
        for interaction in interaction_statistic:
            if interaction.get('@type') == 'InteractionCounter' and interaction.get('interactionType') == 'https://schema.org/FollowAction':
                follows_count = interaction.get('userInteractionCount')
                break
        return (follows_count)

    except json.decoder.JSONDecodeError as e:
        return None

def extractTwitterUserInteractionCount(soupHtml, type):
    if not (soupHtml):
        return (None)
    if (type == "followers"):
        return (getTwitterFollowers(soupHtml))
    