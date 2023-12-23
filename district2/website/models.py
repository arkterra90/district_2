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
    

