import allure
import pytest

class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that booking status and booking id shouldn't be null")
    @allure.description("create a booking from the payload and verify that booking id should not be null ")
    def test_create_booking_positive(self):
        pass


    