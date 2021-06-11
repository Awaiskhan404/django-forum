from django.db import models
from  django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, related_name="senders", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receivers', on_delete=models.CASCADE)
    content = models.CharField(max_length=2200)
    date_created = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('caseygram-home')

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)
        notify.send(self.sender, recipient=self.receiver, verb='sent you a ', description='message', target=self)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.content