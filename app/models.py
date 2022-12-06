from django.db import models
from django.utils.html import format_html
# Create your models here.
class SocialLinks(models.Model):
    telegram = models.URLField(help_text="Enter telegram url",verbose_name="Telegram",default="https://me.behzodasliddinov.uz")
    instagram = models.URLField(help_text="Enter instagram url",verbose_name="Instagram",default="https://me.behzodasliddinov.uz")
    tiktok = models.URLField(help_text="Enter tiktok url",verbose_name="Tiktok",default="https://me.behzodasliddinov.uz")
    facebook = models.URLField(help_text="Enter facebook url",verbose_name="Facebook",default="https://me.behzodasliddinov.uz")
    youtube = models.URLField(help_text="Enter youtube url",verbose_name="Youtube",default="https://me.behzodasliddinov.uz")
    def __str__(self):
        return "Social Links"
    class Meta:
        verbose_name = "Social Link "
        verbose_name_plural = "Social Links "
class Profile(models.Model):
    name = models.CharField(max_length=150,help_text="Enter name",verbose_name="Name")
    image = models.ImageField(upload_to="profile-images",help_text="Upload image",verbose_name="Image")
    age = models.IntegerField(help_text="Enter age",verbose_name="Age")
    technologies = models.TextField(help_text="Enter technologies",verbose_name="Technologies")
    job = models.CharField(max_length=100,help_text="Enter job",verbose_name="Job")
    languages = models.TextField(default="O'zbek",help_text="Enter language",verbose_name="Languages")
    resume = models.FileField(upload_to="resumes",help_text="Upload resume",verbose_name="Resume")
    portfolio = models.IntegerField(default="1",help_text="Enter potfolios count",verbose_name="Portfolio Count")
    profession = models.DecimalField(max_digits=10,decimal_places=2,default="1.5",help_text="Enter profession year",verbose_name="Profession Year")
    projects = models.IntegerField(default="1",help_text="Enter projects count",verbose_name="Projects Count")
    def __str__(self):
        return self.name
    @property
    def photo(self):
        return format_html('<img src={} width="50"  height="50" style="border-radius:50%"'.format(self.image.url))
class Visitors(models.Model):
    count = models.IntegerField(default=1)
class Portfolio(models.Model):
    title=models.CharField(max_length=150,help_text="Enter project name",verbose_name="Project name")
    url =models.URLField(help_text="Enter project url",verbose_name="Project URL",default="https://me.behzodasliddinov.uz")
    image = models.ImageField(upload_to="profile-images",help_text="Upload image",verbose_name="Image")
    def __str__(self):
        return self.title
    @property
    def photo(self):
        return format_html('<img src={} width="50"  height="50" style="border-radius:50%"'.format(self.image.url))
class Info(models.Model):
    gmail = models.EmailField(help_text="Enter email",verbose_name="Email")
    phone=models.CharField(max_length=150,help_text="Enter phone number",verbose_name="Phone Number")
    adress =models.CharField(max_length=150,help_text="Enter address",verbose_name="Address")
    def __str__(self):
        return 'Info'
class Xabarlar(models.Model):
    name = models.CharField(max_length=400)
    message = models.TextField()
    email = models.EmailField()
    def __str__(self):
        return self.name