from django.contrib import admin
from environ.models import Environ

# Register your models here.


@admin.register(Environ)
class EnvironAdmin(admin.ModelAdmin):

    """Environ Admin Definition"""

    fieldsets = (
        (
            "ODN Data",
            {"fields": ("odn_data",)},
        ),
        (
            "Sea ​​Area",
            {
                "fields": (
                    "ocean",
                    "location",
                )
            },
        ),
        (
            "Coordinates",
            {"fields": ("lat", "lon")},
        ),
        (
            "Environ Info",
            {
                "fields": (
                    "temperature",
                    "oxygen",
                    "hydrogen",
                    "salt",
                    "turbidity",
                    "measurement_time",
                )
            },
        ),
    )

    list_display = (
        "ocean",
        "location",
        "lat",
        "lon",
        "temperature",
        "oxygen",
        "hydrogen",
        "salt",
        "turbidity",
        "measurement_time",
        "odn_data",
    )
    list_filter = (
        "ocean",
        "location",
        "odn_data",
    )
    search_fields = [
        "ocean",
        "location",
    ]


# Register your models here.
