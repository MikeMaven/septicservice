from django.test import TestCase
from unittest.mock import patch, Mock
from rest_framework import status
from rest_framework.test import APIRequestFactory
from .views import SepticInfoView


class SepticInfoViewTests(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

    @patch('septicserviceapp.views.requests.get')
    def test_get_septic_info_has_septic(self, mock_requests_get):
        mock_response = Mock()
        mock_response.ok = True
        mock_response.json.return_value = {
            "property/details": {
                "result": {
                    "property": {
                        'sewer': 'septic'
                    }
                }
            }
        }
        mock_requests_get.return_value = mock_response

        address = '123 Main St'
        zip_code = '12345'
        url = f'/septicinfo/{address}/{zip_code}/'
        request = self.factory.get(url)
        response = SepticInfoView.as_view()(request, address, zip_code)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['has_septic'], True)

    @patch('septicserviceapp.views.requests.get')
    def test_get_septic_info_no_septic(self, mock_requests_get):
        mock_response = Mock()
        mock_response.ok = True
        mock_response.json.return_value = {
            "property/details": {
                "result": {
                    "property": {
                        'sewer': 'public'
                    }
                }
            }
        }
        mock_requests_get.return_value = mock_response

        address = '123 Main St'
        zip_code = '12345'
        url = f'/septicinfo/{address}/{zip_code}/'
        request = self.factory.get(url)
        response = SepticInfoView.as_view()(request, address, zip_code)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['has_septic'], False)

    @patch('septicserviceapp.views.requests.get')
    def test_get_septic_info_server_error(self, mock_requests_get):
        mock_response = Mock()
        mock_response.ok = False
        mock_requests_get.return_value = mock_response

        address = '123 Main St'
        zip_code = '12345'
        url = f'/septicinfo/{address}/{zip_code}/'
        request = self.factory.get(url)
        response = SepticInfoView.as_view()(request, address, zip_code)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
