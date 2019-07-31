import markdown
import json
import shutil
import os

template = open("template.html", "r").read()

# build about page
raw_text = open("about.md", "r").read()
html = template.replace("<!-- Fill in template here -->", markdown.markdown(raw_text))
file = open("about.html", "w")
file.write(html)
file.close()
shutil.copyfile("about.html", "../about/index.html")
images = os.listdir("about_images")
for image in images:
	shutil.copyfile("about_images/" + image, "../about/" + image)

#build services page
services = json.loads(open("services.json", "r").read())["services"]
images = [s["image"] for s in services]

html = ""
for service in services:
	html += "<a href=\"" + service["link"] + "\">"
	html += "<span class=\"service mh2 grow code\">"
	html += "<p class=\"dib center\">" + service["name"] + "</p>"
	html += "<img src=\"" + service["image"] + "\">"
	html += "<div class=\"launch code\">"
	html += "<p class=\"ttu code\">" + service["optional_text"] + "</p>"
	html += "</div>"
	html += "</span>"
	html += "</a>"
file = open("services.html", "w")
html = template.replace("<!-- Fill in template here -->", html)
file.write(html)
file.close()
shutil.copyfile("services.html", "../services/index.html")
for image in images:
	shutil.copyfile("service_images/" + image, "../services/" + image)

#build data page
data = json.loads(open("data.json", "r").read())["data"]
images = [d["image"] for d in data]

html = ""
for d in data:
	html += "<a href=\"" + d["link"] + "\">"
	html += "<span class=\"service mh2 grow code\">"
	html += "<p class=\"dib center\">" + d["name"] + "</p>"
	html += "<img src=\"" + d["image"] + "\">"
	html += "<div class=\"launch code\">"
	html += "<p class=\"ttu code\">" + d["optional_text"] + "</p>"
	html += "</div>"
	html += "</span>"
	html += "</a>"
file = open("data.html", "w")
html = template.replace("<!-- Fill in template here -->", html)
file.write(html)
file.close()
shutil.copyfile("data.html", "../data/index.html")
for image in images:
	shutil.copyfile("data_images/" + image, "../data/" + image)

#build software page
software = json.loads(open("software.json", "r").read())["software"]
images = [s["image"] for s in software]

html = ""
for s in software:
	html += "<a href=\"" + s["link"] + "\">"
	html += "<span class=\"service mh2 grow code\">"
	html += "<p class=\"dib center\">" + s["name"] + "</p>"
	html += "<img src=\"" + s["image"] + "\">"
	html += "<div class=\"launch code\">"
	html += "<p class=\"ttu code\">" + s["optional_text"] + "</p>"
	html += "</div>"
	html += "</span>"
	html += "</a>"
file = open("software.html", "w")
html = template.replace("<!-- Fill in template here -->", html)
file.write(html)
file.close()
shutil.copyfile("software.html", "../software/index.html")
for image in images:
	shutil.copyfile("software_images/" + image, "../software/" + image)

#build thanks page
raw_text = open("thanks.md", "r").read()
html = template.replace("<!-- Fill in template here -->", markdown.markdown(raw_text))
file = open("thanks.html", "w")
file.write(html)
file.close()
shutil.copyfile("thanks.html", "../thanks/index.html")
images = os.listdir("thanks_images")
for image in images:
	shutil.copyfile("thanks_images/" + image, "../thanks/" + image)

#copy news items
news_files = os.listdir("news_files")
for news_file in news_files:
	if "~" in news_file:
		os.remove("news_files/" + news_file)
news_files = os.listdir("/users/claw/code/realfast_services/news/news_files")
for news_file in news_files:
	os.remove("/users/claw/code/realfast_services/news/news_files/" + news_file)
news_files = os.listdir("news_files")
for news_file in news_files:
	shutil.copyfile("news_files/" + news_file, "/users/claw/code/realfast_services/news/news_files/" + news_file)

#clean up directory
os.remove("about.html")
os.remove("services.html")
os.remove("data.html")
os.remove("software.html")
os.remove("thanks.html")
