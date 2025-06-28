from rest_framework import serializers
from .models import Manager, Intern


class ManagerSerializer(serializers.ModelSerializer):
    
    full_name = serializers.ReadOnlyField()
    intern_count = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    class Meta:
        model = Manager
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number',
            'hire_date', 'salary', 'is_active', 'department', 
            'has_company_card', 'full_name', 'intern_count', 'role',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'has_company_card']

    def get_intern_count(self, obj):
        return obj.interns.count()

    def get_role(self, obj):
        return obj.get_role()


class InternSerializer(serializers.ModelSerializer):
    
    full_name = serializers.ReadOnlyField()
    mentor_name = serializers.ReadOnlyField(source='mentor.full_name')
    role = serializers.SerializerMethodField()

    class Meta:
        model = Intern
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number',
            'hire_date', 'salary', 'is_active', 'mentor', 'mentor_name',
            'internship_end', 'full_name', 'role', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_role(self, obj):
        return obj.get_role()


class ManagerDetailSerializer(ManagerSerializer):
    
    interns = InternSerializer(many=True, read_only=True)

    class Meta(ManagerSerializer.Meta):
        fields = ManagerSerializer.Meta.fields + ['interns']


class ManagerCreateUpdateSerializer(serializers.ModelSerializer):
   
    
    class Meta:
        model = Manager
        fields = [
            'first_name', 'last_name', 'email', 'phone_number',
            'hire_date', 'salary', 'is_active', 'department'
        ]


class InternCreateUpdateSerializer(serializers.ModelSerializer):
  
    
    class Meta:
        model = Intern
        fields = [
            'first_name', 'last_name', 'email', 'phone_number',
            'hire_date', 'salary', 'is_active', 'mentor', 'internship_end'
        ] 