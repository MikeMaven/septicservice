import os
import urllib

from django.apps import apps
from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse, HttpResponseServerError


def getSepticInfoByAddress(request, address, zip_code):
    # Replace spaces in address with +
    address = address.replace(' ', '+')

    # Make request to HouseCanary API to retrieve property details
    api_key = os.environ.get('HOUSECANARY_API_KEY')
    # Get URL from app configuration
    config = apps.get_app_config('septicserviceapp')
    url = config.house_canary_property_details_api
    params = {'address': address, 'zipcode': zip_code}
    query_string = urllib.parse.urlencode(params)
    full_url = f"{url}?{query_string}"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(full_url, headers=headers)

    # Parse response and check for septic system
    if response.ok:
        data = response.json()
        sewer = data['property/details/summary']['sewer']
        has_septic = sewer.lower() == 'septic'
    else:
        return HttpResponseServerError()

    # Return boolean indicating whether property has septic system
    septic_info = {'has_septic': has_septic}
    return JsonResponse(septic_info)
