#Step 0: Check whether pip is installed by typing pip --version or pip3 --version
#Step 1: If it not installed type sudo apt install python3-pip -y
#Step 2: Now, type pip3 install -r requirements.txt which install google-cloud-bigquery module
#Step 3: type gcloud auth application-default login
#Step 4: type gcloud auth application-default set-quota-project YOUR-PROJECT-ID
#Step 5: type export GOOGLE_CLOUD_PROJECT=YOUR-PROJECT-ID
#Step 6: python3 BigQuery.py

from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# Perform a query.
query = """
	SELECT name, SUM(number) as total_people
	FROM `bigquery-public-data.usa_names.usa_1910_2013`
	WHERE state = 'TX'
	GROUP BY name, state
	ORDER BY total_people ASC
	LIMIT 10
"""

# Make an API request.
query_job = client.query(query)  

print("The query data:")
for row in query_job:
	# Row values can be accessed by field name or index.
	print("name={}, count={}".format(row[0], row["total_people"]))	
