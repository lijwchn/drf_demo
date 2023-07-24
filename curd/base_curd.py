from abc import ABC, abstractmethod
from typing import Any, Tuple, List
from rest_framework.generics import get_object_or_404
from curd import curd_helper


class BaseCURD(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def create_obj(self, creator: str, payload: Any) -> int:
        ...

    @abstractmethod
    def get_obj_by_pk(self, pk: int) -> Any:
        ...

    @abstractmethod
    def get_obj_by_unique_key(self, unique_key: dict) -> Any:
        ...

    @abstractmethod
    def get_or_create(self, filter_kwargs: dict,
                      defaults: dict) -> Tuple[Any, bool]:
        ...

    @abstractmethod
    def list_obj(self, page_filter: dict) -> List[dict]:
        ...

    @abstractmethod
    def update_obj_by_pk(self, pk: int, updater: str, payload: dict) -> int:
        ...

    @abstractmethod
    def delete_obj_by_pk(self, pk: int) -> bool:
        ...


class GenericCURD(BaseCURD):
    def create_obj(self, creator: str, payload: Any) -> int:
        return curd_helper.create(creator, self.model, payload)

    def get_obj_by_pk(self, pk: int) -> Any:
        return get_object_or_404(self.model, id=pk)

    def get_obj_by_unique_key(self, unique_key: dict) -> Any:
        return get_object_or_404(self.model, **unique_key)

    def get_or_create(self, filter_kwargs: dict,
                      defaults: dict) -> Tuple[Any, bool]:
        return curd_helper.get_or_create(self.model, filter_kwargs, defaults)

    def list_obj(self, page_filter: dict) -> List[Any]:
        return self.model.objects.filter(**page_filter)

    def update_obj_by_pk(self, pk: int, updater: str, payload: dict) -> int:
        return curd_helper.update(self.get_obj_by_pk(pk), updater, payload)

    def delete_obj_by_pk(self, pk: int) -> bool:
        self.get_obj_by_pk(pk).delete()
        return True

    def soft_delete_obj_by_pk(self, pk: int, updater: str) -> bool:
        obj = self.get_obj_by_pk(pk)
        return curd_helper.soft_delete_obj_by_pk(obj, updater)