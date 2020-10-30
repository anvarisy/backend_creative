from django.db import models
from django.contrib.auth.models  import BaseUserManager, AbstractBaseUser,\
    PermissionsMixin
from django.utils import timezone
from django.utils.crypto import get_random_string

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,full_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, full_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            full_name=full_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class user(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=100, primary_key=True)
    # c_user = models.CharField(max_length=20, unique=True,default=get_random_string(16))
    full_name = models.CharField(max_length=35,blank=True)
    is_client = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_login = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    date_joined = models.DateTimeField(default=timezone.now)
    
    # EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    
    def __str__(self):
        return self.email
    # class Meta:
    #     verbose_name = _('user')
    #     verbose_name_plural = _('users')
    #     db_table = 'users'
        
    # def clean(self):
    #     super().clean()
    #     self.email = self.__class__.objects.normalize_email(self.email)


    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     send_mail(subject, message, from_email, [self.email], **kwargs)
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
   

class category(models.Model):
    category_name = models.CharField(max_length=40)
    category_icon = models.ImageField(upload_to='category')
    def __str__(self):
        return self.category_name
    
class style(models.Model):
    category = models.ForeignKey(category, related_name='categories', on_delete=models.CASCADE)
    style_name = models.CharField(max_length=40)
    style_icon = models.ImageField(upload_to='style',blank=True)
    style_price = models.IntegerField()

class types(models.Model):
    style = models.ForeignKey(style, related_name='styles', on_delete=models.CASCADE)
    type_name = models.CharField(max_length=60)
    type_icon = models.ImageField(upload_to='types')
    type_extra = models.IntegerField(default=0)
    
class order(models.Model):
    order_id = models.CharField(max_length=12, primary_key=True, default=get_random_string(10))
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    style = models.ForeignKey(style, on_delete=models.CASCADE)
    types = models.ForeignKey(types,on_delete=models.CASCADE)
    order_image = models.ImageField(upload_to='order',null=True, blank=True)
    date_request = models.DateField(default=timezone.now)
    is_remove_acc = models.BooleanField(default=False)
    is_include_file = models.BooleanField(default=False)
    is_fast = models.BooleanField(default=False)
    is_payed = models.BooleanField(default=False)
    is_finish = models.BooleanField(default=False)
    total = models.IntegerField(default=0)
    num_character = models.IntegerField(default=1)
    note = models.TextField()
    order_result = models.FileField(upload_to='result', default='#')

class carousel(models.Model):
    carousel_image = models.ImageField(upload_to='carousel')
    carousel_text = models.CharField(max_length=160, blank = True, null = True)
    carousel_link = models.CharField(max_length=160, blank=True, null = True)
    carousel_position = models.IntegerField()
    
class gallery(models.Model):
    image_gallery = models.ImageField(upload_to='gallery')
    type_gallery=models.CharField(max_length=130)
    
