from nautobot.apps.jobs import Job


class HelloWorldJob(Job):
    class Meta:
        name = "Hello World"
        description = "Minimal test-job"

    def run(self, *args, **kwargs):
        self.logger.info("This code is no longer buggy.")
        return "Done"
