# APIConstants - Class which contain all the endpoints
# keep the URLs

class APIConstants(object):
    def base_url(self):
        return "https://restful-booker.herokuappp.com"
    def url_create_booking(self):
        return "https://restful-booker.herokuappp.com/booking"
    def url_create_token(self):
        return "https://restful-booker.herokuappp.com/auth"
    def url_patch_put_delete(self):
        return "https://restful-booker.herokuappp.com/booking/" + str(booking_id)
