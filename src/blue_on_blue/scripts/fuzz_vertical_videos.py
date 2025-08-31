import json
import sys
import uuid
import pprint
import string
import random
import argparse
import copy
from pathlib import Path
from datetime import datetime, timedelta

default_user_fixture = {
    "model": "vertical_video.VerticalVideo",
    "pk": 1,
    "fields": {
      "name": "alice",
      "user": "",
      "likes": 10,
      "video_file": "videos/asfqwgwerqg.mp4",
      "created_at": "2023-01-05T10:15:00Z",
    }
  }

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--num_records", "-n", type=int, help="The total number of records to generate")
    parser.add_argument("--fixture_dir", "-f", help="The directory where the fixture will be saved.")
    parser.add_argument("--account_fixtures", "-a", help="The path to the fixture .json that used to generate the Social Media User Accounts.")

    args = parser.parse_args()

    with open(Path(args.account_fixtures), "r") as f:
        existing_accounts = json.load(f)

    if len(existing_accounts) == 0:
        print(f"No Social Media User Accounts. Unable to create vertical video posts.")
        sys.exit(0)

    account_ids = [account['pk'] for account in existing_accounts]

    min_year=2014
    max_year=datetime.now().year 

    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year+1
    end = start + timedelta(days=365 * years)

    fixtures: list[dict] = []
    for i in range(0, args.num_records):
        
        new_video_fixture = copy.deepcopy(default_user_fixture)
        new_video_fixture['pk'] = str(uuid.uuid4())

        for key in new_video_fixture['fields'].keys():
            match key:
                case "name":
                    new_video_fixture['fields'][key] = ''.join(
                        random.choices(string.ascii_letters + string.digits, k=50)
                    )
                
                case "likes":
                    new_video_fixture['fields'][key] = random.randint(0, 100_000)

                case "video_file":
                    random_video_str = ''.join(
                        random.choices(string.ascii_letters + string.digits, k=20)
                    )
                    new_video_fixture['fields'][key] = f"videos/{random_video_str}.mp4"
                
                case "user":
                    new_video_fixture['fields'][key] = random.choice(account_ids)
                
                case "created_at":
                    random_date = start + (end - start) * random.random()
                    new_video_fixture['fields'][key] = random_date.strftime("%Y-%m-%dT%H:%M:%SZ")

        pprint.pprint(new_video_fixture)
        fixtures.append(new_video_fixture)
    
    output_path = Path(args.fixture_dir) / f"{str(uuid.uuid4())}.json"
    print(f"Saved {args.num_records} of fuzz Vertical Video fixtures to {output_path}")

    with open(output_path, "w") as f:
        json.dump(fixtures, f)

