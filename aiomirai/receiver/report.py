from quart import Quart, Response, abort, jsonify, request

from . import Receiver


class ReportReceiver(Receiver):
    def __init__(self, app: Quart, endpoint: str = '/mirai'):
        super().__init__()
        app.add_url_rule(path=endpoint,
                         endpoint=endpoint,
                         view_func=self._postreceive,
                         methods=['POST'])

    async def _postreceive(self) -> Response:
        payload = await request.json
        if not isinstance(payload, dict):
            abort(400)

        response = await self._handle_event(payload)
        if isinstance(response, dict):
            return jsonify(response)
        return Response('', 204)
