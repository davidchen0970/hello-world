from flask import Flask, request, abort

from linebot import (	LineBotApi, WebhookHandler)
from linebot.exceptions import (	InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('pLL9E0czj5PQExM0uVof8+Nnjz4ZnBMPxAwRu1oGhTxw0BycZwuC9QJ0Al2y908g3eDxRciFYEHGhnmJAMbKEiwscbKeLZoECbPB16cQEG6Lj2kSo2JkyYTC7VJYe6qpLhaMriBvcn9XTtOq4X44DwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('e16230f50eb13248c20795144d70fab0')



# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
	# get X-Line-Signature header value
	signature = request.headers['X-Line-Signature']
	# get request body as text
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)
	# handle webhook body
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	if event.message.text == "宿舍":
		message = TemplateSendMessage(alt_text='Buttons template',
		template=ButtonsTemplate(thumbnail_image_url='https://www.ncyu.edu.tw/newsite/logo_ncyu_header.gif',
			title='宿舍',
			text='宿舍功能',
			actions=[URITemplateAction(label='宿舍網路',
					uri='http://sflow.ncyu.edu.tw/'),
				URITemplateAction(label='網路報修',
					uri='https://dormfix.ncyu.edu.tw/'),
				URITemplateAction(label='抽籤名單',
					uri='https://www.ncyu.edu.tw/dorm/bulletin.aspx?bulletin_sn=51911')]))
	if event.message.text == "其他":
		message = TemplateSendMessage(alt_text='Buttons template',
		template=ButtonsTemplate(thumbnail_image_url='https://www.ncyu.edu.tw/newsite/logo_ncyu_header.gif',
			title='其他功能',
			text='雜項啦 有懂嗎',
			actions=[MessageTemplateAction(label='暑修通知',
				text='暑修通知'),
				MessageTemplateAction(label='行事曆 中文',
				text='行事曆'),
				MessageTemplateAction(label='Calendar',
				text='Calendar'),
				URITemplateAction(label='專題',
					uri='https://docs.google.com/spreadsheets/d/1A55reNqwri9qFt33OY7d2fov0Ga23t4UtwUlZB8UDuQ/edit#gid=0')]))
	if event.message.text == "課表":
		message = TemplateSendMessage(alt_text='Buttons template',
		template=ButtonsTemplate(thumbnail_image_url='https://www.ncyu.edu.tw/newsite/logo_ncyu_header.gif',
			title='課表',
			text='課表',
			actions=[MessageTemplateAction(label='大一課表',
				text='大一課表'),
				MessageTemplateAction(label='大二課表',
				text='大二課表'),
				MessageTemplateAction(label='大三課表',
				text='大三課表'),
				MessageTemplateAction(label='大四課表',
				text='大四課表')]))

	if event.message.text == "資工" or event.message.text == "資訊工程" or event.message.text == "資訊工程學系" or event.message.text == "嘉大資工":
		message = FlexSendMessage(alt_text='資訊工程學系',
	contents={
  "type": "bubble",
  "direction": "ltr",
  "header": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "text",
		"text": "國立嘉義大學 資訊工程學系",
		"size": "lg",
		"align": "center",
		"contents": []
	  }
	]
  },
  "hero": {
	"type": "image",
	"url": "https://scontent-tpe1-1.xx.fbcdn.net/v/t31.18172-8/13653238_1088614404525791_4445453163975429548_o.jpg?_nc_cat=105&ccb=1-3&_nc_sid=09cbfe&_nc_ohc=IldMZRTIBpYAX9NOBW_&_nc_ht=scontent-tpe1-1.xx&oh=7563db2c7f7db9d9cab44954613819bd&oe=60990C23",
	"size": "full",
	"aspectRatio": "1.51:1",
	"aspectMode": "fit"
  },
  "body": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "box",
		"layout": "horizontal",
		"contents": [
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "學系網頁",
			  "uri": "https://www.ncyu.edu.tw/csie/"
			},
			"height": "sm"
		  },
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "粉絲專頁",
			  "uri": "https://www.facebook.com/CSIE.NCYU/"
			},
			"height": "sm"
		  }
		]
	  },
	  {
		"type": "box",
		"layout": "horizontal",
		"backgroundColor": "#DCDFE5",
		"contents": [
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "資工系學會",
			  "uri": "https://www.facebook.com/ncyucsie/"
			},
			"height": "sm",
			"style": "secondary"
		  },
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "系學會LINE",
			  "uri": "https://page.line.me/?accountId=395tijwm&openerPlatform=native&openerKey=talkroom:message"
			},
			"height": "sm",
			"style": "secondary"
		  }
		]
	  },
	  {
		"type": "separator"
	  },
	  {
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "新生專欄",
		  "uri": "https://www.ncyu.edu.tw/csie/gradation.aspx?site_content_sn=50268"
		},
		"height": "sm"
	  },
	  {
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "專題園地",
		  "uri": "https://www.ncyu.edu.tw/csie/gradation.aspx?site_content_sn=49968"
		},
		"height": "sm",
		"style": "secondary"
	  },
	  {
		"type": "button",
		"action": {
		  "type": "message",
		  "label": "教授列表",
		  "text": "教授列表"
		},
		"height": "sm"
	  }
	]
  }
})
	if event.message.text == "test":
		message = FlexSendMessage(alt_text='hello',
	contents={
		"type": "bubble",
		"body": {
			"type": "box",
			"layout": "vertical",
			"spacing": "sm",
			"contents": [{
				"type": "button",
				"action": {
					"type": "uri",
					"label": "See more",
					"uri": "https://www.google.com"
				},
			"flex": 1,
			"gravity": "center"
			}]
		}
	})
	if event.message.text == "實用功能":
		message = FlexSendMessage(alt_text='hello',
	contents={
  "type": "bubble",
  "direction": "ltr",
  "header": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "text",
		"text": "實用功能",
		"align": "center",
		"contents": []
	  }
	]
  },
  "hero": {
	"type": "image",
	"url": "https://i.imgur.com/g4jnJr0.jpg",
	"size": "full",
	"aspectRatio": "1.51:1",
	"aspectMode": "fit"
  },
  "body": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "text",
		"text": "嘉義大學 資工beta版功能",
		"align": "center",
		"contents": []
	  }
	]
  },
  "footer": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "button",
		"action": {
		  "type": "message",
		  "label": "資工資訊",
		  "text": "資工"
		},
		"height": "sm",
		"style": "secondary"
	  },
	  {
		"type": "button",
		"action": {
		  "type": "message",
		  "label": "學校功能",
		  "text": "學校"
		},
		"height": "sm"
	  },
	  {
		"type": "button",
		"action": {
		  "type": "message",
		  "label": "資工課表",
		  "text": "課表"
		},
		"height": "sm",
		"style": "secondary"
	  },
	  {
		"type": "button",
		"action": {
		  "type": "message",
		  "label": "宿舍功能",
		  "text": "宿舍"
		},
		"height": "sm"
	  },
	  {
		"type": "button",
		"action": {
		  "type": "message",
		  "label": "行事曆",
		  "text": "行事曆"
		},
		"height": "sm",
		"style": "secondary"
	  },
	  {
		"type": "button",
		"action": {
		  "type": "message",
		  "label": "各科資料",
		  "text": "各科資料"
		},
		"height": "sm"
	  },
	  {
		"type": "text",
		"text": "beta 2021.4.16",
		"contents": []
	  }
	]
  }
})
	if event.message.text == "學校":
		message = FlexSendMessage(alt_text="嘉義大學",
			contents={
  "type": "bubble",
  "direction": "ltr",
  "header": {
	"type": "box",
	"layout": "vertical",
	"contents": [{
		"type": "text",
		"text": "國立嘉義大學",
		"weight": "bold",
		"align": "center",
		"contents": []
	  }]
  },
  "hero": {
	"type": "image",
	"url": "https://i.imgur.com/3LiJqS9.jpg",
	"size": "full",
	"aspectRatio": "1.51:1",
	"aspectMode": "fit"
  },
  "footer": {
	"type": "box",
	"layout": "vertical",
	"contents": [{
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "學校首頁",
		  "uri": "https://www.ncyu.edu.tw/newsite/index.aspx"
		},
		"style": "secondary"
	  },
	  {
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "E化校園",
		  "uri": "https://www.ncyu.edu.tw/newsite/gradation.aspx?site_content_sn=8314"
		}
	  },
	  {
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "校務行政系統",
		  "uri": "https://web085004.adm.ncyu.edu.tw/NewSite/login.aspx?Language=zh-TW"
		},
		"style": "secondary"
	  },
	  {
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "教學輔助平台",
		  "uri": "https://ecourse.ncyu.edu.tw/"
		}
	  }]
  }
})
	if event.message.text == "教授" or event.message.text == "教授列表":
		message = FlexSendMessage(alt_text="教授列表",
			contents=
				{
  "type": "bubble",
  "direction": "ltr",
  "body": {
	"type": "box",
	"layout": "vertical",
	"spacing": "sm",
	"contents": [{
		"type": "text",
		"text": "教授",
		"contents": []
	  },
	  {
		"type": "box",
		"layout": "horizontal",
		"contents": [{
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "柯建全 教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52978"
			}
		  },
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "章定遠 教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52979"
			}
		  }]
	  },
	  {
		"type": "box",
		"layout": "horizontal",
		"contents": [{
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "葉瑞峰  教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52982"
			}
		  },
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "邱志義 教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52983"
			}
		  }]
	  },
	  {
		"type": "box",
		"layout": "horizontal",
		"contents": [{
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "陳宗和  教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52984"
			}
		  },
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "許政穆  教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52986"
			}
		  }]
	  },
	  {
		"type": "box",
		"layout": "horizontal",
		"contents": [{
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "王智弘  教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52985"
			}
		  },
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "洪燕竹  教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52980"
			}
		  }]
	  },
	  {
		"type": "separator"
	  },
	  {
		"type": "text",
		"text": "副教授",
		"contents": []
	  },
	  {
		"type": "box",
		"layout": "horizontal",
		"contents": [{
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "賴泳伶 教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52974"
			}
		  },
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "陳耀輝 教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52975"
			}
		  }]
	  },
	  {
		"type": "box",
		"layout": "horizontal",
		"contents": [{
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "林楚迪 教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52976"
			}
		  },
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "盧天麒  教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52981"
			}
		  }]
	  },
	  {
		"type": "separator"
	  },
	  {
		"type": "text",
		"text": "助理教授",
		"contents": []
	  },
	  {
		"type": "box",
		"layout": "horizontal",
		"contents": [{
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "郭煌政 教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52977"
			}
		  },
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "李龍盛 教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52988"
			}
		  }]
	  },
	  {
		"type": "box",
		"layout": "horizontal",
		"contents": [{
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "王皓立 教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=52989"
			}
		  },
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "方文杰 教授",
			  "uri": "https://www.ncyu.edu.tw/csie/content.aspx?site_content_sn=62024"
			}
		  }]
	  }]
  }
})
	if event.message.text == "程式":
		message = FlexSendMessage(alt_text="打程式",
			contents={
  "type": "bubble",
  "direction": "ltr",
  "header": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "text",
		"text": "打程式",
		"align": "center",
		"contents": []
	  }
	]
  },
  "hero": {
	"type": "image",
	"url": "https://i.imgur.com/YVEI5WY.jpg",
	"size": "4xl",
	"aspectRatio": "1.51:1",
	"aspectMode": "fit"
  },
  "body": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "separator"
	  },
	  {
		"type": "box",
		"layout": "horizontal",
		"contents": [
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "zerojudge",
			  "uri": "https://zerojudge.tw/"
			},
			"height": "sm"
		  },
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "翼世界夢想領域(解答)",
			  "uri": "https://knightzone.studio/tag/zerojudge/"
			},
			"height": "sm"
		  }
		]
	  },
	  {
		"type": "box",
		"layout": "horizontal",
		"backgroundColor": "#DCDFE5",
		"contents": [
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "UVa",
			  "uri": "https://onlinejudge.org/"
			},
			"height": "sm",
			"style": "secondary"
		  },
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "udebug",
			  "uri": "https://www.udebug.com/"
			},
			"height": "sm",
			"style": "secondary"
		  }
		]
	  },
	  {
		"type": "box",
		"layout": "horizontal",
		"contents": [
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "CPE",
			  "uri": "https://cpe.cse.nsysu.edu.tw/"
			},
			"height": "sm"
		  },
		  {
			"type": "button",
			"action": {
			  "type": "uri",
			  "label": "CPE 報名",
			  "uri": "https://cpe.cse.nsysu.edu.tw/cpe/newest"
			},
			"height": "sm"
		  }
		]
	  },
	  {
		"type": "separator"
	  },
	  {
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "LeetCode",
		  "uri": "https://leetcode.com/"
		},
		"height": "sm"
	  },
	  {
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "LintCode",
		  "uri": "https://www.lintcode.com/"
		},
		"height": "sm",
		"style": "secondary"
	  },
	  {
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "CodeWars",
		  "uri": "https://www.codewars.com/"
		},
		"height": "sm"
	  },
	  {
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "ITSA",
		  "uri": "https://e-tutor.itsa.org.tw/e-Tutor/"
		},
		"height": "sm",
		"style": "secondary"
	  }
	]
  }
})
	if event.message.text == "各科資料":

		message=FlexSendMessage(alt_text="peko",
			contents={
  "type": "bubble",
  "direction": "ltr",
  "header": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "text",
		"text": "peko",
		"weight": "bold",
		"size": "xl",
		"align": "center",
		"contents": []
	  }
	]
  },
  "hero": {
	"type": "image",
	"url": "https://img.komicolle.org/2020-06/15934331564720.jpg",
	"gravity": "center",
	"size": "full",
	"aspectRatio": "1.51:1",
	"aspectMode": "cover",
	"position": "relative"
  },
  "body": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "text",
		"text": "神奇的百寶袋",
		"align": "center",
		"contents": []
	  }
	]
  },
  "footer": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "box",
		"layout": "horizontal",
		"contents": [
		  {
			"type": "button",
			"action": {
			  "type": "message",
			  "label": "大一上",
			  "text": "大一上"
			}
		  },
		  {
			"type": "button",
			"action": {
			  "type": "message",
			  "label": "大一下",
			  "text": "大一下"
			}
		  }
		]
	  },
	  {
		"type": "box",
		"layout": "horizontal",
		"contents": [
		  {
			"type": "button",
			"action": {
			  "type": "message",
			  "label": "大二上",
			  "text": "大二上"
			}
		  },
		  {
			"type": "button",
			"action": {
			  "type": "message",
			  "label": "大二下",
			  "text": "大二下"
			}
		  }
		]
	  },
	  {
		"type": "text",
		"text": "beta 2021.4.16",
		"contents": []
	  }
	]
  }
}
		)
	if event.message.text == "大二下":
		message = FlexSendMessage(alt_text="大二下",
			contents={
  "type": "bubble",
  "direction": "ltr",
  "header": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "text",
		"text": "大二下",
		"align": "center",
		"contents": []
	  }
	]
  },
  "hero": {
	"type": "image",
	"url": "https://i.imgur.com/YVEI5WY.jpg",
	"size": "full",
	"aspectRatio": "1.51:1",
	"aspectMode": "fit"
  },
  "body": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "程式語言學",
		  "uri": "https://drive.google.com/drive/folders/1TJWkjezFnS5MdkSRvbyvqLP8M-nim0lq?usp=sharing"
		}
	  },
	  {
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "演算法",
		  "uri": "https://drive.google.com/drive/folders/1vU4B3THjEZ5NDkwNboJjWs56Rwp_FhUx?usp=sharing"
		}
	  },
	  {
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "機率學",
		  "uri": "https://drive.google.com/drive/folders/1YuJoilXzZHO-GntVsw0OUCsM3XVVrprO?usp=sharing"
		}
	  },
	  {
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "資料庫",
		  "uri": "https://drive.google.com/drive/folders/1HHsNIxCcqRoy67y2q2aNuAmvqb5XIG2t?usp=sharing"
		}
	  },
	  {
		"type": "button",
		"action": {
		  "type": "uri",
		  "label": "你想幫助我的資料更完整",
		  "uri": "https://drive.google.com/drive/folders/1CXdhFlcet0CKBB-jrXXO0RpxvRzFbMK9?usp=sharing"
		}
	  },
	  {
		"type": "text",
		"text": "beta 2021.4.15",
		"contents": []
	  }
	]
  }
}
			)
	if event.message.text == "大二上":
		message = FlexSendMessage(alt_text="大二下",
			contents={
  "type": "bubble",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "大二上",
        "align": "center",
        "contents": []
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/iwpWyxD.jpg",
    "size": "full",
    "aspectRatio": "1.51:1",
    "aspectMode": "fit"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "計算機網路",
          "uri": "https://drive.google.com/drive/folders/1nKSmjh6ZRU33dwTJ0SPS8PxfI8tVxoJ7?usp=sharing"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "資料結構",
          "uri": "https://drive.google.com/drive/folders/1qcaCYluNuYF_QPbAA-6vboPtCKTzNPeZ?usp=sharing"
        },
        "style": "secondary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "資料壓縮",
          "uri": "https://drive.google.com/drive/folders/1IJLcTLo1u8hr3ehgL42Xgjhe2Fbk96W6?usp=sharing"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "數位系統",
          "uri": "https://drive.google.com/drive/folders/1NpgG5TxfVNl-QbTJmMfq5kgjgRQuvBuv?usp=sharing"
        },
        "style": "secondary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "數位系統實習",
          "uri": "https://drive.google.com/drive/folders/1YA95IkWZWljWYs7NKfuh_35J6gDoCKuF?usp=sharing"
        }
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "beta 2021.4.16",
        "contents": []
      }
    ]
  }
})
	if event.message.text == "大一下":
		message = FlexSendMessage(alt_text="大一下",
			contents={
  "type": "bubble",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "大一下",
        "align": "center",
        "contents": []
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/9VzVGJ3.png",
    "size": "full",
    "aspectRatio": "1.51:1",
    "aspectMode": "fit"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "物件導向程式設計",
          "uri": "https://drive.google.com/drive/folders/17sD6TMCyawRTt51R580xlL_-YwNigaoa?usp=sharing"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "程式設計",
          "uri": "https://drive.google.com/drive/folders/1jom1aHvbhqBk3utpO7MXWyiCrbVbHIRm?usp=sharing"
        },
        "style": "secondary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "電子電路學",
          "uri": "https://drive.google.com/drive/folders/1XnbkWAZqVLVx2kqUKi345PVH-jgTYKFu?usp=sharing"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "電子電路學實驗",
          "uri": "https://drive.google.com/drive/folders/1ZvN_XpH4jZuIq5AuV2sqdEixwLZcCsLK?usp=sharing"
        },
        "style": "secondary"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "離散數學",
          "uri": "https://drive.google.com/drive/folders/1H_hRN2dESMC8FFqAT8FLaD-Ku0R-dm_q?usp=sharing"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "願意幫助我的資料更完整",
          "uri": "https://drive.google.com/drive/folders/1CXdhFlcet0CKBB-jrXXO0RpxvRzFbMK9?usp=sharing"
        },
        "style": "secondary"
      },
      {
        "type": "text",
        "text": "beta 2021.4.16",
        "contents": []
      }
    ]
  }
})
	if event.message.text == "大一上":
		message = FlexSendMessage(alt_text="大一上",
			contents={
  "type": "bubble",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "大一上",
        "align": "center",
        "contents": []
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/YVEI5WY.jpg",
    "size": "full",
    "aspectRatio": "1.51:1",
    "aspectMode": "fit"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "計算機概論",
          "uri": "https://drive.google.com/drive/folders/1V0NT2Nme3iLHtPvquTBZX0JeuSmHD_nI?usp=sharing"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "程式設計",
          "uri": "https://drive.google.com/drive/folders/1jom1aHvbhqBk3utpO7MXWyiCrbVbHIRm?usp=sharing"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "微積分1",
          "uri": "https://drive.google.com/drive/folders/1w341WEsmqlwFB8dR9XawjX7lQBBR0Vmw?usp=sharing"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "線性代數",
          "uri": "https://drive.google.com/drive/folders/1SRnv9_k6fTOBl6he_CqVjNeZQEJ1IZKk?usp=sharing"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "願意幫助我的資料更完整",
          "uri": "https://drive.google.com/drive/folders/1CXdhFlcet0CKBB-jrXXO0RpxvRzFbMK9?usp=sharing"
        }
      },
      {
        "type": "text",
        "text": "beta 2021.4.16",
        "contents": []
      }
    ]
  }
})
	line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)


#依次回復多則訊息
#reply_arr=[]
#reply_arr.append( TextSendMessage(......) )
#reply_arr.append( TextSendMessage(......) )
#line_bot_api.reply_message( token, reply_arr )
