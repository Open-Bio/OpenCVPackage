import os
from uflow.Core.PackageBase import PackageBase


class OpenCVPackage(PackageBase):
    """OpenCv uflow package"""

    def __init__(self):
        super(OpenCVPackage, self).__init__()
        self.analyzePackage(os.path.dirname(__file__))
