from nautobot.apps.jobs import register_jobs
from .hello import HelloWorldJob

register_jobs(HelloWorldJob)
