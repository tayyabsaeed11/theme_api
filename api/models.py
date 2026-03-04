from django.db import models


class Category(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Theme(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    category = models.ForeignKey(Category, related_name='themes', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    thumbnail = models.URLField(blank=True, null=True)
    textColor = models.CharField(max_length=20)
    actionIconColor = models.CharField(max_length=20)
    actionBg = models.URLField(blank=True, null=True)

    keyboardBg = models.URLField(blank=True, null=True)
    keyboardBgColor = models.CharField(max_length=20)
    keysBg = models.URLField(blank=True, null=True)

    isPremium = models.BooleanField(default=False)
    downloads = models.IntegerField(default=0)
    sortOrder = models.IntegerField(default=0)
    createdAt = models.BigIntegerField()

    def __str__(self):
        return self.name


class Story(models.Model):
    imageUrl = models.URLField()
    category = models.ForeignKey(Category, related_name='stories', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.name} Story"