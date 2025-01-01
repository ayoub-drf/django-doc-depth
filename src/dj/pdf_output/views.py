from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from csv_output.models import Product

def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition'] = 'attachment; filename="products.pdf"'
    
    p = canvas.Canvas(response, pagesize=letter)
    
    p.setFont("Helvetica", 12)
    
    p.drawString(100, 750, "Product List Report")

    p.drawString(100, 730, "Name")
    p.drawString(200, 730, "Price")
    p.drawString(300, 730, "Stock Quantity")
    
    products = Product.objects.all()
    
    y_position = 710
    for product in products:
        p.drawString(100, y_position, product.name)
        p.drawString(200, y_position, str(product.price))
        p.drawString(300, y_position, str(product.stock_quantity))
        y_position -= 20 

    p.drawString(200, y_position - 80, "ended")

    
    p.showPage()
    p.save()
    
    return response
