from infra.services import Services

class AnotherPrivateHelloWorldConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="AnotherPrivateHelloWorld",
            path="./functions/another_private_hello_world",
            description="hello world",
            
        )

        services.api_gateway.create_endpoint("GET", "/another_private_hello_world", function)

            