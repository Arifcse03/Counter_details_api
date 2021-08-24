from rest_framework.response import Response
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import CounterDetails
from .serializers import CounterDetailsSerializers
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

from counter_details_api_app import serializers

# Create your views here.
class CounterDetailsApi(APIView):
    def get(self, request):
        try:
            result = CounterDetails.objects.all()

            serializer = CounterDetailsSerializers(result, many=True)
            return Response(serializer.data)
        except Exception as exc:
            print(f"Exception ()->{exc}")
            return Response({"is_success": False, "error": exc})

    def post(self, request):
        counter_details_data = JSONParser().parse(request)
        counter_details_serializer = CounterDetailsSerializers(
            data=counter_details_data
        )
        if counter_details_serializer.is_valid():
            counter_details_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add!!", safe=False)

    def put(self, request):
        counter_details_data = JSONParser().parse(request)
        counter_details = CounterDetails.objects.get(
            kpi_name=counter_details_data["kpi_name"]
        )
        serializer = CounterDetailsSerializers(
            counter_details, data=counter_details_data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse("Failed to Update", safe=False)

    def delete(self, request, pk, format=None):
        counter_details = CounterDetails.objects.filter(kpi_name=pk)
        serializer = CounterDetailsSerializers(counter_details, many=True)
        if serializer:
            if counter_details.delete():
                return JsonResponse("Deleted Succuessfull!!", safe=False)
        return JsonResponse("Failed to delete!!", safe=False)
