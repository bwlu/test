from django.views import View
from ..utils import (
    correct_response, err_response_with_desc,generate_list_dict,check_login
)
import time, os, random

BASE_DIR = os.path.abspath(__file__)

class ImageUpload(View):
	def post(self,request):
		file = request.FILES.get('file', None)
		date_str = time.strftime("%Y%m%d", time.localtime())
		time_str = str(round(time.time() * 1000))
		file_path = os.path.abspath(os.path.join(BASE_DIR, '../../../..', 'static', 'UpLoadFiles', date_str))
		if not os.path.exists(file_path):
			os.makedirs(file_path) 
		file_path = file_path + '\\' +date_str+time_str+'.'+file.name.split('.')[1]
		with open(file_path, 'wb') as f:
			for chunk in file.chunks():
				f.write(chunk)
		try:
			return correct_response({"url": date_str +'/' + date_str+time_str+'.'+file.name.split('.')[1]})
		except Exception as e:
			print(e)
			return err_response_with_desc('图片上传失败')
