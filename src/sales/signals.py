from .models import Sale, Position
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


#### To calulate total rpice for a sale
@receiver(m2m_changed,sender=Sale.positions.through)
def calculate_total_sales_price(sender,instance,action,*args,**kwargs):
    print('action',action)
    total_price = 0

    ##checking type of action
    if action =="post_add" or action =="post_remove":
        for item in instance.get_positions():
            total_price+=item.price

    instance.total_price = total_price
    instance.save()

    ##Register this signal in app.py and then change deafault config method to app.py and class config