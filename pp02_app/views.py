import json

from django.views.decorators.csrf import csrf_exempt
from pp02_app.models import Masters, Details, Orders, PartsManufacturing, Machines
from django.http import JsonResponse


@csrf_exempt
def get_masters_data(request):
    result = [{
        "id": i.id,
        "last_name": i.last_name,
        "first_name": i.first_name,
        "father_name": i.father_name,
        "qualification": i.qualification,
        "work_experience": i.work_experience
    } for i in Masters.objects.all()]
    return JsonResponse({"result": result})


@csrf_exempt
def add_order(request):
    data = json.loads(request.body.decode())
    order = Orders(
        order_date=data['order_date'],
        client=data['client'],
        quantity=data['quantity']
    )
    order.save()
    return JsonResponse({"result": 'Заказ успешно добавлен!'})


@csrf_exempt
def update_machine(request):
    data = json.loads(request.body.decode())
    machines = Machines.objects.get(id=data['id'])
    if 'model' in data:
        machines.model = data['model']
    if 'manufacturer' in data:
        machines.manufacturer = data['manufacturer']
    if 'year_of_release' in data:
        machines.year_of_release = data['year_of_release']
    machines.save()
    return JsonResponse({"result": 'Данные станка успешно изменены!'})


@csrf_exempt
def del_detail(request):
    data = json.loads(request.body.decode())
    detail = Details.objects.get(id=data['id'])
    detail.delete()
    return JsonResponse({"result": 'Деталь успешно удалена!'})
