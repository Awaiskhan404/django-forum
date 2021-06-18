from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=10000, blank=True, null=True)
    block_top = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(blank=True, default=False)
    visits = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=True)

    def get_questions(self):
        return Question.objects.filter(topic=self.id)

    def num_posts(self):
        return self.question_set.count()

    def num_replies(self):
        return max(0, self.question_set.count() - 1)

    def last_post(self):
        if self.question_set.count():
            return self.question_set.order_by("-created")[0]

    def sum_visits(self, user_id=None):
        if user_id:
            if self.user_lst:
                lst = self.user_lst.split(',')
                if str(user_id) not in lst:
                    self.user_lst += ',' + str(user_id)
            else:
                self.user_lst = str(user_id)
        self.visits += 1
        self.save()

    def has_seen(self, user=None):
        if user.is_authenticated():
            if self.user_lst:
                lst = self.user_lst.split(',')
                if str(user.id) in lst:
                    return True
            return False
        return True

    def __unicode__(self):
        return unicode(self.creator) + " - " + self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)



class Question(models.Model):
    title = models.CharField(max_length=60, verbose_name=("Title"))
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True, related_name="%(class)s_posts", on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    body = models.TextField(max_length=10000)
    user_ip = models.GenericIPAddressField(blank=True, null=True)
    views=models.IntegerField(default=0)

    def get_body(self):
        return self.body[:10]

    def __unicode__(self):
        return u"%s - %s - %s" % (self.creator, self.topic, self.title)

    def get_post_num(self):
        return Question.objects.filter(topic__id=self.topic_id).filter(created__lt=self.created).count()
    def get_answer_num(self):
        return Answers.objects.filter(question=self.id).count()
    def get_page(self):
        return self.get_post_num() / POSTS_PER_PAGE + 1

    def short(self):
        return u"%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%Y-%m-%d %H:%M"))

    def supershort(self):
        return u"%s: %s" % (self.creator, self.created.strftime("%Y-%m-%d %H:%M"))

    def get_absolute_url(self):
        return u'/%s?page=%d#%d' % (self.topic.id, self.get_page(), self.id)

    def save(self, *args, **kwargs):
        self.topic.user_lst = str(self.creator.id)
        self.topic.save()
        super(Question, self).save(*args, **kwargs)

    short.allow_tags = True

class Answers(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField()
class UserAvatar(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='avatars')