from django.db import models


class About(models.Model):
    profile_pic = models.ImageField()
    title = models.CharField(max_length=50, default='About Me')
    subtitle_normal = models.CharField(max_length=30, default="Hello!")
    subtitle_styled = models.CharField(max_length=30, default="I'M Sarthak Singh.")
    content = models.TextField()


class Social(models.Model):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=50)
    link = models.URLField()
    about_include = models.BooleanField()

    def __str__(self):
        return self.name


#-------------------------------------------------------------------------------------


class Skill_category(models.Model):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(Skill_category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    progress = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name + ' ( ' + self.category.name + ' )'


#-------------------------------------------------------------------------------------


class Training(models.Model):
    logo_image = models.ImageField()
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


#-------------------------------------------------------------------------------------


class Project(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    description = models.TextField()
    button_link = models.URLField(blank=True)
    button_text = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name + ' ( ' + self.platform + ' ) '


#-------------------------------------------------------------------------------------


class Port_Filter(models.Model):
    name = models.CharField(max_length=20)
    button_name = models.CharField(max_length=20)

    def __str__(self):
        return self.button_name


class Port_Column(models.Model):
    number = models.DecimalField(max_digits=1, decimal_places=0)

    def __str__(self):
        return 'Column ' + str(self.number)


class Port_Item(models.Model):
    filter = models.ForeignKey(Port_Filter, on_delete=models.SET_NULL, null=True)
    column = models.ForeignKey(Port_Column, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(blank=True)
    position = models.DecimalField(max_digits=9999, decimal_places=0, blank=True, null=True)
    caption = models.TextField(blank=True)
    vid_link = models.URLField(blank=True)
    vid_title = models.CharField(blank=True, max_length=40)

    def __str__(self):
        if self.caption:
            return str(self.position) + ' - ' + str(self.caption) + ' ( ' + str(self.column) + ' ) '
        else:
            return self.vid_title + ' ( ' + str(self.column) + ' ) '


#-------------------------------------------------------------------------------------


class Contact(models.Model):
    logo = models.CharField(max_length=50)
    head = models.CharField(max_length=50)
    detail = models.TextField()

    def __str__(self):
        return self.head
