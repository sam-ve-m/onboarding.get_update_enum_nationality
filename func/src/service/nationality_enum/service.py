from etria_logger import Gladsheim

from src.core.interfaces.service.nationality_enum.interface import INationalityEnumService
from src.domain.response.model import ResponseModel
from src.domain.response.status_code.enums import StatusCode
from src.repository.nationality_enum.repository import NationalityEnumRepository


class NationalityEnumService(INationalityEnumService):
    @classmethod
    def get_response(cls):
        service_response = []

        enums = NationalityEnumRepository.get_nationality_enum()
        for code, value in enums:
            service_response.append({"code": code, "value": value})

        service_response = ResponseModel.build_response(
            success=True, code=StatusCode.SUCCESS, message=None, result=service_response
        )
        return service_response
