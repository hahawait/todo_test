import logging
import ssl
from dataclasses import dataclass, field
from typing import Literal, Any, Mapping

import backoff
from aiohttp import ClientSession, TCPConnector, ClientError
from orjson import loads

from infrastructure.clients.schemas.base import APIResponse


@dataclass
class APIClient:
    base_url: str
    _session: ClientSession | None = field(kw_only=True, default=None)

    def __post_init__(self):
        self.log = logging.getLogger(f"API Client {self.__class__.__name__}")

    async def _get_session(self) -> ClientSession:
        """Get aiohttp session with cache."""
        if self._session is None:
            ssl_context = ssl.SSLContext()
            connector = TCPConnector(ssl_context=ssl_context)
            self._session = ClientSession(
                base_url=self.base_url,
                connector=connector,
            )

        return self._session

    async def __aenter__(self):
        self._session = await self._get_session()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.close()
        self._session = None

    @backoff.on_exception(
        backoff.expo,
        ClientError,
        max_time=30,
    )
    async def _make_request(
            self,
            method: Literal["GET", "POST"],
            url: str,
            json: dict[str, Any] | None = None,
            params: Mapping[str, Any] | None = None,
            headers: Mapping[str, str] | None = None,
    ) -> APIResponse:
        """
        Request with 30 seconds backoff
        :param method: Method for request GET or POST
        :param params: Query params for request
        :param json: JSON body for POST request
        :param url: would be added to base url string
        """
        if self._session is None:
            raise ValueError("Session is not initialized")

        async with self._session.request(
                method, url, params=params, json=json, headers=headers
        ) as response:
            status = response.status
            try:
                result = await response.json(loads=loads)
            except Exception as e:
                self.log.exception(e)
                self.log.error(f"{await response.text()}")
                raise e

        return APIResponse(status=status, result=result)
