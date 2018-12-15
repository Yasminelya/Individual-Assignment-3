# -*- coding: utf-8 -*-

def get_repos(username):
    
    import requests

    url = "https://api.github.com/users/" + username + "/repos"
    
    response = requests.get(url)
    
    repos = response.json()
    
    repos_list = []
    
    for repo in repos :
        d = {"name":repo["name"],"stargazers_count": repo["stargazers_count"],"language":repo["language"]}
        repos_list.append(d)
        
    return repos_list
    
get_repos("yasminelya")
