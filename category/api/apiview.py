from rest_framework.views import APIView
from django.http.response import JsonResponse
from category.models import CategoryModel
from .serializer import CategorySerializer
import json


class CategoryApiView(APIView):
	def post(self, request):
		token = json.loads(request.body.decode('utf-8'))
		category = CategoryModel.objects.all()
		serial_data = CategorySerializer(category, many=True).data
		return JsonResponse({"code": 200, "status": "success", "categories": serial_data})



