from django.db import models
from user.models import TimestampedModel


class KnowledgeBucket(TimestampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    uploaded_by = models.ForeignKey('user.CustomUser', 
                                    on_delete=models.SET_NULL, 
                                    null=True)
    archived = models.BooleanField(default=False)

    class Meta:
        abstract=True


class CompanyResearchData(KnowledgeBucket):

    def __str__(self):
        return self.title

class ClientData(KnowledgeBucket):
    client = models.ForeignKey('client.Client', 
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Document(TimestampedModel):
    title = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to='information_files')
    company_research_data = models.ForeignKey(CompanyResearchData, 
                                              on_delete=models.SET_NULL, 
                                              null=True)
    client_data = models.ForeignKey(ClientData, 
                                    on_delete=models.SET_NULL, 
                                    null=True)

    def __str__(self):
        return self.title

