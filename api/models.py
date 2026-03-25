from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class StickerCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sticker(models.Model):
    category = models.ForeignKey(StickerCategory, related_name='stickers', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='stickers/')

    def __str__(self):
        return self.category.name



class Theme(models.Model):
    category = models.ForeignKey(Category, related_name='themes', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='themes/thumbnails/', blank=True, null=True)
    textColor = models.CharField(max_length=20, blank=True, null=True)
    actionIconColor = models.CharField(max_length=20, blank=True, null=True)
    actionBg = models.ImageField(upload_to='themes/action_bg/', blank=True, null=True)
    keyboardBg = models.ImageField(upload_to='themes/keyboard_bg/', blank=True, null=True)
    keyboardBgColor = models.CharField(max_length=20, blank=True, null=True)
    keysBg = models.ImageField(upload_to='themes/keys_bg/', blank=True, null=True)
    foreground = models.ImageField(upload_to='themes/foreground/', blank=True, null=True)
    isPremium = models.BooleanField(default=False)
    downloads = models.IntegerField(default=0)
    sortOrder = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sortOrder']


class Story(models.Model):
    imageUrl = models.ImageField(upload_to='stories/')
    category = models.ForeignKey(Category, related_name='stories', on_delete=models.CASCADE)
    stickers = models.ManyToManyField(Sticker, blank=True)

    def __str__(self):
        return f"{self.category.name} Story"
