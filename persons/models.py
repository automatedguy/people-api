from django.db import models


class Person(models.Model):

    person = models.CharField(max_length=15, primary_key=True)
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

    def __str__(self):
        return self.person


class Introduction(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    introduction = models.CharField(max_length=300, default=None)

    class Meta:
        db_table = 'introduction'

    def __str__(self):
        return self.introduction


class Description(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    description = models.CharField(max_length=600)

    class Meta:
        db_table = 'description'

    def __str__(self):
        return self.description


class ContactInfo(models.Model):

    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    street = models.CharField(max_length=20)
    street_num = models.CharField(max_length=6)
    city_code = models.CharField(max_length=6)

    class Meta:
        db_table = 'contact_info'


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
        db_table = 'location_info'

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
    name = models.CharField(max_length=15)

    class Meta:
        db_table = 'photo'

    def __str__(self):
        return self.name


class Videos(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)

    class Meta:
        db_table = 'video'

    def __str__(self):
        return self.name
