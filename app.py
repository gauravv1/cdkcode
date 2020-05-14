#!/usr/bin/env python3

from aws_cdk import core

from cdkcode.cdkcode_stack import CdkcodeStack


app = core.App()
CdkcodeStack(app, "cdkcode", env={'region': 'us-west-2'})

app.synth()
