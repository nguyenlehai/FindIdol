# API JAV: toidicodedao :v

import requests


def FindActress():
  url = 'https://jav-rest-api-htpvmrzjet.now.sh/api/actress?name='
  jav_name = input("Enter name of jav actress: ")
  jav_url = url + jav_name
  jav_request = requests.get(jav_url).json()

  counts = len(jav_request['result'])
  print("{:<3} | {:<7} | {:17} | {}\t".format("#", "ID", "Name of JAV Idol", "Japanese Name"))
  print("==================================================")

  for i in range(counts):
    actress_id = jav_request['result'][i]['id']
    actress_name = jav_request['result'][i]['name']
    japan_name = jav_request['result'][i]['japanName']
    print("{:<3} | {:<7} | {:17} | {}\t".format(i + 1, actress_id, actress_name, japan_name))
  print('Found {} idol named "{}"'.format(counts, jav_name))
  print()


def FindMovies():
  api_video = 'https://jav-rest-api-htpvmrzjet.now.sh/api/videos/'
  actress_id = input("Enter idol ID: ")
  video_url = api_video + actress_id
  video_request = requests.get(video_url).json()
  video_counts = len(video_request['result'])
  actress_name = video_request['result'][0]['actress'][0]['name']

  print("{:<3} | {} | {}\t| {:<15} | {}".format("#", "Year", "Name", "Code", "Name of movies"))
  print("=============================================================================")

  for i in range(video_counts):
    video_title = video_request['result'][i]['name']

    if len(video_request['result'][i]['name']) > 50:
      video_title = video_title.replace(video_title[49:], '...')
    else:
      video_title = video_request['result'][i]['name']

    site_url = video_request['result'][i]['siteUrl']
    video_code = site_url[(site_url.find("cid=") + 4):(len(site_url) - 1)].upper()
    year = video_request['result'][i]['date'][:4]

    message = "{:<3} | {} | {}\t| {:<15} | {}".format(i + 1, year, actress_name, video_code, video_title)
    print(message)
  print("Found {} videos for {}".format(video_counts, actress_name))
  print()


def checkContinue():
  while True:
    FindActress()
    FindMovies()
    cont = input("Do you want to continue?[Y/N]: ")
    if cont.lower() == 'n':
      print('Have fun :v =)))')
      break


if __name__ == "__main__":
  checkContinue()
