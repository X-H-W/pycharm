from django.contrib import admin
from .models import Banner,About,Project,Case,Tags,Works,Knowledge,About_z,Message
# Register your models here.

admin.site.register(Banner)
# 关于我们
admin.site.register(About)
# 工程案例
admin.site.register(Project)
# 新闻质询
admin.site.register(Case)
# # 动态新闻
# admin.site.register(Trends)
# 成员
admin.site.register(Tags)
#分类
admin.site.register(Works)
# 环境
admin.site.register(Knowledge)
# 关于我们的主页面
admin.site.register(About_z)
# 留言版
admin.site.register(Message)