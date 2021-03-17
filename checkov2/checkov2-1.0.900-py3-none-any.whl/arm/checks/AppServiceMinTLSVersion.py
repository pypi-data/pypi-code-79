from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.arm.base_resource_check import BaseResourceCheck

# https://docs.microsoft.com/en-us/azure/templates/microsoft.web/2019-08-01/sites

class AppServiceMinTLSVersion(BaseResourceCheck):
    def __init__(self):
        name = "Ensure web app is using the latest version of TLS encryption"
        id = "CKV_AZURE_15"
        supported_resources = ['Microsoft.Web/sites']
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if "properties" in conf:
            if "siteConfig" in conf["properties"]:
                if "minTlsVersion" in conf["properties"]["siteConfig"]:
                    if conf["properties"]["siteConfig"]["minTlsVersion"] == '1.2':
                        return CheckResult.PASSED
        return CheckResult.FAILED

check = AppServiceMinTLSVersion()