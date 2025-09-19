from django.db import models

from django.contrib.auth import get_user_model


#create the USer this is imp for authentication
User = get_user_model()
class Workspace(models.Model):
    #We create Workspace, and each workspace can have multiple pages. ✅
    #name is simply the title or label of the workspace.
    name = models.CharField(max_length=30)
    # If the user is Prathamesh, the system needs to know which workspaces belong to him. ✅
    # That’s why we add the owner field, which is a ForeignKey to the User table. ✅
    # on_delete=models.CASCADE ensures that if Prathamesh (the user) is deleted, all his workspaces are automatically deleted. ✅
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workspaces")

class Page(models.Model):
    title = models.CharField(max_length=30)
    workpace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Block(models.Model):
    pasblock_type =[
        ("text", "Text"),
        ("heading", "Heading"),
        ("checklist", "Checklist"),
    ]
    content =models.TextField()
    page =models.CharField()
    order=models.IntegerField()