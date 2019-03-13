from django.db import models


class Person(models.Model):

    nickname = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    creation_date = models.DateField()
    active = models.BooleanField()
    _M_ = 'M'
    _F_ = 'F'
    _T_ = 'T'
    SEX = ((_M_, 'Male'), (_F_, 'Female'), (_T_, 'Trans'))
    sex = models.CharField(
        max_length=6,
        choices=SEX,
        default=_T_,
    )

    class Meta:
        db_table = 'person'
        ordering = ['-nickname']

    def __str__(self):
        return self.nickname


class Introduction(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, unique=True)
    introduction = models.CharField(max_length=300, default=None)

    class Meta:
        db_table = 'introduction'
        ordering = ['-person']

    def __str__(self):
        return self.introduction


class Description(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, unique=True)
    description = models.CharField(max_length=600)

    class Meta:
        db_table = 'description'
        ordering = ['-person']

    def __str__(self):
        return self.description


class ContactInfo(models.Model):

    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length=20)
    home = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    facebook = models.CharField(max_length=30)
    instagram = models.CharField(max_length=30)

    class Meta:
        db_table = 'contact_info'


class LocationInfo(models.Model):

    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    street = models.CharField(max_length=20)
    street_num = models.CharField(max_length=6)
    city_code = models.CharField(max_length=6)

    class Meta:
        db_table = 'location_info'


class Country(models.Model):

    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=15, unique=True)

    class Meta:
        db_table = 'country'

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=15, primary_key=True)

    class Meta:
        db_table = 'city'

    def __str__(self):
        return self.name


class Neighborhood(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=15, primary_key=True)

    class Meta:
        db_table = 'neighborhood'

    def __str__(self):
        return self.name


class Review(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    review = models.CharField(max_length=600, unique=True)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return self.review


class Photo(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        db_table = 'photo'

    def __str__(self):
        return self.name


class Videos(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    video = models.CharField(max_length=15)

    class Meta:
        db_table = 'video'

    def __str__(self):
        return self.name
