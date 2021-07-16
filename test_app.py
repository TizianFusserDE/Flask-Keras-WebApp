from app import *

from azure.cognitiveservices.vision import computervision
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import azure


def test_Azure_key_endpoint():
    analysis = ComputerVisionClient(cog_endpoint, CognitiveServicesCredentials(cog_key))
    try:
        analysis.list_models()
    except:
        assert False, "Wrong key and endpoint from Azure Cognitive Service!"

test_Azure_key_endpoint()

