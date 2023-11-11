import requests
import time
import threading
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout, TooManyRedirects, SSLError

def make_request(payload, flag, filename):
    try:
        response = requests.post(
            'https://realtime.oxylabs.io/v1/queries',
            auth=('hadi14250', '05590560352Hk200018'),
            json=payload,
        )
        response.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(response.content)
    except (ConnectionError, HTTPError, Timeout, TooManyRedirects, SSLError, RequestException) as e:
        print(f"An error occurred: {e}")

def create_thread(payload, flag, filename):
    thread = threading.Thread(target=make_request, args=(payload, flag, filename))
    time.sleep(0.5)
    thread.start()
    return thread

twitterHandle = "ordinalHO"
twitterSession = "?t=jkhlbh&s=04"

threads = [
    create_thread(
        {"source": "universal", "url": f"https://x.com/{twitterHandle}{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://twitter.com/billyrestey/status/1723108332591030474?t=jqnZFH3KytAI1zwsOJyU-A&s=19", "render": "html"},
        "tweet", 'tweet.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/pubity/", "render": "html"},
        "instagramProfile", 'instagramProfile.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost.html'
    ),



    create_thread(
        {"source": "universal", "url": f"https://x.com/elonmusk{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile2.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://twitter.com/billyrestey/status/1723108332591030474?t=jqnZFH3KytAI1zwsOJyU-A&s=19", "render": "html"},
        "tweet", 'tweet2.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/meehofinds/", "render": "html"},
        "instagramProfile", 'instagramProfile2.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost2.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile2.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPos2t.html'
    ),



    create_thread(
        {"source": "universal", "url": f"https://x.com/CultureCrave{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile3.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://twitter.com/slave4engfa/status/1723308710582464913?t=r8BkEsWks2IiO7LtS_f9gg&s=19", "render": "html"},
        "tweet", 'tweet3.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/laurengerman/", "render": "html"},
        "instagramProfile", 'instagramProfile3.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost3.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile3.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost3.html'
    ),


    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile5.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet5.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile5.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost5.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile5.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost5.html'
    ),


    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile4.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet4.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile4.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost4.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile4.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost4.html'
    ),


    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile6.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet6.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile6.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost6.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile6.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost6.html'
    ),


    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile7.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet7.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile7.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost7.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile7.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost7.html'
    ),


    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile8.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet8.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile8.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost8.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile8.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost8.html'
    ),


    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile9.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet9.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile9.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost9.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile9.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost9.html'
    ),


    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile10.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet10.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile10.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost10.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile10.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost10.html'
    ),


    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile11.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet11.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile11.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost11.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile11.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost11.html'
    ),



    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile12.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet12.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile12.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost12.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile12.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost12.html'
    ),


    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile13.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet13.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile13.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost13.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile13.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost13.html'
    ),


    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile14.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet14.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile14.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost14.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile14.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost14.html'
    ),



    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile15.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet15.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile15.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost15.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile15.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost15.html'
    ),


    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile16.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet16.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile16.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost16.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile16.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost16.html'
    ),


    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile17.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet17.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile17.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost17.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile17.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost17.html'
    ),


    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile18.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet18.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile18.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost18.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile18.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost18.html'
    ),


    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile19.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet19.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile19.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost19.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile19.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost19.html'
    ),



    create_thread(
        {"source": "universal", "url": f"https://x.com/slave4engfa{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile20.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://x.com/itstrahuna/status/1723186496985874758?t=QzeAE9GPVUoOZpx3uydvdg&s=08", "render": "html"},
        "tweet", 'tweet20.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://instagram.com/hariniiiiie_?igshid=OGQ5ZDc2ODk2ZA==", "render": "html"},
        "instagramProfile", 'instagramProfile20.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost20.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile20.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost20.html'
    ),



]

# Wait for all threads to finish
for thread in threads:
    thread.join()
