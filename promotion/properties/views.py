# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from promotion.properties.models import Assets, AssetsImg
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
import json
# Create your views here.
return_str = {
    'success': True,
    'status': 200,
    'data': '',
}

def user_list(request):
    return JsonResponse({'success': True, 'assets': []})

# @require_http_methods(['GET'])
def assets_query(request):
    ASSETS_DATA = Assets.objects.all()
    # return JsonResponse({'asdf':123})
    if ASSETS_DATA:
        def format_list(x):
            tmp_data = {
                'title': x.title,
                'id': x.id,
                # 'summary': '/'.join(json.loads(x.parms).values()),
                'summary': '/'.join(x.parms.values()),
                # 'parms': json.loads(x.parms),
                'parms': x.parms,
                # 'instruction': json.loads(x.instruction),
                'instruction': x.instruction,
                'pub_time': x.pub_time.strftime('%Y-%m-%d %H:%M:%S'),
                'category': x.category.name,
                'contacts': x.contacts,
                'debt_type': x.debt_type,
            }
            return tmp_data
        import pdb;pdb.set_trace()
        data = map(format_list, ASSETS_DATA)
        return_str['data'] = data
    else:
        return_str['success'], return_str['status'] = False, 400
    return JsonResponse(return_str)
    # return JsonResponse()


def assets_detail(request, assets_id):
    assets = get_object_or_404(Assets, id=assets_id)
    return JsonResponse({'data': assets.json_data})


@require_http_methods(['POST'])
@csrf_exempt
def assets_create(request):
    json_data = json.loads(request.body)
    print json_data
    title = json_data.get('title')
    debt_type = json_data.get('debt_type')
    instruction = json_data.get('instruction')
    parms = json_data.get('parms')
    bond_institution = json_data.get('bond_institution')
    obligor = json_data.get('obligor')
    guarantee = json_data.get('guarantee')
    mortgagor = json_data.get('mortgagor')
    spot = json_data.get('spot')
    contacts = json_data.get('contacts')
    c_phone = json_data.get('c_phone')
    fax = json_data.get('fax')
    transaction = json_data.get('transaction')
    statement = json_data.get('statement')
    category_id = json_data.get('category_id')
    # import pdb; pdb.set_trace()
    large_img = json_data.get('large_img')
    middle_img = json_data.get('middle_img')
    small_img = json_data.get('small_img')
    new_assets = Assets(title=title, debt_type=debt_type, instruction=instruction,
                        parms=parms, bond_institution=bond_institution, obligor=obligor,
                        guarantee=guarantee, mortgagor=mortgagor, spot=spot, contacts=contacts,
                        c_phone=c_phone, fax=fax, transaction=transaction, statement=statement,
                        category_id=category_id)
    new_assets.save()
    assets_img = AssetsImg(large=large_img, small=small_img,
                           middle=middle_img, assets=new_assets)
    assets_img.save()
    return JsonResponse({'success': True})

@require_http_methods(['POST'])
@csrf_exempt
def post(request):
    img = request.FILES.get('img')
    json_data = json.loads(request.body)
    # json_data = {'name':'zhangsan','age':'12'}
    import pdb; pdb.set_trace()
    print json_data
    # img = 
    assets_img = AssetsImg(large=img, small=img,
                           middle=img, assets_id=1)
    assets_img.save()
    name = json_data.get('name')
    age = json_data.get('age')
    # print name,age
    return JsonResponse({'name': name, 'age': age})





