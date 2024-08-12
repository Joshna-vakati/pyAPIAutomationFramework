import allure
import pytest
import requests

from src.constants.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import APIConstants
from src.constants.helpers.payload_manager import payload_create_booking
from src.constants.helpers.common_verification import *
from utils.utils import Utils


class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that booking status and booking id shouldn't be null")
    @allure.description("create a booking from the payload and verify that booking id should not be null ")
    def test_create_booking_positive(self):
        response = post_request(
            url =  APIConstants().url_create_booking(),
            auth = None,
            headers = Utils().common_headers_json(),
            payload = payload_create_booking(),
            in_json = False
        )
        verify_http_status_code(response_data = response, expect_data = 200)
        verify_json_key_for_not_null(response.json()['bookingid'])

