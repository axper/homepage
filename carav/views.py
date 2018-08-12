import logging
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST, require_GET

from carav import models

logger = logging.getLogger(__name__)


@require_POST
def create_water_fountain(request):
    """
    Creates a water fountain object in the db with given lat/lng.

    :param request: HTTP POST request, contains 'lat' and 'lng' required params which contain floating-point numbers
    :return: HTTP 200/OK JSON response
    """
    if 'lat' not in request.POST:
        logger.error('lat not in request')
        return HttpResponseBadRequest('lat is required')
    if 'lng' not in request.POST:
        logger.error('lng not in request')
        return HttpResponseBadRequest('lng is required')
    lat = request.POST['lat']
    lng = request.POST['lng']
    if models.WaterFountain.objects.filter(lat=lat, lng=lng).exists():
        logger.error('Duplicate latitude and longitude')
        return HttpResponseBadRequest('duplicate latitude and longitude')
    water_fountain = models.WaterFountain.objects.create(lat=lat, lng=lng)
    logger.info('Created a new water fountain: {}'.format(water_fountain))
    return JsonResponse({'id': water_fountain.id})


@require_GET
def all_water_fountains(request):
    """
    Retrieves a list of every water fountain in db.

    :param request: HTTP GET request
    :return: HTTP 200/OK JSON response, contains 'data' object: a list where each element is object with following keys:
    `lat`, `lng`, `id`
    """
    all_fountains = models.WaterFountain.objects.filter(deleted=False)
    all_list = [{'lat': water_fountain.lat, 'lng': water_fountain.lng, 'id': water_fountain.id}
                for water_fountain in all_fountains]
    return JsonResponse({'data': all_list})


@require_POST
def delete_water_fountain(request):
    """
    Soft deletes the water fountain with given id.

    :param request: HTTP DELETE request, contains single param: id
    :return: HTTP SUCCESS response
    """
    if 'id' not in request.POST:
        logger.error('id not in request')
        return HttpResponseBadRequest('id is required')
    water_fountain_id = request.POST['id']
    if not models.WaterFountain.objects.filter(id=water_fountain_id).exists():
        logger.error('water fountain does not exist')
        return HttpResponseBadRequest('water fountain with id {} does not exist'.format(water_fountain_id))
    water_fountain = models.WaterFountain.objects.get(id=water_fountain_id)
    if water_fountain.deleted:
        logger.error('water fountain already deleted')
        return HttpResponseBadRequest('already deleted')
    water_fountain.deleted = True
    water_fountain.save()
    logger.info('Deleted water fountain with id {}: {}'.format(water_fountain_id, water_fountain))
    return JsonResponse({})


@require_POST
def update_water_fountain(request):
    """
    Updates the marker with given id to new coordinates

    :param request: HTTP POST request, contains `id`, `lat`, `lng`
    :return: HTTP SUCCESS response
    """
    if 'id' not in request.POST:
        logger.error('no id in request')
        return HttpResponseBadRequest('id is required')
    if 'lat' not in request.POST:
        logger.error('no lat in request')
        return HttpResponseBadRequest('lat is required')
    if 'lng' not in request.POST:
        logger.error('no lng in request')
        return HttpResponseBadRequest('lng is required')
    water_fountain_id = request.POST['id']
    if not models.WaterFountain.objects.filter(id=water_fountain_id).exists():
        logger.error('water fountain does not exist with given id: {}'.format(water_fountain_id))
        return HttpResponseBadRequest('water fountain with id {} does not exist'.format(water_fountain_id))
    water_fountain = models.WaterFountain.objects.get(id=water_fountain_id)
    water_fountain.lat = request.POST['lat']
    water_fountain.lng = request.POST['lng']
    water_fountain.save()
    logger.info('Updated water fountain: {}'.format(water_fountain))
    return JsonResponse({})
