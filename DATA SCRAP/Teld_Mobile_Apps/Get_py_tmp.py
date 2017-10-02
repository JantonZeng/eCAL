import requests
import random
import datetime
##------ WEB scraping ------#
# def get_station(header, start_page=1, end_page=2, row_nmb=10):
# 	"""
# 		return a list of dictionaries that contains charging station info
# 	"""
# 		curr_page = start_page #specify starting page to scrape, usually it is page 1
# 		page_end = end_page  #specify the page wanted to end scraping. Don't worry if number is too large
# 																						#we ends when page is empty.
# 		row_nmb = row_nmb  #specify how many rows per request returns.
# 		station_info = []  #summarizing all the station location data.

# 		# Starting iteration going over website to scrape station locations
# 		while curr_page <= page_end:
# 			REQUEST_URL = 'https://www.teld.cn/StationNetwork/GetStationNetword?ProvinceName=&CityName=&KeyWords=&RegionName=&type=&page={}'.format(curr_page) + '&rows={}'.format(row_nmb)
# 			resp = requests.get(REQUEST_URL, headers=header)
# 			curr_page += 1
# 			json_requestData = resp.json()
# 			station_info = station_info + json_requestData['rows']
# 		return station_info

# def get_piles(station_code, proxies_pool, header, time_out=1000):
# 	"""
# 		return json object containing piles information
#     	pile code format - string, station_info[0]['code']
# 	"""
# 	STATION_URL = 'https://www.teld.cn/StationNetwork/GetChargingStationByCodeList?StationNo='+ station_code
# 	proxy_idx = random.randint(0,len(proxies_pool)-1)
#     #     print(proxy_idx),
# 	try:
# 		resp = requests.get(STATION_URL, proxies=proxies_pool[proxy_idx], headers=header, timeout=time_out)
# 	# except Exception, e:
# 		pile_info = resp.json()
# 		return pile_info

def get_allStations(hdr):
	"""
		Input:
			hdr - dictionary, detailed spec for headers
		Output:
			stations_list - list, containing all stations info from website, each in format of dict
			Each station has seven attribute: isInterconnection, name, address,
											  isFast, stationType, lat, lng, id
	"""
	REQUEST_URL = 'http://baseapi.teld.cn/api/GetAllStations/StaV3?coordinateType=gaode'
	stations_resp = requests.get(REQUEST_URL, headers=hdr)
	json_requestData = stations_resp.json()
	stations_list = json_requestData['data']['stations']
	return stations_list

 #-----GET ONE STATION DETAILS-----#
def get_oneStation_APP(hdr, stationId, error_log=None, proxies_pool=None,time_out=10000):
	"""
		Input:
			hdr - dictionary, detailed spec for headers
			stationId - string, each station's own station code
			error_log - file, to where store the error messages
			proxies_pool - list, contains all the proxies address
		Output:
			station_detailedInfo - dictionary, containing detailed station information, 37 keys
	"""
	url = "https://basesg.teld.cn/api/invoke"
	querystring = {"SID":"BaseApi-App0304_GetStationDetails"}
	payload = 'param=%7B%0A%20%20%22lng%22%20%3A%20%220.000000%22%2C%0A%20%20%22stationId%22%20%3A%20%22{}%22%2C%0A%20%20%22%lat%22%20%3A%20%220.000000%22%2C%0A%20%20%22%coordinateType%22%20%3A%20%22%gaode%22%0A%7D'.format(stationId)
	try:
		if proxies_pool is not None:
			proxy_idx = random.randint(0,len(proxies_pool)-1)
			terminal_resp = requests.request("POST", url, proxies=proxies_pool[proxy_idx], data=payload,
													headers=hdr, params=querystring, timeout=time_out)
		else:
			terminal_resp = requests.request("POST", url, data=payload, headers=hdr, params=querystring,timeout=time_out)
			json_requestData = terminal_resp.json()
		if json_requestData['data'] is not None:
			station_detailedInfo = json_requestData['data']
		else:
			station_detailedInfo = None
	except requests.exceptions.ConnectionError as e:
		if error_log is not None:
			error_log.write("{}--{}".format(pileCode, e))
		if proxies_pool is not None:,
			print(proxies_pool[proxy_idx])
			proxies_pool.pop(proxy_idx)
		print('failed'),
		station_detailedInfo = None,
	return station_detailedInfo, proxies_pool

# #----- Test on get_oneStation_APP -----##,
# stationId = "c09327a9-fe5b-4b4e-9bff-0e50097000e9",
# hdr = {
# 	'accept': "*/*",
# 	'user-agent': "Teld/3.4.0 (iPhone; iOS 10.3.3; Scale/2.00)",
# 	'cookie': "TELDAppID=",
# 	'content-length': "111",
# 	'connection': "keep-alive",
# 	'accept-encoding': "gzip, deflate",
# 	'device': "app_version=3.4.0&os_version=10.3.3&client=ios&device_name=iPhone 6s (A1633/A1688/A1691/A1700)&device_id=38CD294C-CC36-4998-9074-C7F798EE6087&city_code=4403&city_name=%E6%B7%B1%E5%9C%B3&lat=0.000000&lng=0.000000&network=wifi&location_city_name=",
# 	'host': "basesg.teld.cn",
# 	'content-type': "application/x-www-form-urlencoded",
# 	'cache-control': "no-cache",
# 	'postman-token': "4dd0a429-35ad-1863-c8f5-18e0f7805f60"
# 		}
# station_detailedInfo, proxies_pool = get_oneStation_APP(hdr, stationId)

#-----GET ONE CHARGING PILE DETAILS FROM TERMINAL-----#
def get_onePill_APP(hdr, pillCode, error_log=None, proxies_pool=None, time_out=10000):
	"""
		Input:
			hdr - dictionary, detailed spec for headers
			pillCode - string, each charging pile has its own pile code
			error_log - specify file to write errors
			proxies_pool - contains all the proxies address
		Output:
			pill_detailedInfo - dictionary, containing detailed station information, 49 keys
	"""
	url = "https://basesg.teld.cn/api/invoke"
	querystring = {SID:BaseApi-App0304_GetTerminalDetails}
	payload = 'param=%7B%0A%20%20%22pillCode%22%20%3A%20%22{}%22%2C%0A%20%20%22plateform%22%20%3A%20%22app%22%0A%7D'.format(pillCode)
	try:
		if proxies_pool is not None:
			proxy_idx = random.randint(0,len(proxies_pool)-1)
			pill_resp = requests.request(POST,url, proxies=proxies_pool[proxy_idx], headers=hdr, 
															params=querystring, timeout=time_out)
		else:
			pill_resp = requests.request(POST, url, data=payload, headers=hdr, params=querystring, timeout=time_out)
		json_requestData = pill_resp.json()
		if json_requestData['data'] is not None:
			if 'terminal' in json_requestData['data']:
				pill_detailedInfo = json_requestData['data']['terminal']
			else:
				pill_detailedInfo = None
		else:
			pill_detailedInfo = None
	except requests.exceptions.ConnectionError as e:
		if error_log is not None:
			error_log.write({}--{}.format(pileCode, e))
		if proxies_pool is not None:
			print(proxies_pool[proxy_idx])
		proxies_pool.pop(proxy_idx)
		print('failed')
		pill_detailedInfo = None
	return pill_detailedInfo, proxies_pool

# #----- Generate if-else-encode -----##
# fix_list = ['tag','parkFee','ChargingPort','payType','terminalType']
# for i in fix_list:
# 	print("if pile_detailedInfo['{name}'] is not None:{name} = str(pile_detailedInfo['{name}'].encode('utf-8'))else:{name} = ''".format(name=i))

# #----- Get All Station -----#
# hdr = {'User-Agent':'Mozilla/5.0 Chrome/59.0.3071.115 Safari/537.36', 
#         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
# REQUEST_URL = 'http://baseapi.teld.cn/api/GetAllStations/StaV3?coordinateType=gaode'
# stations_resp = requests.get(REQUEST_URL, headers=hdr)
# json_requestData = stations_resp.json()
# stations_list = json_requestData['data']['stations']"

def get_chargelist_APP(stationId, proxy={'https': '119.90.63.3:3128'}, item_per_pg=150, pg_numb=1):
	"""
		hdr - dict, contains all the headers spec
		stationId - string, individual station id
		proxy - specified proxy address, needs to be https
		iterm_per_pg - specify number of rows in the return pages
		pg_numb - specify number of pages in the the http get request
	"""
	chargeList_detailedInfo_list = []
	for pg in range(1,pg_numb+1):
		url = "https://baseapi.teld.cn/api/GetChargeListBySta/StaV3?"
		querystring = {"itemNumPerPage":"{}".format(item_per_pg), "pageNum":"{}".format(pg), "staID":"{}".format(stationId)}
		chargeList_resp = requests.request("GET", url, params=querystring, proxies=proxy)
		json_requestData = chargeList_resp.json()
		if json_requestData is not None:
			chargeList_detailedInfo = json_requestData['data']['items']
			chargeList_detailedInfo_list.extend(chargeList_detailedInfo)
	return chargeList_detailedInfo_list

