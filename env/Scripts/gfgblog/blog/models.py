# importing django models and users
from django.db import models
from django.contrib.auth.models import User

STATUS = (
	(0,"Draft"),
	(1,"Publish"),
	(2, "Delete")
)

# creating an django model class
class posts(models.Model):
	# title field using charfield constraint with unique constraint
	title = models.CharField(max_length=200, unique=True)
	# slug field auto populated using title with unique constraint
	slug = models.SlugField(max_length=200, unique=True)
	# author field populated using users database
	author = models.ForeignKey(User, on_delete= models.CASCADE)
	# and date time fields automatically populated using system time
	updated_on = models.DateTimeField(auto_now= True)
	created_on = models.DateTimeField()
	# content field to store our post
	content = models.TextField()
	# meta description for SEO benefits
	metades = models.CharField(max_length=300, default="new post")
	# status of post
	status = models.IntegerField(choices=STATUS, default=0)
	
	image_field = models.ImageField(upload_to='uploads/images/')

	# meta for the class
	class Meta:
		ordering = ['-created_on']
	# used while managing models from terminal
	def __str__(self):
		return self.title
from django.db import models

class AllDataTypesModel(models.Model):
    # CharField for short text
    short_text = models.CharField(max_length=100)

    # TextField for long text
    long_text = models.TextField()

    # IntegerField for integers
    integer_number = models.IntegerField()

    # FloatField for floating-point numbers
    float_number = models.FloatField()

    # DecimalField for precise decimal values
    decimal_number = models.DecimalField(max_digits=10, decimal_places=2)

    # BooleanField for true/false values
    boolean_field = models.BooleanField()

    # DateField for dates
    date_field = models.DateField()

    # TimeField for times
    time_field = models.TimeField()

    # DateTimeField for date and time
    datetime_field = models.DateTimeField()

    # FileField for file uploads
    file_field = models.FileField(upload_to='uploads/')

    # ImageField for image uploads
    image_field = models.ImageField(upload_to='uploads/images/')

    # EmailField for email addresses
    email_field = models.EmailField()

    # URLField for URLs
    url_field = models.URLField()

    # JSONField for JSON data (Django 3.1 and later)
    json_field = models.JSONField()

    # UUIDField for universally unique identifiers
    uuid_field = models.UUIDField()

    # ManyToManyField for many-to-many relationships
    related_models = models.ManyToManyField('self', blank=True)

    # Other fields or methods...
	

from django.db import models

class About(models.Model):
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"About (Last updated: {self.last_updated})"