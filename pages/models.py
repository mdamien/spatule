from django.db import models
from tinymce.models import HTMLField

class Page(models.Model):
	title = models.CharField(max_length=400)
	content = HTMLField()
	url = models.CharField(max_length=400)
	image = models.ImageField(upload_to="pages",blank=True)

	def __unicode__(self):
		return self.title

class HomePage(models.Model):
	title = models.CharField(max_length=400)
	content = HTMLField()
	text1 = HTMLField()
	text2 = HTMLField()
	text3 = HTMLField()

	def __unicode__(self):
		return self.title

class SliderImage(models.Model):
	HOME = 'HOME'
	PAGE = 'PAGE'
	CATEGORY_CHOICES = (
		(HOME, 'Home'),
		(PAGE, 'Others page')
	)
	category = models.CharField(max_length="30",choices=CATEGORY_CHOICES,default=HOME)
	image = models.ImageField(upload_to="sliders")

	def __unicode__(self):
		return self.get_category_display() + ": " + str(self.pk)

class Article(models.Model):
	title = models.CharField(max_length=400)
	content = HTMLField()
	image = models.ImageField(upload_to="articles",blank=True)
	position = models.IntegerField()
	page = models.ForeignKey('Page')
	class Meta:
		ordering = ['page', 'position']

	def __unicode__(self):
		return self.page.title + ": " + self.title + " ("+str(self.position)+")"