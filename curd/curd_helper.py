import traceback
from typing import TypeVar, Any, Tuple
from django.utils import timezone
from utils.loguru_settings import logger
from apps.basic.base_model import BaseTable

BModel = TypeVar("BModel", bound=BaseTable)


def create(creator: str, model: BModel, payload: dict) -> int:
    try:
        obj = model.objects.create(creator=creator, **payload)
        logger.info(
            f"input: create={model.__name__}, payload={payload},id: {obj.id}")
        return obj.id
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e


def get_or_create(model: BModel, filter_kwargs: dict,
                  defaults: dict) -> Tuple[Any, bool]:
    logger.info(
        f"input: get_or_create={model.__name__}, filter_kwargs={filter_kwargs}, defaults={defaults}"
    )
    obj, created = model.objects.get_or_create(
        defaults=defaults,
        **filter_kwargs,
    )
    return obj, created


def update(
    obj,
    updater: str,
    payload: dict,
) -> int:
    logger.info(
        f"input: update model={obj.__class__.__name__}, id={obj.id}, payload={payload}"
    )
    if updater:
        obj.updater = updater
    for attr, value in payload.items():
        if hasattr(obj, attr) is False:
            logger.info(f"{attr} not in obj fields, it will not update")
        setattr(obj, attr, value)
        obj.update_time = timezone.now()
    try:
        obj.save()
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e
    logger.info(f"update {obj.__class__.__name__} success, id: {obj.id}")
    return obj.id


def soft_delete_obj_by_pk(obj, updater: str):
    logger.info(
        f"input: soft delete model={obj.__class__.__name__}, id={obj.id}"
    )
    if updater:
        obj.updater = updater
    if hasattr(obj, "is_delete"):
        setattr(obj, "is_delete", 1)
        obj.update_time = timezone.now()
    try:
        obj.save()
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e
    logger.info(f"soft delete {obj.__class__.__name__} success, id: {obj.id}")
    return True
