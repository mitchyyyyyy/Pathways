from django.db import models
from django.core.exceptions import ValidationError
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.urls import reverse
from django.core.cache import cache
from django.contrib.auth.models import User

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()
        
class Company(SingletonModel):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    phone = models.CharField(max_length=20)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    description = models.TextField(null=True, blank=True)
    mission = models.TextField(null=True, blank=True)
    vision = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def clean(self):
        if Company.objects.exists() and self.pk != Company.objects.first().pk:
            raise ValidationError("There can only be one Company instance")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='slider/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Service(models.Model):
    name = models.CharField(max_length=255, db_index=True,null=True)
    slug = models.SlugField(
        max_length=255, 
        null=True, 
        unique=True, 
        db_index=True
    )
    image = models.ImageField(
        upload_to='services/', 
        null=True, 
        blank=True
    )
    content = HTMLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']
        indexes = [
            # Covering index for common queries
            models.Index(
                fields=['-updated_at', '-created_at'],
                name='service_date_idx'
            ),
            # Index for name lookups
            models.Index(
                fields=['name'],
                name='service_name_idx'
            ),
            # Composite index including commonly accessed fields
            models.Index(
                fields=['id'],
                name='service_composite_idx',
                include=['name', 'slug', 'image']
            ),
        ]

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return ''

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        # Clear cache on save
        cache.delete('context_services')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'slug': self.slug}) 

class Team(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team/%Y/%m/%d/')
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=False, unique=True, db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    category = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='service', null=True, blank=True, db_index=True)
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    content = HTMLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug}) 

    class Meta:
        indexes = [
            models.Index(fields=['-created_at', '-updated_at'], name='blog_date_idx'),
            models.Index(fields=['author_id', 'category_id'], name='blog_relations_idx'),
        ]

class BlogVisit(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True) 

class Faq(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General Information'),
        ('contact', 'Contact'),
        ('loan', 'Loan'),
        ('membership', 'Membership'),
        ('payment', 'Payment'),
        ('privacy', 'Privacy'),
        ('terms', 'Terms'),
        ('other', 'Other'),
    ]

    question = models.CharField(max_length=255, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)     

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['category', '-updated_at', '-created_at']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"


# contact
class Inquiry(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    subject = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-updated_at','-created_at']

class Partner(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='partner', null=True, blank=True) 
    website = models.URLField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-updated_at','-created_at']