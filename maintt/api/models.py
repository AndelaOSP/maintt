from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    '''
    UserProfile model, and extension of the Django User models
    '''
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile')
    user_level = models.IntegerField(default=1)
    department = models.CharField(max_length=100)
    admin_level = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username


@receiver(pre_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    '''
    A pre-book for deleting a User, firsts deletes the
    associated UserProfile.
    '''
    if instance:
        user_profile = UserProfile.objects.get(user=instance)
        user_profile.delete()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance=None, created=False, **kwargs):
    '''
    A post-hook for creating a user, creates an associated
    UserProfile instance
    '''
    if created:
        UserProfile.objects.create(user=instance)


class Notification(models.Model):
    '''
    Stores user's notifications
    '''
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    notification = models.TextField()
    created_at = models.DateTimeField()
    read = models.BooleanField()

class IssueState(models.Model):
    '''
    Stores the state of an Issue, eg. open, closed, complete, etc.
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField()

class Issue(models.Model):
    '''
    Issue models
    '''
    id = models.AutoField(primary_key=True)
    state = models.ForeignKey(IssueState, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField()

class IssueAssignment(models.Model):
    '''
    Stores information on who is assigned which Issue
    '''
    id = models.AutoField(primary_key=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    staff = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

class IssueStateTracker(models.Model):
    '''
    Keeps track of the changes in the Issue status
    '''
    id = models.AutoField(primary_key=True)
    state_id_from = models.IntegerField()
    state_to = models.ForeignKey(IssueState, on_delete=models.CASCADE)
