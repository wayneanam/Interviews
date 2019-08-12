import requests, copy, pprint

MAX_FOLLOWERS = 5

def buildURL(user):
  return 'https://api.github.com/' + 'users/' + user + '/followers' +'?per_page=' + str(MAX_FOLLOWERS)
  
def makeRequest(url):
  return requests.get(url)
  
def getFollowersArray(body):
  return list(map(lambda x: x['login'], body))

def retrieveAllData(userList):
  DEPTH = 3
  
  allUsers = []
  
  while(DEPTH > -1):
    for user in userList:
      allUsers = []
      url = buildURL(user)
      response = makeRequest(url)
      
      if response.status_code == 200:
        body = response.json()
        pprint.pprint(body)
        
        followers = getFollowersArray(body)
        
        for id in followers:
          allUsers.append(id)
      
    
    #print(allUsers)
    userList = copy.deepcopy(allUsers)
    DEPTH -= 1


# Main Function
if __name__ == "__main__":
  user = input("Please enter a GitHub ID: ")
  userList = [user]
  retrieveAllData(userList)
