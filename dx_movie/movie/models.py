from django.db import models
from django.db.models import TextChoices,IntegerChoices,BooleanField
# 导入验证器
from django.core.validators import MinValueValidator, MaxValueValidator
# 导入 User 模型 (假设使用 Django 默认用户模型)
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Category(models.Model):
    id = models.AutoField(primary_key=True) #自增主键
    # CharField字符串类型存储分类名称
    category_name = models.CharField(max_length=100,verbose_name='分类名')
    # TextField支持长文本描述
    description = models.TextField(verbose_name='描述',blank=True)
    def __str__(self):
            return self.category_name
    
    class Meta:
        #后台管理显示名字
        verbose_name = '电影分类'
        verbose_name_plural = '电影分类'
        
        
    
# 地区
class RegionChoices(IntegerChoices):
    MAINLAND = '1', '中国大陆'
    HONGKONG = '2', '中国香港'
    TAIWAN = '3', '中国台湾'
    USA = '4', '美国'
    KOREA = '5', '韩国'
    JAPAN = '6', '日本'
    OTHER = '7', '其他'

# 清晰度
class QualityChoices(IntegerChoices):
    HD_720P = '1', '720P'
    HD_1080P = '2', '1080P'
    UHD_4K = '3', '4K'

class LanguageChoices(IntegerChoices):
    """语言选项"""
    Simplified_Chinese = '1','简体中文'
    English = '2','英文'
    Japanese = '3','日语'

    
class Movie(models.Model):
    # 电影信息
    id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100,verbose_name='电影名')
    release_year = models.IntegerField(verbose_name='上映年份')
    director = models.CharField(max_length=100,verbose_name='导演')
    scriptwriter = models.CharField(max_length=100,verbose_name='编剧')
    actors = models.CharField(max_length=200,verbose_name='主演')
    region = models.SmallIntegerField(choices=RegionChoices,verbose_name='地区')
    types = models.CharField(max_length=50,verbose_name='类型')
    language = models.SmallIntegerField(choices=LanguageChoices,verbose_name='语言')
    release_date = models.DateField(verbose_name='上映日期')
    duration = models.CharField(max_length=50,verbose_name='时长(或集数)')
    alternate_name = models.CharField(max_length=100,blank=True,verbose_name='又名')
    image_url = models.CharField(max_length=300,blank=True,verbose_name='图片链接')
    rate = models.FloatField(
        blank=True, 
        verbose_name='评分',
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    review = models.TextField(max_length=500,blank=True,verbose_name='简介')
    is_hot = models.BooleanField(choices=((False, '非热门'), (True, '热门')), default=False, verbose_name='是否热门')
    is_top = models.BooleanField(choices=((False,'不置顶'),(True,'置顶')), default=False, verbose_name='是否置顶')
    quality = models.SmallIntegerField(choices=QualityChoices,blank=False,verbose_name='清晰度')
    subtitle = models.CharField(max_length=100,blank=True,verbose_name='字幕')
    update_info = models.CharField(max_length=100,blank=True,verbose_name='更新信息')
    update_progress = models.CharField(max_length=100,blank=True,verbose_name='更新进度')
    homepage = models.URLField(max_length=500, blank=True, verbose_name='电影主页',help_text="电影主页链接")
    is_show = models.BooleanField(choices=((False,'不显示'),(True,'显示')), default=True, verbose_name='是否显示')
    # 设置外键关联
    category = models.ForeignKey(Category,blank=False,verbose_name='分类名', on_delete=models.CASCADE) 
    # 添加创建时间和更新时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # 添加收藏关系
    collectors = models.ManyToManyField(
        User,
        related_name='collected_movies',
        verbose_name='收藏用户',
        blank=True
    )
    
    def __str__(self):
        return self.movie_name
    
    class Meta:
        #后台管理显示名字
        verbose_name = '电影'
        verbose_name_plural = '电影'