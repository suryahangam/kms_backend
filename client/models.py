from django.db import models
from user.models import TimestampedModel
from kms.utils import generate_unique_ID


class Client(TimestampedModel):
    TECHNOLOGY = 'Technology'
    FINANCE = 'Finance'
    HEALTHCARE = 'Healthcare'
    RETAIL = 'Retail'

    # Define choices as tuples of (value, display_name)
    SECTOR_CHOICES = [
        (TECHNOLOGY, 'Technology'),
        (FINANCE, 'Finance'),
        (HEALTHCARE, 'Healthcare'),
        (RETAIL, 'Retail'),
        # Add other sectors as needed
    ]

    TERM_CHOICES = [
        ('6', '6 Months'),
        ('9', '9 Months'),
        ('12', '12 Months'),
        ('24', '24 Months'),
        ('36', '36 Months'),
        ('0', 'Unlimited'),
    ]

    name = models.CharField(max_length=255)
    sector = models.CharField(max_length=200, choices=SECTOR_CHOICES)
    unique_client_id = models.CharField(max_length=50, 
                                        default=generate_unique_ID, unique=True)
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=20)
    post_code = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    company_size = models.IntegerField(null=True, blank=True)
    key_personnel = models.CharField(max_length=100, null=True, blank=True)
    company_history = models.TextField(null=True, blank=True)
    contactTerm = models.CharField(max_length=20, choices=TERM_CHOICES, default=0)
    company_logo = models.ImageField(upload_to='company_logo')

    def __str__(self):
        return self.name
    
    def add_user(self, user):
        user.client.id = self.id
        user.save()
        return user
    
    def remove_user(self, user):
        pass
