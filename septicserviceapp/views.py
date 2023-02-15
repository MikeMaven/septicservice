import os
import urllib

from django.apps import apps
from django.shortcuts import render

# Create your views here.
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status


class SepticInfoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, address, zip_code):
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
            # Return boolean indicating whether property has septic system
            septic_info = {'has_septic': has_septic}
            return Response(septic_info)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
