## Scripts for seeding the databases (need to be run in squence)

1) Create Social Media Accounts:
`python blue_on_blue/scripts/fuzz_user_fixtures.py -n 20 -f /Volumes/T7/Repos/blue_on_blue/src/users/fixtures`

2) Use existing user fixture to create Vertical Video posts:
`python blue_on_blue/scripts/fuzz_vertical_videos.py -n 30 -f /Volumes/T7/Repos/blue_on_blue/src/vertical_video/fixtures -a /Volumes/T7/Repos/blue_on_blue/src/users/fixtures/57724a13-0603-478c-ba85-15104725060a.json`