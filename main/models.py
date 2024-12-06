from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CharField


class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    yosh = models.PositiveSmallIntegerField()
    telefon_raqam = CharField(max_length=15)
    guruh = models.CharField(max_length=255)
    kurs = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"


class Muallif(models.Model):
    ism = models.CharField(max_length=255)
    t_yil = models.DateField(blank=True, null=True)
    jins = models.CharField(max_length=10, choices=(("erkak", "erkak"), ("ayol", "ayol")))
    millat = models.CharField(max_length=50, blank=True, null=True)
    tirik = models.BooleanField(default=False)
    kitob_soni = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"


class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=50)
    sahifa = models.PositiveSmallIntegerField()
    muqova = models.CharField(
        max_length=50,
        choices=(
            ("Qattiq", "Qattiq"),
            ("Yumshoq", "Yumshoq")
        )
    )
    muallif = models.ManyToManyField(Muallif)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"


class Kutubxonachi(models.Model):
    ISH_VAQTI = (
        ("08:00-13:00", "08:00-13:00"),
        ("13:00-18:00", "13:00-18:00"),
        ("18:00-23:00", "18:00-23:00")
    )
    ism = models.CharField(max_length=255)
    telefon_raqam = models.CharField(max_length=15)
    ish_vaqti = models.CharField(
        max_length=55,
        choices=ISH_VAQTI)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "Kutubxonachi"
        verbose_name_plural = "Kutubxonachilar"


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.SET_NULL, null=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.SET_NULL, null=True)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.SET_NULL, null=True)
    olingan_sana = models.DateTimeField(blank=True, null=True)
    qaytargan_sana = models.DateTimeField(blank=True, null=True)
    qaytardi = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.talaba}-{self.kitob}({self.kutubxonachi})"

    class Meta:
        verbose_name = "Rekord"
        verbose_name_plural = "Rekordlar"
