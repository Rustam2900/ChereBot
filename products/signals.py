import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Product, ProductImage


@receiver(post_delete, sender=ProductImage)
def delete_image_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(pre_save, sender=ProductImage)
def delete_old_image_file_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_image = ProductImage.objects.get(pk=instance.pk).image
    except ProductImage.DoesNotExist:
        return False

    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)


@receiver(post_delete, sender=Product)
def delete_related_images_on_product_delete(sender, instance, **kwargs):
    for product_image in instance.images.all():
        if product_image.image:
            if os.path.isfile(product_image.image.path):
                os.remove(product_image.image.path)
