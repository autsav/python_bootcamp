from django.db import models
from django.core.exceptions import ValidationError

def validate_age(age):
    if age<20:
        raise ValidationError("Your age should be more or equals to 20")

# Create your models here.
class UserBio(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(validators=[validate_age])
    bio = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


    def clean(self):
        if self.age > 40:
            if not self.bio:
                raise ValidationError("Bio is required when age is greater than 40")

    def full_clean(self, exclude=None, validate_unique=True):
        pass
