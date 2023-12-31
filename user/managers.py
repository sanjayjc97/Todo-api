from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

class Custom_user_manager(BaseUserManager):
    '''
    this is a custom user manager where the identifier for the authentication is the email insted of username
    '''

    def create_user(self,email,password,**extra_fields):
        ''' 
        creating a user with given email and password
        '''

        if not email:
            raise ValueError("The Email must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self,email,password,**extra_fields):
        '''
        Create a superuser with the given email and password
        '''
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff = True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email,password,**extra_fields)
        
