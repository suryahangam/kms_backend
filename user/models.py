from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# from client.models import Client
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # This makes sure this model is not created in the database, 
        # it's used for inheritance.
        abstract = True 

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class OfficeBranch(TimestampedModel):
    branch_name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    post_code = models.CharField(max_length=40)
    country = models.CharField(max_length=30)
    branch_email = models.EmailField()
    branch_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.branch_name
    
    def add_employee(self, user):
        pass

    def get_employee_list(self):
        pass

    def remove_employee(self):
        pass


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    client = models.ForeignKey('client.Client', 
                               on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(OfficeBranch, 
                               on_delete=models.SET_NULL, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.email
    
    # def save(self):
    #     # Unique user ID required?
    #     pass

    def get_role(self):
        pass

    def set_role(self, role):
        pass

    def get_company(self):
        pass

    def set_company(self, company):
        pass

    def redeem_item(self):
        pass
    

class Profile(TimestampedModel):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    dob = models.DateField(null=True, blank=True)
    cover_image = models.FileField(upload_to='cover_images')
    about = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=1, 
                              choices=GENDER_CHOICES, null=True)
    address1 = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    profession = models.CharField(max_length=200, null=True) # choice field
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.email)
    
    def get_projects(self):
        pass

    def get_reward_point_list(self):
        pass
    
    def get_biography(self):
        pass
    

class UserLog(TimestampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.user.email} -> {self.title}'

    def get_user_log(self, user):
        return UserLog.objects.filter(user=user)
    

class Announcement(TimestampedModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, 
                                null=True)
    announcement_date = models.DateTimeField()
    is_archive = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    def archive_announcement(self):
        self.is_archive = True
        return True
    
    def get_latest(self, count=5):
        return Announcement.objects.all().order_by('-announcement_date')[:count]
    
    def publish(self, announcement=None):
        if announcement:
            announcement.published = True
            announcement.save()
            return announcement.id
        self.published = True
        return self.id


class AnnouncementDocument(TimestampedModel):
    document_title = models.CharField(max_length=200, 
                                      null=True, blank=True)
    file = models.FileField(upload_to='announcements')
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.announcement.title} => {self.document_title}'


