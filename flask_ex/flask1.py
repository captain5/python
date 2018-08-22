from flask import Flask
from flask import request
 
app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
# def home():
  # return '<h1>Home</h1>'
 
@app.route('/', methods=['GET'])
def sn_form():
  return '''<div align="center"> <form action="/" method="post">
		<label>SN:</label>
		<input name="sn" type="text">
		<input type="submit">
		</form>'''


@app.route('/', methods=['POST'])
def get_sn():
	# 需要从request对象读取表单内容：
	sn0 = './mk -s ' + request.form("sn")
	print sn0
	output = os.popen(sn0)
	return '<h1> SN:\n %s </h1>' % output.read()
 
# 默认只能本机访问 
# if __name__ == '__main__':
  # app.run()

# 其他电脑也可以访问，并且此处可修改端口
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

