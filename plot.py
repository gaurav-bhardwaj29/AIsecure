from track import df
from bokeh.plotting import figure,show,output_file,curdoc
from bokeh.models import HoverTool,ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S.%f")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S.%f")

cds=ColumnDataSource(df)
curdoc().theme = 'dark_minimal'

p=figure(x_axis_type='datetime',height=300,width=400,sizing_mode='stretch_width',title='Motion Plot')
p.yaxis.minor_tick_line_color=None

hover = HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

q = p.quad(left='Start',right="End",bottom=0,top=0.5,color='blue',alpha=0.5,source=cds)

output_file('graph.html')
show(p)

