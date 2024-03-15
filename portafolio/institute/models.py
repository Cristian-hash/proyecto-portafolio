from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    names = models.CharField(max_length=30, null=True)
    first_last_name = models.CharField(max_length=30, null=True)
    second_last_name = models.CharField(max_length=30, null=True)
    age = models.PositiveIntegerField(null=True)
    dni = models.CharField(max_length=8, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.png', blank=True)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    registration_date = models.DateField(auto_now_add = True)
    modification_date = models.DateField(auto_now = True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    @property
    def is_staff(self):
        return self.is_superuser

    class Meta:
        db_table='auth_user'
        verbose_name='usuario'
        verbose_name_plural='usuarios'   

class Course(models.Model):
    name = models.CharField(max_length=30)
    teoric_hours = models.PositiveIntegerField()
    practice_hours = models.PositiveIntegerField()
    credits = models.PositiveIntegerField()
    image = models.ImageField(upload_to='courses_images/', blank=True)
    is_popular = models.BooleanField(default=False)
    
    class Meta:
            db_table='institute_course'
            verbose_name='curso'
            verbose_name_plural='cursos' 
    

class Inscription(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    courses= models.ManyToManyField(Course)
    year=models.DateField()
    cycle=models.PositiveIntegerField()

    def __str__(self):
        return str(self.user) + '(' + str(self.year.year) + '-' + str(self.cycle) + ')'
    
    class Meta:
            verbose_name='inscripción'
            verbose_name_plural='inscripciones'
    

class Grade(models.Model):
    calification=models.PositiveIntegerField()
    published = models.DateTimeField(auto_now_add = True)
    inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE)
    
    class Meta:
            verbose_name='calificación'
            verbose_name_plural='calificaciones'
    