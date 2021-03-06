import os

from instauto.api.client import ApiClient
from instauto.api.actions import post as ps
from instauto.api.actions import search as se

if __name__ == '__main__':
    if os.path.isfile('./.instauto.save'):
        client = ApiClient.initiate_from_file('./.instauto.save')
    else:
        client = ApiClient(user_name=os.environ.get("INSTAUTO_USER") or "your_username", password=os.environ.get("INSTAUTO_PASS") or "your_password")
        client.login()
        client.save_to_disk('./.instauto.save')


s = se.Tag('instagram', 1)
resp = client.search_tag(s).json()
results = resp['results'][0]
tag_name = results['name']
rbt = ps.RetrieveByTag(tag_name)
obj, result = client.post_retrieve_by_tag(rbt)
retrieved_items = []
    
# retrieve the first 20 posts
while result and len(retrieved_items) < 20:
    retrieved_items.extend(result)
    obj, result = client.post_retrieve_by_tag(obj)
    print(f"Retrieved {len(result)} new posts!")
print(f"Retrieved a total of {len(retrieved_items)} posts!")

