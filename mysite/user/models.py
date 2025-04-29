from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # to associate user with the particular model
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures') # This line is used to define a field in a Django model that stores an image file
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username







#  user = models.OneToOneField(User, on_delete=models.CASCADE)
# Purpose:
# This line is typically used to extend the default User model by associating additional fields or data 
# (e.g., profile picture, bio, etc.) with a Profile model.
# Example Use Case:
# If you want to store additional information about users (e.g., address, phone number), 
# you can add those fields to the Profile model and link it to the User model using this OneToOneField.





# image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')

# This line is used to define a field in a Django model that stores an image file
# [models.ImageField]: This is a field type provided by Django specifically for handling image files. It ensures that the uploaded file is an image and provides tools to work with it.
# [default='profilepic.jpg']: This sets a default value for the field. If no image is uploaded, the field will automatically use the file named profilepic.jpg. This file should exist in the appropriate media directory.
# [upload_to='profile_pictures']: This specifies the directory within the MEDIA_ROOT where uploaded images will be stored. For example, if a user uploads an image, it will be saved in the profile_pictures folder.

# Example Use Case
# This field might be used in a user profile model to store profile pictures. If a user doesn't upload a picture, the default image (profilepic.jpg) will be used instead.