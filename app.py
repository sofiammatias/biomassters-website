import streamlit as st
import datetime
import requests
import pandas as pd



'''
# TaxiFare Model
'''

st.markdown('''
This is a model to estimate/predict taxi fare rides in NY city
''')

today = datetime.date.today()
now = datetime.datetime.now()

col1, col2 = st.columns(2)

with col1:
    date = st.date_input("Date", today)

with col2:
    time = st.time_input('Time', now.time())

col1, col2, col3, col4 = st.columns(4)

with col1:
    pickup_lat = st.number_input('Pickup Latitude', 40.783282)

with col2:
    pickup_long = st.number_input('Pickup Longitude', -73.950655)

with col3:
    dropoff_lat = st.number_input('Dropoff Latitude', 40.769802)

with col4:
    dropoff_long = st.number_input('Dropoff Longitude', -73.984365)


passengers = st.slider('Select number of passengers', 1, 8, 2)

# Calling API URL

url = 'https://taxifare-wsbi2k6wha-ew.a.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


url_req = f"""https://taxifare-wsbi2k6wha-ew.a.run.app/predict?pickup_datetime={date} {time}&pickup_longitude={pickup_long}&pickup_latitude={pickup_lat}&dropoff_longitude={dropoff_long}&dropoff_latitude={dropoff_lat}&passenger_count={passengers}"""

fare = requests.get(url_req)

final_fare = round (float(fare.text.split(':')[1].replace('}', '').strip()), ndigits=2)
# fare = 5.4

st.markdown (f"""## Fare Estimation: ${final_fare}""")

df = pd.DataFrame(
    [[pickup_lat, pickup_long],[dropoff_lat, dropoff_long]],
    columns=['lat', 'lon'])

st.map(df)

# 2. Let's build a dictionary containing the parameters for our API...
# 3. Let's call our API using the `requests` package...
# 4. Let's retrieve the prediction from the **JSON** returned by the API...
## Finally, we can display the prediction to the user
