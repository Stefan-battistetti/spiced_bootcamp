<h1>Week 6 - The Data Pipeline</h1>

**Project Goal: Build a Dockerized Data Pipeline that analyzes the sentiment of tweets**

<h2>Description</h2>

- A docker container was built that runs a data pipeline to collect tweets published with the tag "COVID-19" and store them in a postgres database.

<h2>Future Plans</h2>>
- **Current status of the project:** Data pipeline runs up to point where tweets are stored in a database. No sentiment analysis is yet performed within the ETL file. 

- Future updates to the project will involve connecting the ETL sentiment analysis to the Docker container. An extra bonus would be connecting the results of sentiment analysis to a Slack Bot that periodically publishes the results.
