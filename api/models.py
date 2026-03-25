from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    isPremium = models.BooleanField(default=False)
    downloads = models.IntegerField(default=0)
    sortOrder = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Story(models.Model):
    imageUrl = models.ImageField(upload_to='stories/')  # changed here too (optional but recommended)
    category = models.ForeignKey(Category, related_name='stories', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.name} Story"
