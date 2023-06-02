from metaflow import FlowSpec, batch, schedule, step


def say_hello():
    print("hello world")


@schedule(daily=True)
class HelloFlow(FlowSpec):
    @step
    def start(self):
        self.next(self.train)

    @batch(cpu=1, memory=100)
    @step
    # @environment
    def train(self):
        say_hello()
        self.hello = 1
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == '__main__':
    HelloFlow()
