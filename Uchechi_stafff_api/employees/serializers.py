from rest_framework import serializers
from .models import Manager, Intern, Address


class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer for Address model
    """
    
    class Meta:
        model = Address
        fields = [
            'id', 'street_address', 'city', 'state', 'postal_code', 
            'country', 'is_primary', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ManagerSerializer(serializers.ModelSerializer):
    
    full_name = serializers.ReadOnlyField()
    intern_count = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Manager
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number',
            'hire_date', 'salary', 'is_active', 'department', 
            'has_company_card', 'full_name', 'intern_count', 'role',
            'address', 'created_at', 'updated_at'
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
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Intern
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number',
            'hire_date', 'salary', 'is_active', 'mentor', 'mentor_name',
            'internship_end', 'full_name', 'role', 'address',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_role(self, obj):
        return obj.get_role()


class ManagerDetailSerializer(ManagerSerializer):
    
    interns = InternSerializer(many=True, read_only=True)

    class Meta(ManagerSerializer.Meta):
        fields = ManagerSerializer.Meta.fields + ['interns']


class ManagerCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Separate serializer for create/update operations that excludes sensitive fields
    """
    
    class Meta:
        model = Manager
        fields = [
            'first_name', 'last_name', 'email', 'phone_number',
            'hire_date', 'salary', 'is_active', 'department', 'address'
        ]


class InternCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Separate serializer for create/update operations
    """
    
    class Meta:
        model = Intern
        fields = [
            'first_name', 'last_name', 'email', 'phone_number',
            'hire_date', 'salary', 'is_active', 'mentor', 'internship_end', 'address'
        ] 