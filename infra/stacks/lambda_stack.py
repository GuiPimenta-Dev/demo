from functions.another_private_hello_world.config import AnotherPrivateHelloWorldConfig
from authorizers.jwt.config import JwtAuthorizerConfig
from functions.another_private_hello_world.config import AnotherPrivateHelloWorldConfig
from functions.private_hello_world.config import PrivateHelloWorldConfig
from authorizers.docs.config import DocsAuthorizerConfig
from aws_cdk import Stack
from constructs import Construct
from infra.services import Services
from lambda_forge import release

@release
class LambdaStack(Stack):
    def __init__(self, scope: Construct, context, **kwargs) -> None:

        super().__init__(scope, f"{context.name}-CDK", **kwargs)

        self.services = Services(self, context)

        # Authorizers
        JwtAuthorizerConfig(self.services)
        DocsAuthorizerConfig(self.services)

        # PrivateHelloWorld
        PrivateHelloWorldConfig(self.services)

        # AnotherPrivateHelloWorld
        AnotherPrivateHelloWorldConfig(self.services)
        AnotherPrivateHelloWorldConfig(self.services)
