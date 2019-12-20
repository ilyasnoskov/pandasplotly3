import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'nhtsa_traffic_fatalities')


QUERY = """
        SELECT * FROM `bigquery-public-data.nhtsa_traffic_fatalities.accident_2015`
        LIMIT 10
        """


df = bq_assistant.query_to_pandas(QUERY)

print(df.head(10))



#start_point_groupby = df.groupby(['day_of_weak'])['number_of_persons_in_motor_vehicles_in_transport_mvit'].count()

labels=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
values=['17','23','13','9','10','3','11']
fig=go.Figure(data=[go.Pie(labels=labels,values=values)])
plot(fig)


#fig = {
 #   "data":[
  #          "y": start_point_groupby.values,
   #         "x": start_point_groupby.index
    #        "name": "day of weak"
     #       "type": "bar"
      #      ]

       # }
#plot(fig)


trace1 = go.Scatter(

                    )



trace2 = go.Pie(

                    )

trace3 = go.Bar(

)

data = [trace1]

layout = dict(
              title = '',
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)