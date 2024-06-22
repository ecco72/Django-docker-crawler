from django.db import models

# 建立資料庫的資料格式
class AgodaData(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    loc = models.CharField(max_length=255)
    link_url = models.URLField(max_length=200)
    photo_url = models.URLField(max_length=200)
    rate = models.FloatField()
    platform = models.CharField(max_length=50)

#使用Meta更改資料表名稱、排序方法、後臺顯示的資料庫資料表名稱
    class Meta:
        db_table = "all_rooms_data"
        ordering = ['price']
        verbose_name = "訂房網站資料"
        verbose_name_plural = "訂房網站資料集"  