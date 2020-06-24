'''
python+Bootstrap+flask+calendar制作日历
https://mp.weixin.qq.com/s/FcxqVr7Uw3dp75eep8bOiQ
'''

from flask import Flask, render_template, request, session, redirect, url_for
import calendar
from datetime import datetime

calendar.setfirstweekday(firstweekday=6)
app = Flask(__name__)

week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']

def calc_calendar(date):
	year = date.year
	yearInfo = dict()
	for month in range(1, 13):
		days = calendar.monthcalendar(year, month)
		if len(days) != 6:
			days.append([0 for _ in range(7)])
		month_addr = calendar.month_abbr[month]
		yearInfo[month_addr] = days
	return yearInfo

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "GET":
		date = datetime.today()
		this_month = calendar.month_abbr[date.month]
		return render_template('index.html', this_month=this_month, date=date, content=calc_calendar(date))

if __name__ == '__main__':
	app.run(debug=True)