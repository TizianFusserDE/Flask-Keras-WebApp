from app import *
import pytest

from azure.cognitiveservices.vision import computervision
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import azure


def test_Azure_key_endpoint():
    analysis = ComputerVisionClient(cog_endpoint, CognitiveServicesCredentials(cog_key))
    try:
        analysis.list_models()
    except:
       return "Not Match"


def test_model():
    if test_Azure_key_endpoint() == "Not Match":
        result = "Inactive"
    elif test_Azure_key_endpoint() == None:
        result = "Active"
    else:
        result = "Unknown"
    assert result == "Active", "Inactive Azure Cognitive Service Key or Endpoint."

