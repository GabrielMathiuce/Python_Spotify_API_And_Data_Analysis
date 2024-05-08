from django.middleware.csrf import CsrfViewMiddleware
import pdb


class CRSFHandler(CsrfViewMiddleware):

    def process_request(self, request):
        pdb.set_trace()
        print("Here")
