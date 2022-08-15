from django.contrib import admin
from assessment.models import Comment, Assessment

class CommentAdmin(admin.ModelAdmin):
    list_display=['user', 'shoes', 'title', 'content']
    
admin.site.register(Comment, CommentAdmin)

class AssessmentAdmin(admin.ModelAdmin):
    list_display=['user', 'shoes', 'assessment', ]
    
admin.site.register(Assessment, AssessmentAdmin)
