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
async def test_get_views(make_post_request, make_get_request, query_data,
                         expected_answer):
    # Arrange
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
    }
    body = {
        "film_id": query_data["film_id"],
        "time": query_data["time"]
    }
    _ = await make_post_request(
        "views", params=body, headers=headers
    )
    # Act
    response = await make_get_request(
        f"views/{query_data['film_id']}", headers=headers
    )
    # Assert
    assert response["status"] == expected_answer["status"]
    assert response["body"]["status"] == expected_answer["body"]["status"]
    assert response["body"]["timestamp"] == expected_answer["body"][
        "timestamp"]


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
                {"film_id": "dasdasda"},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
                {"film_id": ''},
                {"status": HTTPStatus.METHOD_NOT_ALLOWED},
        ),
        (
                {"film_id": '7f58c3ff-2308-423b-b217-98982528e4dd'},
                {"status": HTTPStatus.NOT_FOUND},
        )
    ],
)
@pytestmark
async def test_set_bad_views(make_get_request, query_data, expected_answer):
    # Arrange
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
    }
    # Act
    response = await make_get_request(
        f"views/{query_data['film_id']}", headers=headers
    )
    # Assert
    assert response["status"] == expected_answer["status"]


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
                {"film_id": films[0]["film_id"]},
                {"status": HTTPStatus.FORBIDDEN}
        ),
        (
                {"film_id": films[1]["film_id"]},
                {"status": HTTPStatus.FORBIDDEN}
        ),
        (
                {"film_id": films[2]["film_id"]},
                {"status": HTTPStatus.FORBIDDEN}
        ),
        (
                {"film_id": films[3]["film_id"]},
                {"status": HTTPStatus.FORBIDDEN}
        ),
    ],
)
@pytestmark
async def test_set_not_jwt(make_get_request, query_data, expected_answer):
    # Act
    response = await make_get_request(
        f"views/{query_data['film_id']}"
    )
    # Assert
    assert response["status"] == expected_answer["status"]
