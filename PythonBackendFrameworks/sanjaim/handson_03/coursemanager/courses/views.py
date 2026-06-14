from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import course_serializer

def hello_view(request):
    return HttpResponse("Course Management API is running")


class CourseListView(APIView):
    def get(self,request):
        cour = Course.objects.all()
        seri = course_serializer(cour,many=True)
        return Response(seri.data)

    def post(self,request):
        seri = course_serializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data,status=status.HTTP_201_CREATED)

        return Response(seri.errors,status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):
    def get(self,request,pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"error":"not found"},status=404)
        seri = course_serializer(course)
        return Response(seri.data)

    def put(self,request,pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"error":"not found"},status=404)

        seri = course_serializer(course,data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data,status=200)
        return Response(seri.errors,status=400)


    def delete(self,request,pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"status":"error not Found"},status=404)
        course.delete()
        return Response(status=204)