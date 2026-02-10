import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EquipmentDataset

@api_view(['POST'])
def upload_csv(request):
    file = request.FILES['file']

    df = pd.read_csv(file)

    type_dist = df['Type'].value_counts().to_dict()

    summary = {
        "total": len(df),
        "avg_flowrate": df['Flowrate'].mean(),
        "avg_pressure": df['Pressure'].mean(),
        "avg_temperature": df['Temperature'].mean(),
        "type_distribution": type_dist
    }

    EquipmentDataset.objects.create(
        total_equipment=summary["total"],
        avg_flowrate=summary["avg_flowrate"],
        avg_pressure=summary["avg_pressure"],
        avg_temperature=summary["avg_temperature"],
        type_distribution=str(type_dist)  
    )


    old_datasets = EquipmentDataset.objects.all().order_by('-uploaded_at')[5:]
    EquipmentDataset.objects.filter(id__in=old_datasets).delete()

    return Response(summary)
from ast import literal_eval
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import EquipmentDataset

def download_report(request):
    latest = EquipmentDataset.objects.last()

    if not latest:
        return HttpResponse("No data available", status=400)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="equipment_report.pdf"'

    c = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Chemical Equipment Analysis Report")

    y -= 40
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Total Equipment: {latest.total_equipment}")

    y -= 20
    c.drawString(50, y, f"Average Flowrate: {latest.avg_flowrate:.2f}")

    y -= 20
    c.drawString(50, y, f"Average Pressure: {latest.avg_pressure:.2f}")

    y -= 20
    c.drawString(50, y, f"Average Temperature: {latest.avg_temperature:.2f}")

    y -= 40
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Equipment Type Distribution")

    c.setFont("Helvetica", 12)
    type_dist = literal_eval(latest.type_distribution)

    for eq_type, count in type_dist.items():
        y -= 20
        c.drawString(70, y, f"{eq_type}: {count}")

    c.showPage()
    c.save()

    return response
