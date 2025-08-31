import json
import sys
import uuid
import pprint
import string
import random
import argparse
from datetime import datetime, timedelta
from pathlib import Path

default_user_fixture = {
    "model": "users.SocialMediaAccount",
    "pk": 1,
    "fields": {
      "username": "alice",
      "email": "alice@example.com",
      "full_name": "Alice Johnson",
      "bio": "Coffee lover ☕ | Traveler ✈️ | Cat mom 🐱",
      "date_joined": "2023-01-05T10:15:00Z",
      "last_active": "2023-08-10T12:30:00Z"
    }
  }

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--num_records", "-n", type=int, help="The total number of records to generate")
    parser.add_argument("--fixture_dir", "-f", help="The directory where the fixture will be saved.")

    args = parser.parse_args()

    min_year=2014
    max_year=datetime.now().year

    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year+1
    end = start + timedelta(days=365 * years)

    fixtures: list[dict] = []
    for i in range(0, args.num_records):
        new_fixture = default_user_fixture.copy()
        updated_fields: dict = default_user_fixture['fields'].copy()

        for key in updated_fields.keys():

            match key:
                case "date_joined" | "last_active":
                    random_date = start + (end - start) * random.random()
                    new_fixture['fields'][key] = random_date.strftime("%Y-%m-%dT%H:%M:%SZ")
                    
                case default:
                    new_fixture['fields'][key] = ''.join(
                        random.choices(string.ascii_letters + string.digits, k=50)
                    )
        
        new_json = {
            "model": "users.SocialMediaAccount",
            "pk": str(uuid.uuid4()),
            "fields": updated_fields
        }

        pprint.pprint(new_json)
        fixtures.append(new_json)
    
    output_path = Path(args.fixture_dir) / f"{str(uuid.uuid4())}.json"
    print(f"Saved {args.num_records} of fuzz SocialMediaAccount fixtures to {output_path}")

    with open(output_path, "w") as f:
        json.dump(fixtures, f)
