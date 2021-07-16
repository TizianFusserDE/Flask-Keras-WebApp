from app import *

from azure.cognitiveservices.vision import computervision
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import azure


def test_get_employee_details_check_status_code_equals_200():
    analysis = ComputerVisionClient(cog_endpoint, CognitiveServicesCredentials(cog_key))
    try:
        analysis.list_models()
    except:
        assert 2 == 1