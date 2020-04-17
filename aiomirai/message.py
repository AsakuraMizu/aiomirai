import re
from typing import Any, Dict, Iterable, Optional, Tuple, Union

from .utils import camelCase


class MessageSegment(dict):
    """
    消息段，即表示成字典的 Mirai 消息对象。
    不建议手动构造消息段；建议使用此类的静态方法构造，例如：
    ```py
    at_seg = MessageSegment.at(target=10001000)
    ```
    可进行判等和加法操作，例如：
    ```py
    assert at_seg == MessageSegment.at(target=10001000)
    msg: MessageChain = at_seg + MessageSegment.face(face_id=14)
    ```
    """
    def __init__(self,
                 d: Optional[Dict[str, Any]] = None,
                 *,
                 type: Optional[str] = None,
                 **extra):
        super().__init__()
        if isinstance(d, dict) and d.get('type'):
            self.update(d)
        elif type:
            self.type = type
            self.update(extra)
        else:
            raise ValueError('the \'type\' field cannot be None or empty')

    @property
    def type(self):
        return self['type']

    @type.setter
    def type(self, type_):
        self['type'] = type_

    def __str__(self):
        params = ','.join(f'{k}={str(self[k])}'
                          for k in self.keys() - {'type'})
        if params:
            params = '::' + params
        return '[{}{}]'.format(self.type, params)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, MessageSegment):
            return False
        return self.type == other.type and super().__eq__(other)

    def __add__(self, other: Any):
        return MessageChain(self).__add__(other)


def At(target: int) -> MessageSegment:
    return MessageSegment(type='At', target=target)


def AtAll() -> MessageSegment:
    return MessageSegment(type='AtAll')


def Face(face: Union[int, str]) -> MessageSegment:
    if isinstance(face, int):
        return MessageSegment(type='Face', face_id=face)
    else:
        return MessageSegment(type='Face', name=face)


def Plain(text: str) -> MessageSegment:
    return MessageSegment(type='Plain', text=text)


def Image(image: str) -> MessageSegment:
    if re.match(
            r'\{[A-F0-9]{8}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{12}\}.png',
            image
    ) or re.match(
            r'/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}',
            image):
        return MessageSegment(type='Image', image_id=image)
    elif image.startswith(('http://', 'https://', 'ftp://')):
        return MessageSegment(type='Image', url=image)
    else:
        return MessageSegment(type='Image', path=image)


def FlashImage(image: str) -> MessageSegment:
    if re.match(
            r'\{[A-F0-9]{8}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{12}\}.png',
            image
    ) or re.match(
            r'/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}',
            image):
        return MessageSegment(type='FlashImage', image_id=image)
    elif image.startswith(('http://', 'https://', 'ftp://')):
        return MessageSegment(type='FlashImage', url=image)
    else:
        return MessageSegment(type='FlashImage', path=image)


def Xml(xml: str) -> MessageSegment:
    return MessageSegment(type='Xml', xml=xml)


def Json(json: str) -> MessageSegment:
    return MessageSegment(type='Json', json=json)


def App(content: str) -> MessageSegment:
    return MessageSegment(type='App', content=content)


def Poke(name: str) -> MessageSegment:
    return MessageSegment(type='Poke', name=name)


class MessageChain(list):
    """
    消息，即消息段列表。
    """
    def __init__(self, msg: Any = None, *args, **kwargs):
        """``msg`` 参数为要转换为 `MessageChain` 对象的字符串、列表或字典。"""
        super().__init__(*args, **kwargs)
        try:
            if isinstance(msg, list):
                self.extend(msg)
            elif isinstance(msg, (dict, str)):
                self.append(msg)
        except ValueError:
            raise ValueError('the msg argument is not recognizable')

    def __str__(self):
        return ''.join(map(str, self))

    def __repr__(self):
        return self.__str__()

    def __add__(self, other: Any):
        result = MessageChain(self)
        try:
            if isinstance(other, MessageChain):
                result.extend(other)
            elif isinstance(other, MessageSegment):
                result.append(other)
            elif isinstance(other, list):
                result.extend(map(MessageSegment, other))
            elif isinstance(other, (dict, str)):
                result.append(MessageSegment(other))
            return result
        except ValueError:
            raise ValueError('the addend is not a valid message')

    def append(self, obj: Any) -> Any:
        """在消息末尾追加消息段。"""
        try:
            if isinstance(obj, MessageSegment):
                if self and self[-1].type == 'Plain' and obj.type == 'Plain':
                    self[-1]['text'] += obj['text']
                elif obj.type != 'text' or obj['text'] or not self:
                    super().append(obj)
            elif isinstance(obj, str):
                self.append(Plain(obj))
            else:
                self.append(MessageSegment(obj))
            return self
        except ValueError:
            raise ValueError('the object is not a valid message segment')

    def extend(self, msg: Any) -> Any:
        """在消息末尾追加消息（消息段列表）。"""
        try:
            for seg in msg:
                self.append(seg)
            return self
        except ValueError:
            raise ValueError('the object is not a valid message')

    def reduce(self) -> None:
        """
        化简消息，即去除多余消息段、合并相邻纯文本消息段。
        由于 `MessageChain` 类基于 `list`，此方法时间复杂度为 O(n)。
        """
        idx = 0
        while idx < len(self):
            if idx > 0 and self[idx -
                                1].type == 'text' and self[idx].type == 'text':
                self[idx - 1]['text'] += self[idx]['text']
                del self[idx]
            else:
                idx += 1

    def extract_plain_text(self, reduce: bool = False) -> str:
        """
        提取消息中的所有纯文本消息段，合并，中间用空格分隔。
        ``reduce`` 参数控制是否在提取之前化简消息。
        """
        if reduce:
            self.reduce()

        result = ''
        for seg in self:
            if seg.type == 'text':
                result += ' ' + seg['text']
        if result:
            result = result[1:]
        return result
