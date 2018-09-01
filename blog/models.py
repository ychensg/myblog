from django.db import models

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)  # 博客标题
    body = models.TextField()                   # 博客正文
    timestamp = models.DateTimeField()          # 创建时间

class Article(models.Model):
    title = models.CharField(u"博客标题",max_length = 100)        #博客标题
    category = models.CharField(u"博客标签",max_length = 50,blank = True)       #博客标签
    pub_date = models.DateTimeField(u"发布日期",auto_now_add = True,editable=True)       
    update_time = models.DateTimeField(u'更新时间',auto_now=True,null=True)
    content = models.TextField(blank=True, null=True)  # 博客文章正文
 
    def __unicode__(self):
        return self.title
 
    class Meta:     #按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"
