from django.db import models

# Create your models here.


class Article (models.Model):
    DEVELPTMENT = "dv"
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMENT,"development"),
        (PERSONAL, "persnal")
    )

    title = models.CharField(max_length=200)
    contents = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=DEVELOPMENT,
    )

class Comments (models.Model) :
    article = models.ForeignKey (Article, on_delete=models.CASCADE)
    # 아티클을 상속해서 포린키를 갖고온다. on_delete이하부분 : 아티클 삭제시 이 모델도 삭제됨.
    # on_delete 이하부분을 다르게 설정해서 댓글있을때, 아티클 삭제가 안되게 하는 등 설정가능.
    username = models.CharField (max_length=50)
    contents = models.CharField (max_length=200)

class HashTag(modes.Model) :
    name = models.CharField(max_length=50)
