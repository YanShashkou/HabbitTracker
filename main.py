import requests
import datetime

END_POINT = 'https://pixe.la/v1/users'

params = {
    "token" : "<TOKEN>",
    "username":"yanshashkou",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
graph_params={
    "id":"graph1",
    "name":"listening-books",
    "unit":"books",
    "type":"int",
    "color":"sora"
}
graph_endpoint = f"{END_POINT}/{params['username']}/graphs"
headers ={
    "X-USER-TOKEN": params['token']
}
pixel_endpoint = f"{END_POINT}/{params['username']}/graphs/{graph_params['id']}"
pixel_params={
    "date":datetime.datetime.now().strftime("%Y%m%d"),
    "quantity":"12"
}
pixel_update_endpoint = f"{END_POINT}/{params['username']}/graphs/{graph_params['id']}/20240107"
update_params={
    "quantity":"1"
}
