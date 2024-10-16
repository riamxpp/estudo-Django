from django.db import models
from datetime import date

class Todo(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    deadLine = models.DateField(verbose_name="Fim", null=False, blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ["deadLine"]

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()