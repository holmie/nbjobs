from nautobot.apps.jobs import Job


class HelloWorldJob(Job):
    class Meta:
        name = "Hello World"
        description = "Minimal test-job"

    def run(self, *args, **kwargs):
        self.logger.info("Wow, this code contains a nasty bug.")
        return "Done"
