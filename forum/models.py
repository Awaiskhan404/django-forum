from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Category(models.Model):
    order = models.IntegerField()
    title = models.CharField(max_length=60)

    def get_forums(self):
        return Forum.objects.filter(category=self.id)

    def __unicode__(self):
        return self.title

class Forum(models.Model):
    title = models.CharField(max_length=60)
    slug = slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)














# from photologue.models import Photo
# from django.utils.translation import ugettext_lazy as _
# try:
#     User = settings.AUTH_USER_MODEL
# except ImportError:  # django < 1.5
#     from django.contrib.auth.models import User

# POSTS_PER_PAGE = getattr(settings, 'POSTS_PER_PAGE', 10)

# class Category(models.Model):
#     order = models.IntegerField()
#     title = models.CharField(max_length=60)

#     def get_forums(self):
#         return Forum.objects.filter(category=self.id)

#     def __unicode__(self):
#         return self.title


# class Forum(models.Model):
#     title = models.CharField(max_length=60)
#     slug = slug = models.SlugField(unique=True)
#     description = models.TextField(blank=True, default='')
#     icon = models.ForeignKey(Photo, null=True, blank=True, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
#     creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

#     def __unicode__(self):
#         return self.title

#     def get_summary(self):
#         if len(self.description) > 50:
#             return self.description[:50] + '...'
#         return self.description

#     def get_visits(self):
#         vs = 0
#         for t in self.topic_set.all():
#             vs += t.visits
#         return vs

#     def has_seen(self, user=None):
#         if user.is_authenticated():
#             for t in self.topic_set.all():
#                 if not t.has_seen(user):
#                     return False
#         return True

#     def num_posts(self):
#         return sum([t.num_posts() for t in self.topic_set.all()])

#     def num_topics(self):
#         return self.topic_set.all().count()

#     def last_post(self):
#         if self.topic_set.count():
#             last = None
#             for t in self.topic_set.all():
#                 l = t.last_post()
#                 if l:
#                     if not last:
#                         last = l
#                     elif l.created > last.created:
#                         last = l
#             return last


# class Topic(models.Model):
#     title = models.CharField(max_length=60)
#     description = models.TextField(max_length=10000, blank=True, null=True)
#     # forum = models.ForeignKey(Forum)
#     forums = models.ManyToManyField(Forum)
#     block_top = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
#     updated = models.DateTimeField(auto_now=True)
#     closed = models.BooleanField(blank=True, default=False)
#     visits = models.IntegerField(default=0)
#     user_lst = models.TextField(blank=True, null=True)

#     def num_posts(self):
#         return self.post_set.count()

#     def num_replies(self):
#         return max(0, self.post_set.count() - 1)

#     def last_post(self):
#         if self.post_set.count():
#             return self.post_set.order_by("-created")[0]

#     def sum_visits(self, user_id=None):
#         if user_id:
#             if self.user_lst:
#                 lst = self.user_lst.split(',')
#                 if str(user_id) not in lst:
#                     self.user_lst += ',' + str(user_id)
#             else:
#                 self.user_lst = str(user_id)
#         self.visits += 1
#         self.save()

#     def has_seen(self, user=None):
#         if user.is_authenticated():
#             if self.user_lst:
#                 lst = self.user_lst.split(',')
#                 if str(user.id) in lst:
#                     return True
#             return False
#         return True

#     def __unicode__(self):
#         return unicode(self.creator) + " - " + self.title


# class Post(models.Model):
#     title = models.CharField(max_length=60, verbose_name=_("Title"))
#     created = models.DateTimeField(auto_now_add=True)
#     creator = models.ForeignKey(User, blank=True, null=True, related_name="%(class)s_posts", on_delete=models.CASCADE)
#     updated = models.DateTimeField(auto_now=True)
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     body = models.TextField(max_length=10000)
#     user_ip = models.GenericIPAddressField(blank=True, null=True)
#     telegram_id = models.CharField(max_length=20, blank=True, null=True)

#     def __unicode__(self):
#         return u"%s - %s - %s" % (self.creator, self.topic, self.title)

#     def get_post_num(self):
#         return Post.objects.filter(topic__id=self.topic_id).filter(created__lt=self.created).count()

#     def get_page(self):
#         return self.get_post_num() / POSTS_PER_PAGE + 1

#     def short(self):
#         return u"%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%Y-%m-%d %H:%M"))

#     def supershort(self):
#         return u"%s: %s" % (self.creator, self.created.strftime("%Y-%m-%d %H:%M"))

#     def get_absolute_url(self):
#         return u'/%s?page=%d#%d' % (self.topic.id, self.get_page(), self.id)

#     def save(self, *args, **kwargs):
#         self.topic.user_lst = str(self.creator.id)
#         self.topic.save()
#         super(Post, self).save(*args, **kwargs)

#     short.allow_tags = True


# class ProfaneWord(models.Model):
#     word = models.CharField(max_length=60)

#     def __unicode__(self):
#         return self.word