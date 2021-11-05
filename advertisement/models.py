from django.db import models


class JobAlert(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    company_logo = models.ImageField(blank=True, upload_to='advertisement_images/')
    company_name = models.CharField(max_length=50, blank=True)
    company_city = models.CharField(max_length=50, blank=True)
    company_country = models.CharField(max_length=50, blank=True)
    company_email = models.EmailField(blank=True)
    text = models.TextField(max_length=2000)

    # return the first name of the user_shop capitalized
    def save(self, *args, **kwargs):
        for file in ['company_name', 'company_city', 'company_country', 'text']:
            val = getattr(self, file, False)
            if val:
                setattr(self, file, val.capitalize())
                super(JobAlert, self).save(*args, **kwargs)


class Announcement(models.Model):
    photo = models.ImageField(blank=True, upload_to='advertisement_images/')
    text = models.TextField(max_length=2000)

    def clean(self):
        self.text = self.text.capitalize()

    def save(self, *args, **kwargs):
        #resizing image
        from PIL import Image
        super().save()  # saving image first
        img = Image.open(self.photo.path)  # Open image using self

        if img.height > 1 or img.width > 1:
            new_img = (100, 800)
            img.thumbnail(new_img)
            img.save(self.photo.path)  # saving image at the same path


    def __str__(self):
        return self.text[:10]


