from http import HTTPStatus
from flask import request, Response
from pathlib import Path

from src.infrastructure.env_config import Configuration

Configuration.get_config(Path(__file__).parent)  # This line is important to load the environment variables needed by the project!

from src.core.response_model.response_model import ResponseModel
from src.service.enum.service import EnumService


def get_nationality_enums(request_=request) -> Response:
    service_response = EnumService.get_response()
    response = ResponseModel.build_http_response(
        response_model=service_response,
        status=HTTPStatus.OK
    )
    return response

