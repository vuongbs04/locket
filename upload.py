import requests, sys, os
# data = open('cc.mp4','rb').read()
# print(data)
# sys.exit()
request_data = {
            "email": 'vuong.works@gmail.com',
            "password": 'Vuong@@2004',
            "clientType": "CLIENT_TYPE_IOS",
            "returnSecureToken": True
 }

url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyCQngaaXQIfJaH0aS2l7REgIjD7nL431So"
response = requests.post(url, json=request_data)
# sys.exit(response.text)
TokenAccount = response.json()['idToken']
localID = response.json()['localId']
typeanh = 'locket-img' #video or img


nameimg = 'P4dbiE9csi4hgIveWkGOisssshjhhjhjss.jpg'
namevideo = 'P4dbiE9csi4hgIveWkGOisssshjhhjhjss.mp4'
filename = 'cc.mp4'
imagesize = os.path.getsize(filename)
data_uploads = open(filename,'rb').read()




head = {
	'content-type': 'application/json; charset=UTF-8',
	'authorization': f'Firebase {response.json()['idToken']}',
	'x-goog-upload-protocol': 'resumable',
	'accept': '*/*',
	'x-goog-upload-command': 'start',
	'x-goog-upload-content-length': f'{imagesize}',
	'accept-language': 'vi-VN,vi;q=0.9',
	'x-firebase-storage-version': 'ios/10.13.0',
	'user-agent': 'com.locket.Locket/1.43.1 iPhone/17.3 hw/iPhone15_3 (GTMSUF/1)',
	'x-goog-upload-content-type': 'image/jpg, image/png, image/gif, image/jpeg, image/mp4,video/mp4,video/x-m4v,video/*',
	'x-firebase-gmpid': '1:641029076083:ios:cc8eb46290d69b234fa606'
}

data_img = '{"name":"users\\/e9yEHBoGlYgF1hfsbha8cX8iliw1\\/moments\\/thumbnails\\/'+nameimg+'","contentType":"image\\/webp","bucket":"","metadata":{"creator":"e9yEHBoGlYgF1hfsbha8cX8iliw1","visibility":"private"}}'
data_video = '{"name":"users\\/e9yEHBoGlYgF1hfsbha8cX8iliw1\\/moments\\/videos\\/'+namevideo+'","contentType":"video\\/mp4","bucket":"","metadata":{"creator":"e9yEHBoGlYgF1hfsbha8cX8iliw1","visibility":"private"}}'

url_img = 'https://firebasestorage.googleapis.com:443/v0/b/locket-img/o/users%2F'+localID+'%2Fmoments%2Fthumbnails%2F'+nameimg+'?uploadType=resumable&name=users%2F'+localID+'%2Fmoments%2Fthumbnails%2F'+nameimg+''
url_video = 'https://firebasestorage.googleapis.com:443/v0/b/locket-video/o/users%2F'+localID+'%2Fmoments%2Fvideos%2F'+namevideo+'?uploadType=resumable&name=users%2F'+localID+'%2Fmoments%2Fvideos%2F'+namevideo+''
# print(url)
res_img = requests.post(url_img, headers=head, data=data_img)
res_video = requests.post(url_video, headers=head, data=data_video)
# res = requests.post(url, headers=head, data=data)
# print(res.headers['X-Goog-Upload-URL'])
# sys.exit()


head = {
	
	'content-type': 'application/octet-stream',
	'x-goog-upload-protocol': 'resumable',
	'x-goog-upload-offset': '0',
	'x-goog-upload-command': 'upload, finalize',
	'upload-incomplete': '?0',
	'upload-draft-interop-version': '3',
	'user-agent': 'com.locket.Locket/1.43.1 iPhone/17.3 hw/iPhone15_3 (GTMSUF/1)'
}

res_upload_img = requests.put(res_img.headers['X-Goog-Upload-URL'], headers=head, data=data_uploads)
res_upload_video = requests.put(res_video.headers['X-Goog-Upload-URL'], headers=head, data=data_uploads)
# print(res.text)
# sys.exit()
downloadToken_img = res_upload_img.json()['downloadTokens']
downloadToken_video = res_upload_video.json()['downloadTokens']
# head = {
# 	'content-type': 'application/json; charset=UTF-8',
# 	'authorization': f'Firebase {response.json()['idToken']}',
# 	'accept': '*/*',
# 	'accept-language': 'vi-VN,vi;q=0.9',
# 	'user-agent': 'com.locket.Locket/1.43.1 iPhone/17.3 hw/iPhone15_3 (GTMSUF/1)',
# 	'x-firebase-gmpid': '1:641029076083:ios:cc8eb46290d69b234fa606'
# }

# ress = requests.get('https://firebasestorage.googleapis.com:443/v0/b/'+typeanh+'/o/users%2F'+localID+'%2Fmoments%2Fthumbnails%2F'+nameimg+'', headers=head)
# ress = requests.get('https://firebasestorage.googleapis.com:443/v0/b/'+typeanh+'/o/users%2F'+localID+'%2Fmoments%2Fvideos%2F'+nameimg+'', headers=head)
# downLoad_Token = ress.json()['downloadTokens']
# namecc = f'https://firebasestorage.googleapis.com/v0/b/{typeanh}/o/users%2F{localID}%2Fmoments%2Fthumbnails%2F{nameimg}?alt=media&token={downLoad_Token}'
# namecc = f'https://firebasestorage.googleapis.com/v0/b/{typeanh}/o/users%2F{localID}%2Fmoments%2Fvideos%2F{nameimg}?alt=media&token={downLoad_Token}'
# print(namecc)
# sys
# print(ress.text)
# sys.exit()

headers = {
	'content-type': 'application/json',
	'accept': '*/*',
	'authorization': f'Bearer {TokenAccount}',
	'accept-language': 'vi-VN,vi;q=0.9',
	'user-agent': 'com.locket.Locket/1.43.1 iPhone/17.3 hw/iPhone15_3'
}

caption = 'anh yêu em mãi mãi mãi mãi mãi mãi'
# data = '{"data":{"analytics":{"platform":"ios","google_analytics":{"app_instance_id":"7A58F101E5B043519DC9783D63D0A07F"},"amplitude":{"device_id":"5E1F6CFD-1FC9-4DED-82B1-03743DD1FE09","session_id":{"@type":"type.googleapis.com\\/google.protobuf.Int64Value","value":"1722307848648"}}},"thumbnail_url":"https:\\/\\/firebasestorage.googleapis.com:443\\/v0\\/b\\/'+typeanh+'\\/o\\/users%2F'+localID+'%2Fmoments%2Fthumbnails%2F'+nameimg+'?alt=media&token='+downLoad_Token+'","sent_to_all":false,"migration":{"database":"locket"},"recipients":["r77mY315k8OSFUHhe8jmV7Vq8rG2"],"md5":"b9e295674e4a3bb56d8e09ee78cc7749"}}';
# data = '{"data":{"thumbnail_url":"https:\\/\\/firebasestorage.googleapis.com:443\\/v0\\/b\\/'+typeanh+'\\/o\\/users%2F'+localID+'%2Fmoments%2Fthumbnails%2F'+nameimg+'?alt=media&token='+downLoad_Token+'","md5":"442ba709c9f061fb8f597c1fe993a6cf","migration":{"database":"locket"},"recipients":["e9yEHBoGlYgF1hfsbha8cX8iliw1"],"analytics":{"platform":"ios","google_analytics":{"app_instance_id":"7A58F101E5B043519DC9783D63D0A07F"},"amplitude":{"device_id":"5E1F6CFD-1FC9-4DED-82B1-03743DD1FE09","session_id":{"@type":"type.googleapis.com\\/google.protobuf.Int64Value","value":"1722326200769"}}},"sent_to_all":false,"caption":"'+caption+'","overlays":[{"data":{"text":"'+caption+'","text_color":"#FFFFFFE6","type":"standard","max_lines":{"value":"4","@type":"type.googleapis.com\\/google.protobuf.Int64Value"},"background":{"material_blur":"ultra_thin","colors":[]}},"overlay_id":"caption:standard","alt_text":"'+caption+'","overlay_type":"caption"}]}}'
data_video = '{"data":{"analytics":{"experiments":{"flag_4":{"value":"43","@type":"type.googleapis.com\\/google.protobuf.Int64Value"},"flag_10":{"@type":"type.googleapis.com\\/google.protobuf.Int64Value","value":"504"},"flag_22":{"value":"1203","@type":"type.googleapis.com\\/google.protobuf.Int64Value"},"flag_23":{"@type":"type.googleapis.com\\/google.protobuf.Int64Value","value":"400"},"flag_19":{"@type":"type.googleapis.com\\/google.protobuf.Int64Value","value":"51"},"flag_18":{"value":"1203","@type":"type.googleapis.com\\/google.protobuf.Int64Value"},"flag_16":{"@type":"type.googleapis.com\\/google.protobuf.Int64Value","value":"303"},"flag_15":{"value":"501","@type":"type.googleapis.com\\/google.protobuf.Int64Value"},"flag_14":{"@type":"type.googleapis.com\\/google.protobuf.Int64Value","value":"500"},"flag_25":{"@type":"type.googleapis.com\\/google.protobuf.Int64Value","value":"23"}},"amplitude":{"device_id":"5E1F6CFD-1FC9-4DED-82B1-03743DD1FE09","session_id":{"@type":"type.googleapis.com\\/google.protobuf.Int64Value","value":"1722327853004"}},"google_analytics":{"app_instance_id":"7A58F101E5B043519DC9783D63D0A07F"},"platform":"ios"},"thumbnail_url":"https:\\/\\/firebasestorage.googleapis.com:443\\/v0\\/b\\/locket-img\\/o\\/users%2F'+localID+'%2Fmoments%2Fthumbnails%2F'+nameimg+'?alt=media&token='+downloadToken_img+'","sent_to_all":true,"recipients":[],"video_url":"https:\\/\\/firebasestorage.googleapis.com:443\\/v0\\/b\\/locket-video\\/o\\/users%2F'+localID+'%2Fmoments%2Fvideos%2F'+namevideo+'?alt=media&token='+downloadToken_video+'","md5":"607a606f071f2e6f82205932737213efcccccc", "caption":"test nè","overlays":[{"data":{"background":{"material_blur":"ultra_thin","colors":[]},"text_color":"#FFFFFFE6","type":"standard","max_lines":{"@type":"type.googleapis.com\\/google.protobuf.Int64Value","value":"4"},"text":"test nè"},"overlay_id":"caption:standard","alt_text":"test nè","overlay_type":"caption"}]}}'

# dt = {
# 		"data":{
# 			"analytics":{
# 			"platform":"ios",
# 			"google_analytics":{
# 			"app_instance_id":"7A58F101E5B043519DC9783D63D0A07F"
# 		},
# 		"amplitude":{
# 			"device_id":"5E1F6CFD-1FC9-4DED-82B1-03743DD1FE09",
# 			"session_id":{
# 				"value":"1722321133084",
# 				"@type":"type.googleapis.com/google.protobuf.Int64Value"
# 				}
# 			}
# 		},
# 		"thumbnail_url":"https://firebasestorage.googleapis.com:443/v0/b/locket-img/o/users%2Fe9yEHBoGlYgF1hfsbha8cX8iliw1%2Fmoments%2Fthumbnails%2FP4dbiE9si4hgIveWkGOi.webp?alt=media&token=6cdb8308-8470-4ed9-b372-88e4bf180f07",
# 		"sent_to_all":false,
# 		"migration":{
# 			"database":"locket"
# 			},
# 		"recipients":[
# 			"r77mY315k8OSFUHhe8jmV7Vq8rG2"
# 		],
# 			"md5":"0ffa1b22fa084e4b5fa0accc6b190666"
# 		}
# }
res = requests.post("https://api.locketcamera.com/postMoment", headers=headers, data=data_video)
print(res.text)