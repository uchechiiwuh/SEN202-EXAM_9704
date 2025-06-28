from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Manager, Intern
from .serializers import (
    ManagerSerializer, 
    ManagerDetailSerializer,
    InternSerializer
)

# Create your views here.

class ManagerViewSet(viewsets.ModelViewSet):
   
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ManagerDetailSerializer
        return ManagerSerializer

    @action(detail=True, methods=['get'])
    def interns(self, request, pk=None):
       
        manager = self.get_object()
        interns = manager.interns.all()
        serializer = InternSerializer(interns, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_department(self, request):
       
        department = request.query_params.get('department', '')
        if department:
            managers = Manager.objects.filter(department__icontains=department)
        else:
            managers = Manager.objects.all()
        
        serializer = self.get_serializer(managers, many=True)
        return Response(serializer.data)


class InternViewSet(viewsets.ModelViewSet):
   
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

    @action(detail=False, methods=['get'])
    def by_mentor(self, request):
        
        mentor_id = request.query_params.get('mentor_id', '')
        if mentor_id:
            interns = Intern.objects.filter(mentor_id=mentor_id)
        else:
            interns = Intern.objects.all()
        
        serializer = self.get_serializer(interns, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def active(self, request):
       
        interns = Intern.objects.filter(is_active=True)
        serializer = self.get_serializer(interns, many=True)
        return Response(serializer.data)
