""" 处理数据请求 """
import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 响应存储在变量中
requestse_dict = r.json()
print("Total repositories:", requestse_dict['total_count'])

# 探索有关仓库的信息(item 是一个列表)
repo_dicts = requestse_dict['items']
print("Repositories returned:", len(repo_dicts))

# 第一个仓库(每一个仓库是一个字典)
repo_dict = repo_dicts[]