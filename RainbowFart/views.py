from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import random
import json
import time
import urllib.request
import urllib.parse
import hashlib
import base64



def main():
	
	return

# Create your views here.
def index(request):
	try:
		return render(request,'RainbowFart/index.html')
	except Exception as e:
		print(e)
		raise e

def rainbowFart(son):
	sons=['王一博','肖战']
	characters=['好帅','好酷','超帅','超酷','可爱','体面','懂事','善良','有礼貌','坚强','强大']
	skills=['唱歌好听','演技超棒','跳舞好看','有舞台感','温婉居家','不卑不亢']
	skillsForBo=['会骑摩托','会玩滑板','rap好听']
	skillsForZan=['画画好看','会做设计','做饭好吃']
	bless=['开心每一天','健健康康','顺顺利利','平安喜乐','诸事顺利','岁岁年年，万喜万般宜','幸福安康','越来越好','万事顺遂','平安顺遂','平安健康','万事胜意']
	emoji=['[爱你]','[鼓掌]','[亲亲]','[舔屏]','[憧憬]','[鲜花]','[赞]','[good]','[哆啦A梦微笑]','[哆啦A梦笑]','[哆啦A梦亲亲]','[小黄人高兴]','[米奇喜欢]','[给你小心心]']
	tagsForBo=['#王一博平安喜乐#','#王一博#','#王一博冰雨火#','#王一博有翡#','#王一博这就是街舞3#','#王一博天天向上#','#王一博代言肯德基#','#王一博夏日冲浪店#','#王一博 喜马拉雅爱的代言人#']
	tagsForZan=['#肖战平安喜乐#','#肖战#','#肖战斗罗大陆#','#肖战余生请多指教#','#肖战正能量艺人#','#肖战公益一路有你#','#肖战为你开小灶#','#支持肖战代言#','#支持肖战影视综艺#']
	if(son=='b'):
		rainbow_Fart=[sons[0]+'真的',characters[random.randint(0,len(characters)-1)]+emoji[random.randint(0,len(emoji)-1)]*random.randint(0,4)
			+'，而且'+skills[random.randint(0,len(skills)-1)]+emoji[random.randint(0,len(emoji)-1)]*random.randint(0,4)
			+'、'+skillsForBo[random.randint(0,len(skillsForBo)-1)]+emoji[random.randint(0,len(emoji)-1)]*random.randint(0,4)
			+'，希望你永远'+bless[random.randint(0,len(bless)-1)]+emoji[random.randint(0,len(emoji)-1)]*random.randint(0,4)
			+tagsForBo[random.randint(0,len(tagsForBo)-1)]+emoji[random.randint(0,len(emoji)-1)]
			+tagsForBo[random.randint(0,len(tagsForBo)-1)]]
		return ''.join(rainbow_Fart)
	elif(son=='z'):
		rainbow_Fart=[sons[1]+'真的',characters[random.randint(0,len(characters)-1)]+emoji[random.randint(0,len(emoji)-1)]*random.randint(0,4)
			+'，而且'+skills[random.randint(0,len(skills)-1)]+emoji[random.randint(0,len(emoji)-1)]*random.randint(0,4)
			+'，'+skillsForZan[random.randint(0,len(skillsForZan)-1)]+emoji[random.randint(0,len(emoji)-1)]*random.randint(0,4)
			+'，希望你永远'+bless[random.randint(0,len(bless)-1)]+emoji[random.randint(0,len(emoji)-1)]*random.randint(0,4)
			+tagsForZan[random.randint(0,len(tagsForZan)-1)]+emoji[random.randint(0,len(emoji)-1)]
			+tagsForZan[random.randint(0,len(tagsForZan)-1)]]
		return ''.join(rainbow_Fart)

@ensure_csrf_cookie
def getText(request):
	try:
		if (request.method=='POST'):
			son = json.loads(request.body.decode())
			return HttpResponse(rainbowFart(son['son']))
	except Exception as e:
		print(e)
		raise e

@ensure_csrf_cookie
def analyzeText(request):
	try:
		if (request.method=='POST'):
			rf_text=json.loads(request.body.decode())
			#接口地址
			url ="http://ltpapi.xfyun.cn/v2/sa"
			#开放平台应用ID
			x_appid = "5f0689df"
			#开放平台应用接口秘钥
			api_key = "01071dbe41703a7008cfcddd74e78ffc"
			#语言文本
			TEXT=rf_text['text']
			print(TEXT)
			body = urllib.parse.urlencode({'text': TEXT}).encode('utf-8')
			param = {"type": "dependent"}
			x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
			x_time = str(int(time.time()))
			x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
			x_header = {'X-Appid': x_appid,
						'X-CurTime': x_time,
						'X-Param': x_param,
						'X-CheckSum': x_checksum}
			req = urllib.request.Request(url, body, x_header)
			result = urllib.request.urlopen(req)
			result = result.read()
			result=eval(result.decode('utf-8'))
			print(result['data'])
			return HttpResponse(json.dumps(result['data']))
	except Exception as e:
		print(e)
		raise e