# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .certificate import *
from .policy import *
from .provider import *
from .ssh_certificate import *
from .ssh_config import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_venafi.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_venafi.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "venafi",
  "mod": "index/certificate",
  "fqn": "pulumi_venafi",
  "classes": {
   "venafi:index/certificate:Certificate": "Certificate"
  }
 },
 {
  "pkg": "venafi",
  "mod": "index/policy",
  "fqn": "pulumi_venafi",
  "classes": {
   "venafi:index/policy:Policy": "Policy"
  }
 },
 {
  "pkg": "venafi",
  "mod": "index/sshCertificate",
  "fqn": "pulumi_venafi",
  "classes": {
   "venafi:index/sshCertificate:SshCertificate": "SshCertificate"
  }
 },
 {
  "pkg": "venafi",
  "mod": "index/sshConfig",
  "fqn": "pulumi_venafi",
  "classes": {
   "venafi:index/sshConfig:SshConfig": "SshConfig"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "venafi",
  "token": "pulumi:providers:venafi",
  "fqn": "pulumi_venafi",
  "class": "Provider"
 }
]
"""
)
