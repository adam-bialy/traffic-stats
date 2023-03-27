from django.db import models


class SiteVisit(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    location = models.TextField(max_length=256, blank=True)

    # The choices below can be changed to suit the user's needs.
    # In this case:
    # `open` represent just entering the page,
    # `view` - scrolling to the end,
    # `read` - scrolling to the end and spending enough time on the page.
    OPEN = "open"
    VIEW = "view"
    READ = "read"
    interaction_choices = (
        (OPEN, "Open"),
        (READ, "View"),
        (VIEW, "Read"),
    )
    interaction_type = models.CharField(max_length=4, choices=interaction_choices)

    def __str__(self):
        name = f"SiteVisit Event {self.interaction_type}"
        if self.location:
            name += f" from {self.location}"
        return name
