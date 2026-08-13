from django.db import models

class Field(models.Model):          # branches of computer computing
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Branch(models.Model):              # Branches in each field
    field = models.ForeignKey(to='myweb.Field',on_delete=models.CASCADE,
        related_name='themes',null=True,)
    branch = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
       return f"{self.field.name} - {self.branch}"
    
class Topic(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    topic = models.CharField(max_length=30)
    dp = models.TextField()
    def __str__(self):
        return f'{self.topic}'

class Resource(models.Model):
    VIDEO = 'video'
    PDF = 'pdf'
    TEXT = 'text'
    RESOURCE_TYPES = [
        (VIDEO, 'Video'),
        (PDF, 'PDF'),
        (TEXT, 'Text only'),
    ]

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='resources')
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES, default=TEXT)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='resources/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'uploaded_at']

    def __str__(self):
        return self.title or self.file.name if self.file else self.title or 'Untitled'

