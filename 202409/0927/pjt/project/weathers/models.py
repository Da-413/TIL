from django.db import models

class Weather(models.Model):
    date = models.DateField()  # 날짜
    temp_high_f = models.FloatField()  # 최고 기온 (F)
    temp_avg_f = models.FloatField()  # 평균 기온 (F)
    temp_low_f = models.FloatField()  # 최저 기온 (F)
    dew_point_high_f = models.FloatField()  # 최고 이슬점 (F)
    dew_point_avg_f = models.FloatField()  # 평균 이슬점 (F)
    dew_point_low_f = models.FloatField()  # 최저 이슬점 (F)
    humidity_high_percent = models.FloatField()  # 최고 습도 (%)
    humidity_avg_percent = models.FloatField()  # 평균 습도 (%)
    humidity_low_percent = models.FloatField()  # 최저 습도 (%)
    sea_level_pressure_high_inches = models.FloatField()  # 최고 해수면 기압 (inches)
    sea_level_pressure_avg_inches = models.FloatField()  # 평균 해수면 기압 (inches)
    sea_level_pressure_low_inches = models.FloatField()  # 최저 해수면 기압 (inches)
    visibility_high_miles = models.FloatField()  # 최고 가시거리 (miles)
    visibility_avg_miles = models.FloatField()  # 평균 가시거리 (miles)
    visibility_low_miles = models.FloatField()  # 최저 가시거리 (miles)
    wind_high_mph = models.FloatField()  # 최고 바람 속도 (MPH)
    wind_avg_mph = models.FloatField()  # 평균 바람 속도 (MPH)
    wind_gust_mph = models.FloatField()  # 바람 돌풍 속도 (MPH)
    precipitation_sum_inches = models.FloatField()  # 총 강수량 (inches)
    events = models.TextField(blank=True, null=True)  # 이벤트 (텍스트)