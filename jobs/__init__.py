from nautobot.apps.jobs import Job


class HelloWorldJob(Job):
    class Meta:
        name = "Hello World"
        description = "Minimal test-job for Nautobot/Celery"

    def run(self, *args, **kwargs):
        self.logger.info("Hello from nbjobs")
        self.logger.info("Celery worker is alive")
        return "Done"
