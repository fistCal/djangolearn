from django.contrib import admin
from .models import testappVariety, SeatReview, Airplane, seatNumber

# Register your models here.
class seatReviewInline(admin.TabularInline):
    model = SeatReview
    extra = 2

class seatVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [seatReviewInline]

class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('seat_variety', )

class SeatNumberAdmin(admin.ModelAdmin):
    list_display = ('seat', 'seat_number')


admin.site.register(testappVariety, seatVarietyAdmin)
admin.site.register(Airplane, AirplaneAdmin)
admin.site.register(seatNumber, SeatNumberAdmin)