from http import HTTPStatus

import pytest

from ugc_service.tests.functional.testdata.users import films, jwt

pytestmark = pytest.mark.asyncio


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
                {"film_id": films[0]["film_id"],
                 "time": films[0]["time"]},
                {"status": HTTPStatus.OK,
                 "body":
                     {
                         "timestamp": films[0]["time"],
                         "status": True
                     }
                 },
        ),
        (
                {"film_id": films[1]["film_id"],
                 "time": films[1]["time"]},
                {"status": HTTPStatus.OK,
                 "body":
                     {
                         "timestamp": films[1]["time"],
                         "status": True
                     }
                 },
        ),
        (
                {"film_id": films[2]["film_id"],
                 "time": films[2]["time"]},
                {"status": HTTPStatus.OK,
                 "body":
                     {
                         "timestamp": films[2]["time"],
                         "status": True
                     }
                 },
        ),
        (
                {"film_id": films[3]["film_id"],
                 "time": films[3]["time"]},
                {"status": HTTPStatus.OK,
                 "body":
                     {
                         "timestamp": films[3]["time"],
                         "status": True
                     }
                 },
        ),
    ],
)
@pytestmark
async def test_set_views(make_post_request, query_data, expected_answer):
    # Arrange
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
    }
    body = {
        "film_id": query_data["film_id"],
        "time": query_data["time"]
    }
    # Act
    response = await make_post_request(
        "views", params=body, headers=headers
    )
    # Assert
    assert response["status"] == expected_answer["status"]
    assert response["body"]["status"] == expected_answer["body"]["status"]


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
                {"film_id": "dasdasda",
                 "time": films[0]["time"]},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
                {"film_id": films[1]["film_id"],
                 "time": "sdasdasda"},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
                {"film_id": films[2]["film_id"],
                 "time": ""},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
                {"film_id": films[3]["film_id"],
                 "time": "999999992321432423592398582385238"},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
    ],
)
@pytestmark
async def test_set_bad_views(make_post_request, query_data, expected_answer):
    # Arrange
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
    }
    body = {
        "film_id": query_data["film_id"],
        "time": query_data["time"]
    }
    # Act
    response = await make_post_request(
        "views", params=body, headers=headers
    )
    # Assert
    assert response["status"] == expected_answer["status"]


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
                {"film_id": films[0]["film_id"],
                 "time": films[0]["time"]},
                {"status": HTTPStatus.FORBIDDEN}
        ),
        (
                {"film_id": films[1]["film_id"],
                 "time": films[1]["time"]},
                {"status": HTTPStatus.FORBIDDEN}
        ),
        (
                {"film_id": films[2]["film_id"],
                 "time": films[2]["time"]},
                {"status": HTTPStatus.FORBIDDEN}
        ),
        (
                {"film_id": films[3]["film_id"],
                 "time": films[3]["time"]},
                {"status": HTTPStatus.FORBIDDEN}
        ),
    ],
)
@pytestmark
async def test_set_not_jwt(make_post_request, query_data, expected_answer):
    # Arrange
    body = {
        "film_id": query_data["film_id"],
        "time": query_data["time"]
    }
    # Act
    response = await make_post_request(
        "views", params=body
    )
    # Assert
    assert response["status"] == expected_answer["status"]
