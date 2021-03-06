# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Dig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, license_id: int=None, pos_x: int=None, pos_y: int=None, depth: int=None):  # noqa: E501
        """Dig - a model defined in Swagger

        :param license_id: The license_id of this Dig.  # noqa: E501
        :type license_id: int
        :param pos_x: The pos_x of this Dig.  # noqa: E501
        :type pos_x: int
        :param pos_y: The pos_y of this Dig.  # noqa: E501
        :type pos_y: int
        :param depth: The depth of this Dig.  # noqa: E501
        :type depth: int
        """
        self.swagger_types = {
            'license_id': int,
            'pos_x': int,
            'pos_y': int,
            'depth': int
        }

        self.attribute_map = {
            'license_id': 'licenseID',
            'pos_x': 'posX',
            'pos_y': 'posY',
            'depth': 'depth'
        }
        self._license_id = license_id
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._depth = depth

    @classmethod
    def from_dict(cls, dikt) -> 'Dig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The dig of this Dig.  # noqa: E501
        :rtype: Dig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def license_id(self) -> int:
        """Gets the license_id of this Dig.

        ID of the license this request is attached to.  # noqa: E501

        :return: The license_id of this Dig.
        :rtype: int
        """
        return self._license_id

    @license_id.setter
    def license_id(self, license_id: int):
        """Sets the license_id of this Dig.

        ID of the license this request is attached to.  # noqa: E501

        :param license_id: The license_id of this Dig.
        :type license_id: int
        """
        if license_id is None:
            raise ValueError("Invalid value for `license_id`, must not be `None`")  # noqa: E501

        self._license_id = license_id

    @property
    def pos_x(self) -> int:
        """Gets the pos_x of this Dig.


        :return: The pos_x of this Dig.
        :rtype: int
        """
        return self._pos_x

    @pos_x.setter
    def pos_x(self, pos_x: int):
        """Sets the pos_x of this Dig.


        :param pos_x: The pos_x of this Dig.
        :type pos_x: int
        """
        if pos_x is None:
            raise ValueError("Invalid value for `pos_x`, must not be `None`")  # noqa: E501

        self._pos_x = pos_x

    @property
    def pos_y(self) -> int:
        """Gets the pos_y of this Dig.


        :return: The pos_y of this Dig.
        :rtype: int
        """
        return self._pos_y

    @pos_y.setter
    def pos_y(self, pos_y: int):
        """Sets the pos_y of this Dig.


        :param pos_y: The pos_y of this Dig.
        :type pos_y: int
        """
        if pos_y is None:
            raise ValueError("Invalid value for `pos_y`, must not be `None`")  # noqa: E501

        self._pos_y = pos_y

    @property
    def depth(self) -> int:
        """Gets the depth of this Dig.


        :return: The depth of this Dig.
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth: int):
        """Sets the depth of this Dig.


        :param depth: The depth of this Dig.
        :type depth: int
        """
        if depth is None:
            raise ValueError("Invalid value for `depth`, must not be `None`")  # noqa: E501

        self._depth = depth
