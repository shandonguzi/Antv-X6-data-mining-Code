# from django.db import models
#
#
# class Yuanweihua(models.Model):
#     SepalLength = models.DecimalField(db_column='SepalLength', max_digits=10, decimal_places=2, blank=True, null=True)
#     SepalWidth = models.DecimalField(db_column='SepalWidth', max_digits=10, decimal_places=2, blank=True, null=True)
#     PetalLength = models.DecimalField(db_column='PetalLength', max_digits=10, decimal_places=2, blank=True, null=True)
#     PetalWidth = models.DecimalField(db_column='PetalWidth', max_digits=10, decimal_places=2, blank=True, null=True)
#     Class = models.CharField(db_column='Class', max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'yuanweihua'
#
#
# class Graduateincome(models.Model):
#     Major_code = models.IntegerField(db_column='Major_code', blank=True, null=True)  # Field name made lowercase.
#     Major = models.CharField(db_column='Major', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     Major_category = models.CharField(db_column='Major_category', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     Total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
#     Employed = models.IntegerField(db_column='Employed', blank=True, null=True)  # Field name made lowercase.
#     Employed_full_time_year_round = models.IntegerField(db_column='Employed_full_time_year_round', blank=True, null=True)  # Field name made lowercase.
#     Unemployed = models.IntegerField(db_column='Unemployed', blank=True, null=True)  # Field name made lowercase.
#     Unemployment_rate = models.DecimalField(db_column='Unemployment_rate', max_digits=10, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
#     Median = models.IntegerField(db_column='Median', blank=True, null=True)  # Field name made lowercase.
#     P25th = models.IntegerField(db_column='P25th', blank=True, null=True)  # Field name made lowercase.
#     P75th = models.IntegerField(db_column='P75th', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'graduateIncome'
#
#
# class Userinfo(models.Model):
#     username = models.CharField(max_length=255, blank=True, null=True)
#     password = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'userInfo'
