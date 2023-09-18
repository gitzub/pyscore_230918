from django.db import models
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.core.validators import MinValueValidator, MaxValueValidator


class Part(models.Model):
    part = models.CharField(blank=False, max_length=20, unique=True, verbose_name="파트")

    def __str__(self):
        return "{}".format(self.part)


class Gamelist(models.Model):
    gamedate = models.DateField(verbose_name="날짜")
    part = models.ForeignKey(
        Part,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        verbose_name="파트",
        related_name="appliers_part",
    )
    gamememo = models.CharField(max_length=20, verbose_name="메모")

    def __str__(self):
        return "{} {} {}".format(self.gamedate, self.part, self.gamememo)


class Rankname(models.Model):
    rank = models.CharField(blank=False, max_length=20, unique=True, verbose_name="순위")

    def __str__(self):
        return "{}".format(self.rank)


class Score(models.Model):
    foreignkey = models.ForeignKey(
        Gamelist,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        verbose_name="foreignkey",
        related_name="appliers_Score_foreignkey",
    )
    username = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        verbose_name="이름",
        related_name="appliers_Score_username",
    )
    rank = models.ForeignKey(
        Rankname,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        verbose_name="순위",
        related_name="appliers_Score_rank",
    )
    coupon = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(2)],
        verbose_name="쿠폰",
    )

    def __str__(self):
        return "{} {} {} {}".format(
            self.foreignkey, self.username, self.rank, self.coupon
        )


class GameDetail(DetailView):
    model = Gamelist
    template_name = "aaatest_detail.html"
    context_object_name = "value"  # 변수값지정


class ViewGame(models.Model):
    id = models.IntegerField(primary_key=True)
    gamedate = models.DateField(verbose_name="날짜")
    part = models.CharField(max_length=1000000000)
    gamememo = models.CharField(max_length=20, verbose_name="메모")
    coupon = models.IntegerField()
    names = models.CharField(max_length=1000000000)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = "v_game"
