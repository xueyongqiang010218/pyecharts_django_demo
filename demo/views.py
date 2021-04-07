from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse,request
from demo.models import company
from pyecharts import options as opts
from pyecharts.charts import Bar


def index(request):
    z = company.objects.filter()
    c = (
        Bar()
        .add_xaxis([f"{i.name}" for i in z])
        .add_yaxis("人数", [f"{i.shu}" for i in z])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return HttpResponse(c.render_embed())