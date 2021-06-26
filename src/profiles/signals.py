### Model to work on
from .models import Profile
### Sender model
from django.contrib.auth.models import User

## Action
from django.db.models.signals import post_save

## Receiver
from django.dispatch import receiver


## Funtion to auto create a profile once a user is created.
@receiver(post_save,sender=User)
def post_save_create_profile(sender,instance,created,**kwargs):
    print(sender)
    print(instance)
    print(created)
    
    if created:
        Profile.objects.create(user=instance)

### Go to apps.py file to register this signal