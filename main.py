from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing

doc = SimpleDocTemplate("report.pdf", pagesize=A4)
style = getSampleStyleSheet()

title = Paragraph("Data Analytics Snapshot", style['Title'])

data = [
    ['Product', 'Quantity', 'Price', 'Total'],
    ['Laptop Pro', '15', '$1,200', '$18,000'],
    ['Wireless Mouse', '50', '$25', '$1,250'],
    ['Total', '', '', '$19,250']
]

table = Table(data, style=[('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),])

chart = Drawing(400, 200)

bar_chart = VerticalBarChart()
quantities = [int(row[1]) for row in data[1:-1]]
bar_chart.data = [quantities]  
bar_chart.categoryAxis.categoryNames = [row[0] for row in data[1:-1]]
bar_chart.valueAxis.valueMin = 0
bar_chart.valueAxis.valueMax = max(quantities) + 10 
bar_chart.valueAxis.valueStep = 10
bar_chart.x = 50
bar_chart.y = 50
bar_chart.height = 125
bar_chart.width = 300

chart.add(bar_chart)
doc.build([title, Spacer(1, 12), table, Spacer(1, 12), chart])