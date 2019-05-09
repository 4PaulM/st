import os
from bottle import route, run, view, redirect, request, static_file

x = {1:"Text"}
y = 111

@route("/addinfo", method = "POST")
def info():
	inf = str(request.POST.inputinfo.strip())
	key = (max(x.keys()))+1
	x[key]=inf
	i = request.POST.info1.strip()
	y = i
	return redirect("/")

@route("/h")
@view("h")
def logic():
	return{"infor":x,"id":y}

@route("/api/<k>")
def delete(k):
	return {"infor":x,"id":y}

@route("/api/delete/<u>")
def delete(u):
	u = int(u)
	del x[u]
	return redirect("/")

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)