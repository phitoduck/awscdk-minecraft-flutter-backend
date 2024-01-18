# -*- coding: utf-8 -*-
import os

from aws_cdk import App, Environment
from cdk_minecraft import MinecraftPaasStack

# for development, use account/region from cdk cli
DEV_ENV = Environment(account=os.environ["AWS_ACCOUNT_ID"], region=os.getenv("AWS_REGION"))

APP = App()

MinecraftPaasStack(
    APP,
    "awscdk-minecraft-pickupgames-mc",
    login_page_domain_name_prefix="pickupgames-mc-user-pool",
    ec2_instance_type="t3.medium",
    disable_frontend=True,
    disable_auth=True,
    env=DEV_ENV,
)

APP.synth()
