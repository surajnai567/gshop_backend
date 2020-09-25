from rest_framework.views import APIView
from django.http.response import JsonResponse
from offer.models import Offer
from.serializer import OfferSerializer


class OfferApiView(APIView):
    def get(self, request):
        offers = Offer.objects.all()
        print(offers)
        serialised = OfferSerializer(offers, many=True).data
        print(serialised)
        return JsonResponse({"code": 200, "status": "success", "offers": serialised})

