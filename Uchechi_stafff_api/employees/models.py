from django.db import models

class Address(models.Model):
    """
    Address model to store address information
    """
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default='Nigeria')
    is_primary = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state}"


class StaffBase(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_role(self):
        """
        Base method to be overridden by subclasses
        Returns role-specific label
        """
        return "Staff Member"


class Manager(StaffBase):
    
    

    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"

    def __str__(self):
        return f"{self.full_name} - {self.department} Manager"

    def get_role(self):
        """
        Override get_role method for Manager
        """
        return f"Manager - {self.department}"


class Intern(StaffBase):

    mentor = models.ForeignKey(
        Manager, 
        on_delete=models.CASCADE, 
        related_name='interns'
    )
    internship_end = models.DateField()
    
    class Meta:
        verbose_name = "Intern"
        verbose_name_plural = "Interns"

    def __str__(self):
        return f"{self.full_name} - Intern (Mentor: {self.mentor.full_name})"

    def get_role(self):
        """
        Override get_role method for Intern
        """
        return f"Intern - Mentored by {self.mentor.full_name}"
