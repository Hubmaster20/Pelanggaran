from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Model_pengurus(models.Model):
	nama_pengurus	= models.CharField(max_length = 2500)
	staff	=models.CharField(max_length = 1200)
	no_telpon	=models.CharField(max_length = 25)
	username	=models.CharField(max_length = 1200)
	password	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_pengurus)

class Model_santri(models.Model):
	id_santri	= models.CharField(max_length = 2500)
	nama_santri	= models.CharField(max_length = 2500)
	tempat_tgl_lahir	=models.CharField(max_length = 1200)
	alamat	=models.CharField(max_length = 25)
	pendidikan	=models.CharField(max_length = 1200)
	nama_wali	=models.CharField(max_length = 1200)
	nomer_hp	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_santri)

class Model_pelanggaran1(models.Model):
	id_pelanggaran	= models.CharField(max_length = 2500)
	nama_santri	=models.CharField(max_length = 1200)
	kategori	=models.CharField(max_length = 2500)
	tgl_kejadian	=models.CharField(max_length = 1200)
	keterangan	=models.CharField(max_length = 1200)
	hukuman	=models.CharField(max_length = 1200)
	nama_pengurus	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.kategori)