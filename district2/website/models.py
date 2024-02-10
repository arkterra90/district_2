from django.db import models

class ContactForm(models.Model):
    formName = models.CharField(max_length=255)
    formEmail = models.CharField(max_length=255)
    formPhone = models.CharField(max_length=20)
    formMessage = models.TextField()
    formVolunteer = models.BooleanField(default=False)
    formYardSign = models.BooleanField(default=False)
    formDoorHangers = models.BooleanField(default=False)
    formLargeSign = models.BooleanField(default=False)
    formMeetAndGreet = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.formName} {self.formEmail} {self.formPhone} {self.formMessage} {self.formVolunteer} {self.formYardSign} {self.formDoorHangers} {self.formLargeSign} {self.formMeetAndGreet}"
    

class blogPost(models.Model):

    author = models.CharField(max_length=15)
    dateMade = models.DateField()
    title = models.CharField(max_length=45)
    text = models.TextField()
    photo = models.ImageField()


    def __str__(self):
        return f"{self.id} {self.author} {self.dateMade} {self.text} {self.photo}"