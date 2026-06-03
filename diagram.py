from diagrams import Diagram, Cluster
from diagrams.programming.framework import FastAPI
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.queue import Kafka
from diagrams.generic.compute import Rack

with Diagram("SentinelIQ SOC Architecture", show=True):

    data = Rack("Data Sources")

    with Cluster("Ingestion Layer"):
        api = FastAPI("FastAPI / Events")
        queue = Kafka("Stream (Kafka/Redis)")

    with Cluster("Processing"):
        enrich = Rack("Enrichment Engine")

    with Cluster("Detection Engine"):
        ai = Rack("ML + Rules + Risk Engine")

    db = PostgreSQL("Database")

    data >> api >> queue >> enrich >> ai >> db