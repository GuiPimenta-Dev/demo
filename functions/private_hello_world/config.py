from infra.services import Services

class PrivateHelloWorldConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="PrivateHelloWorld",
            path="./functions/private_hello_world",
            description="hello world",
            
        )

        services.api_gateway.create_endpoint("GET", "/private_hello_world", function)

            