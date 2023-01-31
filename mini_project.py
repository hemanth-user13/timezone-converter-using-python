### mini project for time zone converter
## here we will use pytz and date time librarary to convert and check the time of various places using python
### for the time zone info refer this following link "https://www.zeitverschiebung.net/en/city/1835848"
import pytz , datetime
 
year=int(input())
month=int(input())
day=int(input())
hour=int(input())
minute=int(input())

## converting to a date
user_time=datetime.datetime(year,month,day,hour,minute)
cairo_timezone=pytz.timezone('Africa/cairo')
london_timezone=pytz.timezone('UTC')
delhi_timezone=pytz.timezone('Asia/Kolkata')
sydney_timezone=pytz.timezone('Australia/Sydney')
tokyo_timezone=pytz.timezone('Asia/Tokyo')
seoul_timezone=pytz.timezone('Asia/seoul')


cairo_time=pytz.utc.localize(user_time).astimezone(cairo_timezone)
london_time=pytz.utc.localize(user_time).astimezone(london_timezone)
delhi_time=pytz.utc.localize(user_time).astimezone(delhi_timezone)
sydney_time=pytz.utc.localize(user_time).astimezone(sydney_timezone)
tokyo_time=pytz.utc.localize(user_time).astimezone(tokyo_timezone)
seoul_time=pytz.utc.localize(user_time).astimezone(tokyo_timezone)

print("Cairo Time is",cairo_time.isoformat())
print("London Time is",london_time.isoformat())
print("New Delhi Time is",delhi_time.isoformat())
print("Sydney Time is",sydney_time.isoformat())
print("Tokyo Time is",tokyo_time.isoformat())
print("Seoul Time is",seoul_time.isoformat())




